import argparse
import json
from collections import OrderedDict
import datetime

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--filename')

args = parser.parse_args()

scene = OrderedDict()
scene['filename'] = '../img/'+ args.filename +'.png'
scene['maxSamples'] = 20
scene['windowWidth'] = 1024
scene['windowHeight'] = 512

scene['basePolyhedron'] = 'cube'
imageTypes = ['infiniteSphairahedron',
              'infiniteLimitSet',
              'finiteSphairahedron',
              'finiteLimitSet']
scene['imageType'] = imageTypes[0]
scene['angleType'] = 0

scene['param1'] = 0.1
scene['param2'] = 0.1

camera = OrderedDict()
camera['position'] = [0, 2, 3]
camera['target'] = [0, 0, 0]
camera['fovDegree'] = 60
camera['up'] = [0, -1, 0]
scene['camera'] = camera

inversionSphere = OrderedDict()
inversionSphere['type'] = 'default'
inversionSphere['center'] = [0, 0, 0]
inversionSphere['radius'] = 1
scene['inversionSphere'] = inversionSphere

with open('./scene/'+ args.filename +'.json', 'w') as f:
    json.dump(scene, f,
              sort_keys=False,
              indent=4)
