# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license.

import os
import numpy as np
import argparse
from PIL import Image


def init():
    global args

    parser = argparse.ArgumentParser(allow_abbrev=False, description="ParallelRunStep Agent")
    parser.add_argument("--model", type=str, default=0)
    parser.add_argument("--output", type=str, default=0)
    args, _ = parser.parse_known_args()



def run(mini_batch):
    print(f'run method start: {__file__}, run({mini_batch})')
    resultList = []

    print(f'### mounted file output loc {args.output}')

    for image in mini_batch:
        # prepare each image
        data = Image.open(image)
        #np_im = np.array(data).reshape((1, 784))
        
        average = np.average(data)
        resultList.append("{}: {} ({})".format(os.path.basename(image), average, args.model))
        Image.save(os.path.join(args.output,os.path.basename(image)), format='PNG')


    return resultList