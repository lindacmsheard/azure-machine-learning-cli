
from pystac.extensions.eo import EOExtension as eo
import pystac_client
import planetary_computer as pc

import subprocess

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--aoi-type", default="polygon")
    parser.add_argument("--toi")
    parser.add_argument("--collection")
    

    args, unparsed = parser.parse_known_args()
    
    print(args)

    # The Hub sets PC_SDK_SUBSCRIPTION_KEY automatically.
    # pc.settings.set_subscription_key(<YOUR API Key>)

    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=pc.sign_inplace,
    )

    area_of_interest = {
        "type": "Polygon",
        "coordinates": [
            [
                [-148.56536865234375, 60.80072385643073],
                [-147.44338989257812, 60.80072385643073],
                [-147.44338989257812, 61.18363894915102],
                [-148.56536865234375, 61.18363894915102],
                [-148.56536865234375, 60.80072385643073],
            ]
        ],
    }


    time_of_interest = "2019-06-01/2019-08-01"

    search = catalog.search(
        collections=["sentinel-2-l2a"],
        intersects=area_of_interest,
        datetime=time_of_interest,
        query={"eo:cloud_cover": {"lt": 10}},
    )

    # Check how many items were returned
    items = search.item_collection()
    print(f"Returned {len(items)} Items")


    least_cloudy_item = min(items, key=lambda item: eo.ext(item).cloud_cover)

    print(
        f"Choosing {least_cloudy_item.id} from {least_cloudy_item.datetime.date()}"
        f" with {eo.ext(least_cloudy_item).cloud_cover}% cloud cover"
    )

    asset_href = least_cloudy_item.assets["visual"].href

    subprocess.check_output(['wget', '-O', 'example_output_file.tif', asset_href])
    