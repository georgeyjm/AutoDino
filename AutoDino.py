from PIL import Image
import subprocess
import os
import time
import threading

class jump(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        subprocess.call('osascript jump.scpt', shell=True)

class capture(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            try:
                img = Image.open(imageFile)
            except:
                continue
            if sum(img.load()[1,1][:3]) < 260:
                thread = jump()
                thread.start()

os.chdir(os.path.dirname(os.path.realpath(__file__)))

subprocess.call('osascript start.scpt', shell=True)

imageFile = os.path.expanduser('~/Desktop/autodino.png')

time.sleep(2)

runThread = capture()
runThread.start()
subprocess.call('osascript run.scpt', shell=True)
