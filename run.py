import subprocess
import datetime
import os

os.makedirs('./img', exist_ok=True)
os.makedirs('./scene', exist_ok=True)

dt_now = datetime.datetime.now()
filename = dt_now.strftime('%Y-%m-%d_%H-%M-%S')
subprocess.run(['python3','genSceneJSON.py', '-f', filename], check=True)
os.chdir('./SphairahedronFractalRenderer')
subprocess.run(['./bin/native/Release/SphairahedronRenderer',
                '-j', '../scene/'+ filename +'.json'], check=True)
os.chdir('../')
subprocess.run(['python3','tweet.py',
                '-i', './img/'+ filename +'.png',
                '-d', filename], check=True)
 
