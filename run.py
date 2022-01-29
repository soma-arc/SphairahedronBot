import subprocess
import datetime
import os
from collections import OrderedDict
import json
import random
import time

os.makedirs('./img', exist_ok=True)
os.makedirs('./scene', exist_ok=True)

while True:
    dt_now = datetime.datetime.now()
    time = dt_now.strftime('%Y-%m-%d_%H-%M-%S')
    filename = time +'-infiniteSphairahedron'

    scene = OrderedDict()
    scene['filename'] = '../img/'+ filename +'.png'
    scene['maxSamples'] = 5
    scene['windowWidth'] = 1024
    scene['windowHeight'] = 512

    scene['basePolyhedron'] = 'cube'
    imageTypes = ['infiniteSphairahedron',
                  'infiniteLimitSet',
                  'finiteSphairahedron',
                  'finiteLimitSet']
    scene['imageType'] = imageTypes[0]
    scene['angleType'] = 0

    scene['param1'] = random.uniform(-1.0, 1.0)
    scene['param2'] = random.uniform(-1.0, 1.0)

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

    # Write json files
    with open('./scene/'+ filename +'.json', 'w') as f:
        json.dump(scene, f,
                  sort_keys=False,
                  indent=4)

    scene['imageType'] = imageTypes[1]
    filename = time +'-infiniteLimitSet'
    scene['filename'] = '../img/'+ filename +'.png'
    with open('./scene/'+ filename +'.json', 'w') as f:
        json.dump(scene, f,
                  sort_keys=False,
                  indent=4)

    # Render images
    os.chdir('./SphairahedronFractalRenderer')
    subprocess.run(['./bin/native/Release/SphairahedronRenderer',
                    '-j', '../scene/'+ time +'-infiniteSphairahedron.json'],
                   check=True)
    subprocess.run(['./bin/native/Release/SphairahedronRenderer',
                    '-j', '../scene/'+ time +'-infiniteLimitSet.json'],
                   check=True)
    os.chdir('../')

    # Tweet
    subprocess.run(['python3','tweet.py',
                    '-i',
                    './img/'+ time +'-infiniteSphairahedron.png',
                    './img/'+ time +'-infiniteLimitSet.png',
                    '-d', time], check=True)

    time.sleep(60 * 10)
