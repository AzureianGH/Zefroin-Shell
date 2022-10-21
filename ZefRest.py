from tqdm import tqdm
import time
from subprocess import Popen

print("Restarting...")
seconds = 12
for i in tqdm(range(seconds)):
    time.sleep(0.1)
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
run("ZefroinShell.py")
quit()
