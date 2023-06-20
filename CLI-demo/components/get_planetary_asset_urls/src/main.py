from pystac.extensions.eo import EOExtension as eo
import pystac_client
import planetary_computer as pc

import os
import json
import argparse
import mlflow

# to support image logging

import imageio
import numpy as np

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--aoi", default="[[[-148.56536865234375, 60.80072385643073], [-147.44338989257812, 60.80072385643073], [-147.44338989257812, 61.18363894915102], [-148.56536865234375, 61.18363894915102], [-148.56536865234375, 60.80072385643073]]]")
    parser.add_argument("--aoi-type", default="Polygon")
    parser.add_argument("--toi", default="2019-06-01/2019-08-01")
    parser.add_argument("--collections", default='["sentinel-2-l2a"]')
    parser.add_argument("--query", default='{"eo:cloud_cover": {"lt": 10}}')
    parser.add_argument("--output_location", default="./")
                 
    args, _ = parser.parse_known_args()
    print(args.aoi)
    print(type(args.aoi))
    
    mlflow.set_tags({"foo":"bar"})
    mlflow.set_tag("foz","baz")

    # The Hub sets PC_SDK_SUBSCRIPTION_KEY automatically.
    # pc.settings.set_subscription_key(<YOUR API Key>)

    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=pc.sign_inplace,
    )

    area_of_interest = {
        "type": args.aoi_type,
        "coordinates": json.loads(args.aoi),
    }

    mlflow.log_dict(area_of_interest, "area_of_interest.json")


    time_of_interest = args.toi

    mlflow.log_param("toi", args.toi)
    mlflow.log_param("query", args.query)


    search = catalog.search(
        collections=json.loads(args.collections),
        intersects=area_of_interest,
        datetime=time_of_interest,
        query=json.loads(args.query),
    )

    items = search.item_collection()

    # Let's log some stuff
    # item count as a metric
    mlflow.log_metric('items',len(items))

    # tile metadata as a json file
    metadata = [{
        "id": item.id,
        "date": str(item.datetime.date()),
        "cloud_cover":eo.ext(item).cloud_cover,
      } for item in items]
    mlflow.log_dict(metadata, "item_metadata.json")

    # cloud cover as a chart (many values for a metric)
    cloudiness = [eo.ext(item).cloud_cover for item in items]
    [mlflow.log_metric(key="cloud_cover", value=eo.ext(i).cloud_cover, step=s) for s,i in enumerate(items)]

    with open(os.path.join(args.output_location,'asset_hrefs.csv'), 'w') as f:
        [f.write(f"{item.assets['visual'].href}\n") for item in items]


    # print(
    #     f"Choosing {least_cloudy_item.id} from {least_cloudy_item.datetime.date()}"
    #     f" with {eo.ext(least_cloudy_item).cloud_cover}% cloud cover"
    # )

    #print(least_cloudy_item.assets.keys())
    #asset_href = least_cloudy_item.assets["visual"].href
    
    # lastly, let's fetch two images in their preview size and log them to the run

    def get_and_log(item):
        # imageio can read directly from the source
        im = imageio.imread(item.assets["preview"].href)
        # convert to numpy array and log the image object
        mlflow.log_image(np.asarray(im), f'{item.id}.png')
    
    least_cloudy_item = min(items, key=lambda item: eo.ext(item).cloud_cover)    
    most_cloudy_item = max(items, key=lambda item: eo.ext(item).cloud_cover)

    [get_and_log(item) for item in [least_cloudy_item,most_cloudy_item]]