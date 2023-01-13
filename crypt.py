
# encrypt
def encryptpass(password):

    encryptedpasse = []

    for i in password:
        encryptedpasse.append(i)

    encryptedpass = str(encryptedpasse)
    encryptedpass = encryptedpass.replace("'", "")
    encryptedpass = encryptedpass.replace("[", "")
    encryptedpass = encryptedpass.replace("]", "")
    encryptedpass = encryptedpass.replace(",", "")
    encryptedpass = encryptedpass.replace(" ", "")

    encryptedpass = encryptedpass.replace("1", "£")
    encryptedpass = encryptedpass.replace("2", "§")
    encryptedpass = encryptedpass.replace("3", "€")
    encryptedpass = encryptedpass.replace("4", "¥")
    encryptedpass = encryptedpass.replace("5", "æ")
    encryptedpass = encryptedpass.replace("6", "¶")
    encryptedpass = encryptedpass.replace("7", "•")
    encryptedpass = encryptedpass.replace("8", "±")
    encryptedpass = encryptedpass.replace("9", "°")
    encryptedpass = encryptedpass.replace("0", "©")
    encryptedpass = encryptedpass.replace("a", "1")
    encryptedpass = encryptedpass.replace("A", "2")
    encryptedpass = encryptedpass.replace("b", "3")
    encryptedpass = encryptedpass.replace("B", "4")
    encryptedpass = encryptedpass.replace("c", "5")
    encryptedpass = encryptedpass.replace("C", "6")
    encryptedpass = encryptedpass.replace("d", "7")
    encryptedpass = encryptedpass.replace("D", "8")
    encryptedpass = encryptedpass.replace("e", "9")
    encryptedpass = encryptedpass.replace("E", "!")
    encryptedpass = encryptedpass.replace("f", "@")
    encryptedpass = encryptedpass.replace("F", "#")
    encryptedpass = encryptedpass.replace("g", "$")
    encryptedpass = encryptedpass.replace("G", "%")
    encryptedpass = encryptedpass.replace("h", "^")
    encryptedpass = encryptedpass.replace("H", "&")
    encryptedpass = encryptedpass.replace("i", "*")
    encryptedpass = encryptedpass.replace("I", "(")
    encryptedpass = encryptedpass.replace("j", ")")
    encryptedpass = encryptedpass.replace("J", "-")
    encryptedpass = encryptedpass.replace("k", "_")
    encryptedpass = encryptedpass.replace("K", "=")
    encryptedpass = encryptedpass.replace("l", "+")
    encryptedpass = encryptedpass.replace("L", "[")
    encryptedpass = encryptedpass.replace("m", "]")
    encryptedpass = encryptedpass.replace("M", "{")
    encryptedpass = encryptedpass.replace("n", "}")
    encryptedpass = encryptedpass.replace("N", ",")
    encryptedpass = encryptedpass.replace("o", "<")
    encryptedpass = encryptedpass.replace("O", ".")
    encryptedpass = encryptedpass.replace("p", ">")
    encryptedpass = encryptedpass.replace("P", ":")
    encryptedpass = encryptedpass.replace("q", ";")
    encryptedpass = encryptedpass.replace("Q", "'")
    encryptedpass = encryptedpass.replace("r", "?")
    encryptedpass = encryptedpass.replace("R", "/")
    encryptedpass = encryptedpass.replace("s", "|")
    encryptedpass = encryptedpass.replace("S", "`")
    encryptedpass = encryptedpass.replace("t", "~")
    encryptedpass = encryptedpass.replace("T", "A")
    encryptedpass = encryptedpass.replace("u", "B")
    encryptedpass = encryptedpass.replace("U", "C")
    encryptedpass = encryptedpass.replace("v", "D")
    encryptedpass = encryptedpass.replace("V", "E")
    encryptedpass = encryptedpass.replace("w", "F")
    encryptedpass = encryptedpass.replace("W", "G")
    encryptedpass = encryptedpass.replace("x", "H")
    encryptedpass = encryptedpass.replace("X", "I")
    encryptedpass = encryptedpass.replace("y", "J")
    encryptedpass = encryptedpass.replace("Y", "K")
    encryptedpass = encryptedpass.replace("z", "L")
    encryptedpass = encryptedpass.replace("Z", "M")
    parv = encryptedpass

    return parv

# decrypt
def decryptpass(usr ,password):
 cryp = encryptpass(password)
 try:
   a = open(usr + '.zc', 'r')
   ab = a.read()
   a.close()
   if ab == cryp:
     return True
   else:
     return False
 except:
   print("User doesn't exist!")
   pass
 
