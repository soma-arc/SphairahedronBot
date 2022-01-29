import subprocess
import datetime
import os
from collections import OrderedDict
import json
import random
import time

os.makedirs('./img', exist_ok=True)
os.makedirs('./scene', exist_ok=True)
angleType2alphabet = ['A', 'B', 'C', 'D', 'E', 'H', 'I']

while True:
    dt_now = datetime.datetime.now()
    strtime = dt_now.strftime('%Y-%m-%d_%H-%M-%S')
    filename = strtime +'-infiniteSphairahedron'

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
    scene['angleType'] = random.randint(0, 6)

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
    filename = strtime +'-infiniteLimitSet'
    scene['filename'] = '../img/'+ filename +'.png'
    with open('./scene/'+ filename +'.json', 'w') as f:
        json.dump(scene, f,
                  sort_keys=False,
                  indent=4)

    # Render images
    os.chdir('./SphairahedronFractalRenderer')
    subprocess.run(['./bin/native/Release/SphairahedronRenderer',
                    '-j', '../scene/'+ strtime +'-infiniteSphairahedron.json'],
                   check=True)
    subprocess.run(['./bin/native/Release/SphairahedronRenderer',
                    '-j', '../scene/'+ strtime +'-infiniteLimitSet.json'],
                   check=True)
    os.chdir('../')

    # Tweet
    description = strtime +', base polyhedron: '+ scene['basePolyhedron']+\
        ', angle type: '+ angleType2alphabet[scene['angleType']]+\
        ', zb = '+ str(scene['param1']) +', zc = '+ str(scene['param2'])

    subprocess.run(['python3','tweet.py',
                    '-i',
                    './img/'+ strtime +'-infiniteSphairahedron.png',
                    './img/'+ strtime +'-infiniteLimitSet.png',
                    '-d', description], check=True)

    print('Sleep...')
    time.sleep(60)
