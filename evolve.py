import random
from string import ascii_lowercase
import keyword
#8/19/16
#8/11/16
class evolve:
    def __init__(self):
        print "loading evolve module..."
    def size(self, script):
        char = 0
        c = "a"
        f = open(script, 'r+')
        while(c != ''):
            c = f.read(1)
            char = char + 1
        char = char - 1
        f.close()
        return char
    #8/13/16
    def randkeyword(self, length):
        ret = []
        n = 0
        k = len(keyword.kwlist)
        if(length == 0):
            ret = ""
        while(n < length):
            y = random.randint(0,k)
            ret.append(keyword.kwlist[y])
            n = n + 1
        return ret
    #8/12/16
    def randbell(self):
        x = int(random.gauss(0,1))
        return x
    #8/11/16
    def randstring(self, length):
        ret = ""
        n = 0
        while(n < length):
            x = random.randint(0,92)
            if(x == 0):
                ret = ret + "a"
            if(x == 1):
                ret = ret + "A"
            if(x == 2):
                ret = ret + "b"
            if(x == 3):
                ret = ret + "B"
            if(x == 4):
                ret = ret + "c"
            if(x == 5):
                ret = ret + "C"
            if(x == 6):
                ret = ret + "d"
            if(x == 7):
                ret = ret + "D"
            if(x == 8):
                ret = ret + "e"
            if(x == 9):
                ret = ret + "E"
            if(x == 10):
                ret = ret + "f"
            if(x == 11):
                ret = ret + "F"
            if(x == 12):
                ret = ret + "g"
            if(x == 13):
                ret = ret + "G"
            if(x == 14):
                ret = ret + "h"
            if(x == 15):
                ret = ret + "H"
            if(x == 16):
                ret = ret + "i"
            if(x == 17):
                ret = ret + "I"
            if(x == 18):
                ret = ret + "j"
            if(x == 19):
                ret = ret + "J"
            if(x == 20):
                ret = ret + "k"
            if(x == 21):
                ret = ret + "K"
            if(x == 22):
                ret = ret + "l"
            if(x == 23):
                ret = ret + "L"
            if(x == 24):
                ret = ret + "m"
            if(x == 25):
                ret = ret + "M"
            if(x == 26):
                ret = ret + "n"
            if(x == 27):
               ret = ret + "N"
            if(x == 28):
                ret = ret + "o"
            if(x == 29):
                ret = ret + "O"
            if(x == 30):
                ret = ret + "p"
            if(x == 31):
                ret = ret + "P"
            if(x == 32):
                ret = ret + "q"
            if(x == 33):
                ret = ret + "Q"
            if(x == 34):
                ret = ret + "r"
            if(x == 35):
                ret = ret + "R"
            if(x == 36):
                ret = ret + "s"
            if(x == 37):
                ret = ret + "S"
            if(x == 38):
                ret = ret + "t"
            if(x == 39):
                ret = ret + "T"
            if(x == 40):
                ret = ret + "u"
            if(x == 41):
                ret = ret + "U"
            if(x == 42):
                ret = ret + "v"
            if(x == 43):
                ret = ret + "V"
            if(x == 44):
                ret = ret + "w"
            if(x == 45):
                ret = ret + "W"
            if(x == 46):
                ret = ret + "x"
            if(x == 47):
                ret = ret + "X"
            if(x == 48):
                ret = ret + "y"
            if(x == 49):
                ret = ret + "Y"
            if(x == 50):
                ret = ret + "z"
            if(x == 51):
               ret = ret + "Z"
            if(x == 52):
                ret = ret + "1"
            if(x == 53):
                ret = ret + "2"
            if(x == 54):
                ret = ret + "3"
            if(x == 55):
                ret = ret + "4"
            if(x == 56):
                ret = ret + "5"
            if(x == 57):
                ret = ret + "6"
            if(x == 58):
                ret = ret + "7"
            if(x == 59):
                ret = ret + "8"
            if(x == 60):
                ret = ret + "9"
            if(x == 61):
                ret = ret + "0"
            if(x == 62):
                ret = ret + "!"
            if(x == 63):
                ret = ret + "@"
            if(x == 64):
                ret = ret + "#"
            if(x == 65):
                ret = ret + "$"
            if(x == 66):
                ret = ret + "%"
            if(x == 67):
                ret = ret + "^"
            if(x == 68):
                ret = ret + "&"
            if(x == 69):
                ret = ret + "*"
            if(x == 70):
                ret = ret + "("
            if(x == 71):
                ret = ret + ")"
            if(x == 72):
                ret = ret + "-"
            if(x == 73):
                ret = ret + "_"
            if(x == 74):
                ret = ret + "="
            if(x == 75):
                ret = ret + "+"
            if(x == 76):
                ret = ret + ","
            if(x == 77):
                ret = ret + "<"
            if(x == 78):
                ret = ret + "."
            if(x == 79):
                ret = ret + ">"
            if(x == 80):
                ret = ret + ":"
            if(x == 81):
                ret = ret + ";"
            if(x == 82):
                ret = ret + "'"
            if(x == 83):
                ret = ret + '"'
            if(x == 84):
                ret = ret + "["
            if(x == 85):
                ret = ret + "]"
            if(x == 86):
                ret = ret + "{"
            if(x == 87):
                ret = ret + "}"
            if(x == 88):
                ret = ret + "|"
            if(x == 89):
                ret = ret + "?"
            if(x == 90):
                ret = ret + "/"
            if(x == 91):
                ret = ret + "~"
            if(x == 92):
                ret = ret + "`"
            n=n+1
        return ret
    #8/13/16
    def mutate(self, script, typ):
        f = open(script, 'r+')
        if(typ == "key"):
            a = 0
            b = int(random.gauss(1,1))
            mutations = 0
            while(a < b):
                address = random.randint(0, evolve.size(self, script))
                f.seek(address, 0)
                a = evolve.randbell(self)
                st = evolve.randkeyword(self, a)
                mutations = mutations + len(st)
                n = 0
                while(n < len(st)):
                    x = st[n]
                    f.write(x)
                    f.write(" ")
                    n = n + 1
                a = a + 1
            print mutations
        if(typ == "char"):
            a = 0
            b = int(random.gauss(1,1))
            mutations = 0
            while(a < b):
                address = random.randint(0, evolve.size(self, script))
                f.seek(address, 0)
                a = evolve.randbell(self)
                st = evolve.randstring(self, a)
                mutations = mutations + len(st)
                f.write(st)
            print mutations
        f.close()
