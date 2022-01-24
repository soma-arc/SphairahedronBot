import json
from collections import OrderedDict

scene = OrderedDict()
scene['maxSamples'] = 20
scene['windowWidth'] = 1024
scene['windowHeight'] = 512

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

print(json.dumps(scene,
                 sort_keys=False,
                 indent=4))
