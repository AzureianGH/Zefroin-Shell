import sys
import subprocess
import time

print("Checking packages...")
try:
  from pythonping import ping
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pythonping'])
  print("pythonping not found... Filling requirement.")
try:
  import requests
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])
  print("requests not found... Filling requirement.")
try:
  from tqdm import tqdm
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'tqdm'])
  print("tqdm... Filling requirement.")
try:
  from update_check import update
  from update_check import isUpToDate
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'update_check'])
  print("update_check not found... Filling requirement.")
try:
  import matplotlib.pyplot as plt
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'matplotlib'])
  print("matplotlib not found... Filling requirement.")
try:
  import numpy as np
except:
  subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'numpy'])
  print("numpy not found... Filling requirement.")
print("All packages found.")
def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())
try:
  import os  
  import requests
  import matplotlib.pyplot as plt
  import numpy as np
  from update_check import update
  from update_check import isUpToDate
  import urllib
  from urllib import request
  from tqdm import tqdm
  from pythonping import ping
  import logging
  import glob
  import os.path
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

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    
    ectp = traceback.print_exception(exc_type, exc_value, tb)
    print("Fatal Error: -1")
    run("ZefRest.py")
    logger.critical(ectp)

sys.excepthook = show_exception_and_exit
seconds = 3
betatest = False
if betatest == False:
  print("Checking on updates for Zefroin...")
  for i in tqdm(range(seconds)):
        time.sleep(0.1)
  if isUpToDate(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/main.py") == False:
      update(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/main.py")
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
print("\033[1;33;40m Zefroin Shell 4.1 COPYRIGHT OF AZUREIAN")
print("\033[1;33;40m Powered by Python!")
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
def error26():
  print("\033[1;31;40m Input is too large! 26")
  logger.error("Input is too large! 26")
def error0():
  print("\033[1;31;40m No Feature! 0") 
  logger.error("No Feature! 0")
def warning1():
  print("\033[1;31;40m Warning! This feature is experimental and may result in loops or possible breaks from the code! w1")
  logger.warning("Warning! This feature is experimental and may result in loops or possible breaks from the code! w1")
def errorunk():
  print("\033[1;31;40m Unknown error has occured! UNK")
  logger.critical("Unknown error has occured! UNK")
def error45():
  print("\033[1;31;40m No sign entered! 45")
  logger.error("No sign entered! 45")
iftrue = 1
def error67():
  print("\033[1;31;40m Value can not be Alphic! 67")
  logger.error("Value can not be Alphic! 67")
def error88():
  print("\033[1;31;40m Function Overload! Cannot convert string to Char! 88")
  logger.error("Function Overload! Cannot convert string to Char! 88")

def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = 'center')
def valuelabel(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i], ha = 'center',
                 bbox = dict(facecolor = 'cyan', alpha =0.8))
def deferror(errorcode):
  if errorcode == "109":
    error109()
  elif errorcode == "1":
    error1()
  elif errorcode == "32":
    error32()
  elif errorcode == "18":
    error18()
  elif errorcode == "26":
    error26()
  elif errorcode == "0":
    error0()
  elif errorcode == "w1":
    warning1()
  elif errorcode == "unk":
    errorunk()
  elif errorcode == "45":
    error45()
  elif errorcode == "67":
    error67()
  elif errorcode == "88":
    error88()
  else:
    print("No error code found!")
defaultnm = "~/Zef"
osname = sys.platform
ostype = ""
if osname == "linux":
  ostype = "linux"
elif osname == "Windows":
  ostype = "Windows"
elif osname == "Mac OS X":
  ostype = "Mac"
else:
  ostype = "Other"
zfname = defaultnm
while True:
    while True:
        
        zinput = input("\033[1;32;40m"+zfname+" >> ")
        if zinput == "help":
            print("help - Opens Help\nprint - Prints a line\nloop - Loops a word for a certain amount\nmath - Simple Mathmatics\nkcal - Used for the trophic levels.\nend - Closes the terminal.\nupdate - Updates Zefroin\ngithub - Official github for Zefroin\nDownl - Downloads files from links\nzep install - Installs a package\nzf - Run selected package\nclear - Clears console\nsleep - Sleeps a certain amount of time\nerlist - Lists error\ncrash - What do you think it does?\nscatter - Plots a scatter plot\nlinegraph - Plots a line graph\nbargraph - Plots a bar graph\nsortalpha - Sorts alpha text files\nzimmer - Translate into Zimmerman note\ndir - Lists files in an area\ncd - Calls directory\nmkdir - Makes directory\nrndir - Renames directory\nrmdir - Removes directory\nwlkdir - Walks along a directory and sub-directory\n")
        elif zinput == "print":
            prnt = input("Print >> ")
            print(prnt)
        elif zinput == "":
            error109()
        
        elif zinput == "loop":
            intimes = 0
            loop = input("Loop >> ")
            times = input("How many times? >> ")
            if times.isnumeric() == False:
                error67()
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
                    error32()
                    intimes = 0
                    addtimes = 0
                elif intimes == -0:
                    error18()
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
                errorunk()
                iftrue = 0
            elif mathoper == 5:
                iftrue = 0
                error45()
            if iftrue == 1:
                print("Number 1: ")
                math1 = input("Math >> ")
                print("Number 2: ")
                math2 = input("Math >> ")
                if math1.isnumeric() == False:
                    error67()
                    break
                else:
                    if math2.isnumeric() == False:
                        error67()
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
                            errorunk()
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
            error67()
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
             
             if isUpToDate(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/main.py") == False:
                update(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/main.py")
                print("Updates Required!")
                run("ZefRest.py")
                quit()
                
                
             elif isUpToDate(__file__, "https://raw.githubusercontent.com/AzureianGH/Zefroin-Shell/main/main.py") == True:
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
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
          
        elif zinput == "sleep":
          print("Sleep (seconds)")
          slepr = input("Sleep >> ")
          if slepr.isnumeric():
            slepa = int(slepr)
            if slepa <= 9223372036.854775:
              print("Sleeping for " + slepr + " seconds.")
              time.sleep(slepa)
              print("Awaking...")
            else:
              error26()
          else:
            error67()
        elif zinput == "erlist":
          print("Error code?")
          ercode = input("Er >> ")
          deferror(ercode)
        elif zinput == "crash":
          print("Confirm? Y/N")
          critconf = input("Crash >> ")
          if critconf == "Y" or "y" or "yes":
            logger.critical("User Confirmed Crash || Zefroin Dieded")
            quit()
          else:
            break
        elif zinput == "scatter":
          xint = input("X-Axis Number\nScatter >> ")
          
          breaker = False
          yp = ""
          xp = ""
          x=[]
          y=[]
          xint = int(xint)
          x.append(xint)
          while True:
            xp = str(x)
           
            xam = input("Add another X?\nType a Number, or say 'No'.\n" + xp + "\nScatter >> ")
            if xam.isalpha() == False:
              xam = int(xam)
              x.append(xam)
            else:
              breaker = True
              break
            if breaker:
              break
          breaker = False
          yint = input("Y-Axis Number\nScatter >> ")
          yint = int(yint)
          y.append(yint)
          while True:
            yp = str(y)
            yam = input("Add another Y?\nType a Number, or say 'No'.\n" + yp + "\nScatter >> ")
            if yam.isalpha() == False:
              yam = int(yam)
              y.append(yam)
            else:
              breaker = True
              break
            if breaker:
              break
              
          
          xaxlab = input("X-Axis Name\nScatter >> ")
          yaxlab = input("Y-Axis Name\nScatter >> ")
          plottitle = input("Title\nScatter >> ")
          plt.plot(x, y, 'ro')
          plt.xlabel(xaxlab)
          plt.ylabel(yaxlab)
          plt.title(plottitle)
          xs = str(x)
          ys = str(y)
          print("X = " + xs + "\n Y = " + ys)
          plt.show()
          break
        elif zinput == "linegraph":
          xint = input("X-Axis Number\nLine >> ")
          
          breaker = False
          yp = ""
          xp = ""
          x=[]
          y=[]
          xint = int(xint)
          x.append(xint)
          while True:
            xp = str(x)
           
            xam = input("Add another X?\nType a Number, or say 'No'.\n" + xp + "\nLine >> ")
            if xam.isalpha() == False:
              xam = int(xam)
              x.append(xam)
            else:
              breaker = True
              break
            if breaker:
              break
          breaker = False
          yint = input("Y-Axis Number\nLine >> ")
          yint = int(yint)
          y.append(yint)
          while True:
            yp = str(y)
            yam = input("Add another Y?\nType a Number, or say 'No'.\n" + yp + "\nLine >> ")
            if yam.isalpha() == False:
              yam = int(yam)
              y.append(yam)
            else:
              breaker = True
              break
            if breaker:
              break
              
          
          xaxlab = input("X-Axis Name\nLine >> ")
          yaxlab = input("Y-Axis Name\nLine >> ")
          plottitle = input("Title\nLine >> ")
          plt.plot(x, y)
          plt.xlabel(xaxlab)
          plt.ylabel(yaxlab)
          plt.title(plottitle)
          xs = str(x)
          ys = str(y)
          print("X = " + xs + "\n Y = " + ys)
          plt.show()
          break
        elif zinput == "bargraph":
          xint = input("X-Axis Data\nBar >> ")
          
          breaker = False
          yp = ""
          xp = ""
          x=[]
          y=[]
          
          x.append(xint)
          while True:
            xp = str(x)
           
            xam = input("Add another X?\nType data, or say '.end'.\n" + xp + "\nBar >> ")
            if xam == ".end":
              breaker = True
              break
            if breaker: break
            x.append(xam)  
          breaker = False
          yint = input("Y-Axis Number\nBar >> ")
          yint = int(yint)
          y.append(yint)
          while True:
            yp = str(y)
            yam = input("Add another Y?\nType a Number, or say 'No'.\n" + yp + "\nBar >> ")
            if yam.isalpha() == False:
              yam = int(yam)
              y.append(yam)
            else:
              breaker = True
              break
            if breaker:
              break
              
          
          xaxlab = input("X-Axis Name\nBar >> ")
          yaxlab = input("Y-Axis Name\nBar >> ")
          plottitle = input("Title\nBar >> ")
          
          
          
          ys = str(y)
          xs = str(x)
          plt.figure(figsize = (len(x), len(y)))
          plt.bar(x, y, color= 'orange')
      

          valuelabel(x, y)       
     
          # Define labels
          plt.xlabel(xaxlab)
          plt.ylabel(yaxlab)
          plt.title(plottitle)
    # Display plot
          
          print("X = " + xs + "\n Y = " + ys)
          plt.show()
          break
        elif zinput == "sortalpha":
          
          dirl = input("File location? (With Extension)\nSort >> ")

          FileName = (dirl)
          data=open(FileName).readlines()
          data.sort()
          for i in range(len(data)):
              print(data[i])
        elif zinput == "zimmer":
          zim = []
          while True:
            zimp = input("Add letter or type '.end'")
            if zimp == ".end":
                break
            if zimp == "a" or zim == "A":
              zim.append("DG")
            elif zimp == "b" or zim == "B":
              zim.append("AA")
            elif zimp == "c" or zim == "C":
              zim.append("DX")
            elif zimp == "d" or zim == "D":
              zim.append("FD")
            elif zimp == "e" or zim == "E":
              zim.append("AF")
            elif zimp == "f" or zim == "F":
              zim.append("FG")
            elif zimp == "g" or zim == "G":
              zim.append("FX")
            elif zimp == "h" or zim == "H":
              zim.append("GD")
            elif zimp == "i" or zim == "I":
              zim.append("DV")
            elif zimp == "j" or zim == "J":
              zim.append("GG")
            elif zimp == "k" or zim == "K":
              zim.append("GX")
            elif zimp == "l" or zim == "L":
              zim.append("AX")
            elif zimp == "m" or zim == "M":
              zim.append("VA")
            elif zimp == "n" or zim == "N":
              zim.append("DF")
            elif zimp == "o" or zim == "O":
              zim.append("VD")
            elif zimp == "p" or zim == "P":
              zim.append("VF")
            elif zimp == "q" or zim == "Q":
              zim.append("VG")
            elif zimp == "r" or zim == "R":
              zim.append("AV")
            elif zimp == "s" or zim == "S":
              zim.append("VV")
            elif zimp == "t" or zim == "T":
              zim.append("VX")
            elif zimp == "u" or zim == "U":
              zim.append("XA")
            elif zimp == "v" or zim == "V":
              zim.append("XD")
            elif zimp == "w" or zim == "W":
              zim.append("XF")
            elif zimp == "x" or zim == "X":
              zim.append("XG")
            elif zimp == "y" or zim == "Y":
              zim.append("XV")
            elif zimp == "z" or zim == "Z":
              zim.append("XX")
            elif zimp == "1":
              zim.append("DA")
            elif zimp == "2":
              zim.append("AD")
            elif zimp == "3":
              zim.append("FA")
            elif zimp == "4":
              zim.append("FF")
            elif zimp == "5":
              zim.append("AG")
            elif zimp == "6":
              zim.append("FV")
            elif zimp == "7":
              zim.append("GA")
            elif zimp == "8":
              zim.append("GF")
            elif zimp == "9":
              zim.append("DD")
            elif zimp == "0":
              zim.append("GV")
            else:
              error88()
            print(zim)
        elif zinput == "dir":
          der = os.listdir()
          print(der)
        elif zinput == "cd":
          der = input("Location? Or press return\nCd >> ")
          if der == "" or der == " ":
            break
          elif der == "^":
            parent_dir = os.path.split(os.getcwd())[0]
            der = parent_dir
          os.chdir(der)
          zfname = der
        elif zinput == "mkdir":
          der = input("Name? Or press return\nMk >> ")
          os.mkdir(der)
          print("Dir '"+der+"' Created.")
        elif zinput == "rndir":
          nam1 = input("Dir name? Or press return\nRn >> ")
          if nam1 == "" or nam1 == " ":
            break
          nam2 = input("New name?")
          os.rename(nam1,nam2)
          print("'"+nam1+"' Renamed to '"+nam2+"'")
        elif zinput == "rmdir":
          import shutil
          nam1 = input("Dir name? Or press return\nRm >> ")
          if nam1 == "" or nam1 == " ":
            break
          shutil.rmtree(nam1)
          print("Deleted '"+nam1+"'")
        elif zinput == "wlkdir":
          nam1 = input("Dir name? Or press return\nWlk >> ")
          if nam1 == "" or nam1 == " ":
            break
          for roots,dirs,files in os.walk(nam1):
                print(roots,len(dirs),len(files))
        elif zinput == "restart":
            run("ZefRest.py")
            quit()
        else:
            error1()

