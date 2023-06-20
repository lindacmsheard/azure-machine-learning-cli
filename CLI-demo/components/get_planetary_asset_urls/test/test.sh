#!/bin/bash


python3 ../src/main.py \
--aoi "[[[-148.56536865234375, 60.80072385643073], [-147.44338989257812, 60.80072385643073], [-147.44338989257812, 61.18363894915102], [-148.56536865234375, 61.18363894915102], [-148.56536865234375, 60.80072385643073]]]" \
--aoi-type "Polygon" \
--toi "2019-06-01/2019-08-01" \
--collections '["sentinel-2-l2a"]' \
--query '{"eo:cloud_cover": {"lt": 10}}'
