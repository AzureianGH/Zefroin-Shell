
try:
  import re
  import time
  import os
  import socket
  import subprocess
  import sys
  import requests
  from update_check import update
  from update_check import isUpToDate
  import urllib
  from subprocess import call
  from urllib import request
  from tqdm import tqdm
  from pythonping import ping
  import logging
except Exception as e:
  print(e)
  print("Did you install the requirements.txt?")
  time.sleep(5)
  quit()
error95 = "Unable to reach update service! 95"
logging.basicConfig(filename="ZEF.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 

logger = logging.getLogger()
 

logger.setLevel(logging.DEBUG)
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

seconds = 3

print("Checking on updates for Zefroin...")
for i in tqdm(range(seconds)):
      time.sleep(0.1)
if isUpToDate(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/ZefroinShell.py") == False:
    update(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/ZefroinShell.py")
    print("Updates Required!")
    run("ZefRest.py")
    quit()
else:
  print("No Updates! Or " + error95)
seconds = 2
print("Mounting Zefroin...")
for i in tqdm(range(seconds)):
    time.sleep(0.1)
with open(r'zefdump.txt', 'w') as fp:
    fp.write('Dump file created.')
    pass
print("Mounted.")
seconds = 30
print("Starting Zefroin...")
for i in tqdm(range(seconds)):
    time.sleep(0.01)
print("\033[1;33;40m Zefroin Shell 2.4 COPYRIGHT OF AZUREIAN")
print("\033[1;33;40m Powered by Python, tqdm, pythonping, and more!")
def error109():
  print("\033[1;31;40m No Statement provided! 109")
  logger.error("No Statement provided! 109")
def error1():
  print("\033[1;31;40m Unknown Statement! 1")
  logger.error("Unknown Statement! 1")
error56a = 0
def error32():
  print("\033[1;31;40m Unable to parse negative value! 32")
  logger.error("Unable to parse negative value! 32")
def error18():
  print("\033[1;31;40m Value input can't be negative! 18")
  logger.error("Value input can't be negative! 18")
def error0():
  print("\033[1;31;40m No Feature! 0") 
  logger.error("No Feature! 0")
def warning1():
  print("\033[1;31;40m Warning! This feature is experimental and may result in loops or possible breaks from the code!")
  logger.warning("Warning! This feature is experimental and may result in loops or possible breaks from the code!")
def errorunk():
  print("\033[1;31;40m Unknown error has occured! UNK")
  logger.critical("Unknown error has occured! UNK")
def error45():
  print("\033[1;31;40m No sign entered! 45")
  logger.error("No sign entered! 45")
iftrue = 1
def error67():
  print("\033[1;31;40m Value can not be letters! 67")
  logger.error("Value can not be letters! 67")
while True:
    while True:
        zinput = input("\033[1;32;40mZef >> ")
        if zinput == "help":
            print("help - Opens Help\nprint - Prints a line\nloop - Loops a word for a certain amount\nmath - Simple Mathmatics\nkcal - Used for the trophic levels.\nend - Closes the terminal.\nupdate - Updates Zefroin\ngithub - Official github for Zefroin\nDownl - Downloads files from links\nzep install - Installs a package\nzf - Run selected package.\nclear - Clears console")
        elif zinput == "print":
            prnt = input("Print >> ")
            print(prnt)
        elif zinput == "":
            print(error109)
        
        elif zinput == "loop":
            intimes = 0
            loop = input("Loop >> ")
            times = input("How many times? >> ")
            if times.isnumeric() == False:
                print(error67)
                break
                
            else: 
                intimes = int(times)
                if intimes > 1000:
                    error56a = intimes - 1000
                    error56b = str(error56a)
                    error56 = "Charcter Limit Exceeded by " + error56b
                    print(error56 + "! 56")
                    intimes = 0
                    addtimes = 0
                elif intimes < 0:
                    print(error32)
                    intimes = 0
                    addtimes = 0
                elif intimes == -0:
                    print(error18)
                    intimes = 0
                    addtimes = 0
                
                addtimes = 0
            
                while addtimes < intimes:
                    addtimes = addtimes + 1
                    print(loop)
        elif zinput == "math":
            print("What operation?\n+\n-\n*\n/")
            mathop = input("Math >> ")
            mathoper = 0
            if mathop == "+":
                mathoper = 1
                iftrue = 1
            elif mathop == "-":
                mathoper = 2
                iftrue = 1
            elif mathop == "*":
                mathoper = 3
                iftrue = 1
            elif mathop == "/":
                mathoper = 4
                iftrue = 1
            else:
                mathoper = 5
            if mathoper == 0:
                print(errorunk)
                iftrue = 0
            elif mathoper == 5:
                iftrue = 0
                print(error45)
            if iftrue == 1:
                print("Number 1: ")
                math1 = input("Math >> ")
                print("Number 2: ")
                math2 = input("Math >> ")
                if math1.isnumeric() == False:
                    print(error67)
                    break
                else:
                    if math2.isnumeric() == False:
                        print(error67)
                        break
                    else:
                        math1i = int(math1)
                        math2i = int(math2)
                        mathp = math1i + math2i
                        mathm = math1i - math2i
                        mathmt = math1i * math2i
                        mathd = math1i / math2i
                        mathper = math1i % math2i
                        if mathoper == 1:
                            print(mathp)
                            if mathp == 38:
                                mathazure = str(mathp)
                                print(mathazure + " Is Azureian's favorite number!")
                            # +
                        elif mathoper == 2:
                            print(mathm)
                            # -
                        elif mathoper == 3:
                            print(mathmt)
                            if math1i == math2i:
                                math1m = str(math1i)
                                math2m = str(math2i)
                                mathmt1 = str(mathmt)
                                print(mathmt1 + " is the square of " + math1m + " and " + math2m)
                            # *
                        elif mathoper == 4:
                            print(mathd)
                            if mathd == math2i:
                                mathds = str(mathd)
                                math1s = str(math1i)
                                print(mathds + " is the square root of " + math1s)
                            # /
                        
                        else:
                            print(errorunk)
        elif zinput == "end":
            quit()
        elif zinput == "msdos":
              print("  __  __  _____       _____   ____   _____  ")
              print("  |  \/  |/ ____|     |  __ \ / __ \ / ____|")
              print("  | \  / | (___ ______| |  | | |  | | (___  ")
              print("  | |\/| |\___ \______| |  | | |  | |\___ \ ")
              print("  | |  | |____) |     | |__| | |__| |____) |")
              print("  |_|  |_|_____/      |_____/ \____/|_____/ ")
              print("                                            ")
              input("C:\>")
              print("Bad command or not swag enough")
        elif zinput == "kcal":
          print("How many Kcals?")
          kcalinput = input("Kcal >> ")
          if kcalinput.isnumeric() == False:
            print(error67)
            break
          else:
            kcal = float(kcalinput)
            kcal2 = kcal * .10
            kcal3 = kcal2 * .10
            kcal4 = kcal3 * .10
            kcal5 = kcal4 * .10
  
  
            kcal1s = str(kcal2)
            kcal2s = str(kcal3)
            kcal3s = str(kcal4)
            kcal4s = str(kcal5)
  
  
            
            print(kcalinput + " - Producers\n" + kcal1s + " - Primary Consumers\n" + kcal2s + " - Secondary Consumers\n" + kcal3s + " - Tertiary Consumers\n" + kcal4s + " - Apex Predators")
            print("Don't we love biology?!")
        elif zinput == "update":
             updtelog = 0
             seconds = 3
             print("Checking on updates for Zefroin...")
             for i in tqdm(range(seconds)):
                 time.sleep(0.1)
             
             if isUpToDate(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/ZefroinShell.py") == False:
                update(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/ZefroinShell.py")
                print("Updates Required!")
                run("ZefRest.py")
                quit()
                
                
             elif isUpToDate(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/ZefroinShell.py") == True:
                print("All caught up!")
             else:
                print("Unable to reach update service! 95")
        elif zinput == "github":
          print("https://github.com/AzureianGH/Zefroin-Shell")
         
        elif zinput == "downl":
          print("URL?")
          urlinp = input("Downl >> ")
          print("Name with file extension:")
          urldown = input("Downl >> ")
          URL = urlinp
          response = request.urlretrieve(URL, urldown)
          
        elif zinput == "zep install":
            print("Link to Raw ZF file")
            URL = input("Zep >> ")
            print("Name of file? (Without extension)")
            URLname = input("Zep >> ")
            URLzef = URLname + ".zf"
            response = request.urlretrieve(URL, URLzef)
            

        elif zinput == "zf":
            print("Name of Package? (Without extension)")
            nop1 = input("Runzf >> ")
            nop = str(nop1)
            exec(open(nop + '.zf').read())
        elif zinput == "clear":
            print('\x1b[2J')
        
        
        else:
            print(error1)

