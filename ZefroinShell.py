print("Zefroin Shell 1.0 COPYRIGHT OF AZUREIAN")
error109 = "No Statement provided! 109"
error1 = "Unknown Statement! 1"
error56a = 0
error32 = "Unable to parse negative value! 32"
error18 = "Value input can't be negative! 18"
error0 = "No Feature! 0"
warning1 = "Warning! This feature is experimental and may result in loops or possible breaks from the code!"
errorunk = "Unknown error has occured! UNK"
error45 = "No sign entered! 45"
iftrue = 1
while True:
    zinput = input("Zef >> ")
    if zinput == "help":
        print("help - Opens Help
print - Prints a line
loop - Loops a word for a certain amount
math - Simple Mathmatics")
    elif zinput == "print":
        prnt = input("Print >> ")
        print(prnt)
    elif zinput == "":
        print(error109)
    
    elif zinput == "loop":
        intimes = 0
        loop = input("Loop >> ")
        times = input("How many times? >> ")
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
        print(error0)
        print(warning1)
        print("What operation?
+
-
*
/")
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
            math1i = int(math1)
            math2i = int(math2)
            mathp = math1i + math2i
            mathm = math1i - math2i
            mathmt = math1i * math2i
            mathd = math1i / math2i
            mathper = math1i % math2i
            if mathoper == 1:
                print(mathp)
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
    else:
        print(error1)