import sys
import subprocess
import time
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
print("Welcome to Zefroin first time setup...")
time.sleep(2)
print("Please wait while we install some required packages...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pythonping'])
print("Installation 25% complete...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])
print("Installation 50% complete...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'tqdm'])
print("Installation 75% complete...")
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'update_check'])
print("Installation 100% complete...")
with open('zf.nzf', 'w') as f:
    f.write('1')
run("main.py")


