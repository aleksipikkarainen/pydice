import re
import random

#We can start the program by fancily using this one function.
def Init():
    InitPrinter()
    InitLogger()
    while True:
        s = parseInput()
        if s[1] == "quit":
            break
        printDice(s)
        
    print("Thanks and see you next time.")    
    
#Prints liibalaaba at the start so we can reach the required five functions.    
def InitPrinter():
    print("Welcome to pyDice! \n")
    print("For more detailed instructions please refer to the documentation.")
    
#Takes input from user and parses the required values from it using some Regex magic. If there's no value it gets replaced by an "x",
# so that the later part of the code can still iterate through if needed.
def parseInput():
    list = ["x"] * 4
    x = input("Enter your di(c)e roll.\n")
    r = re.search(r"^(\d+)",x)
    
    if r != None:
        list[0] = r.group()
        
    r2 = re.search(r"(?<=d)(\d+)",x)
    
    if r2 != None:
        list[1] = r2.group()
        
    r3 = re.search(r"\+|-(?=\d)",x)
    
    if r3 != None:
        list[2] = r3.group()
        
    r4 = re.search(r"(?<=\+|-)[\d]",x)
    
    if r4 != None:
        list[3] = r4.group()
        
    r5 = re.search(r"quit",x)
    
    if r5 != None:
        list[1] = r5.group()
        
    return list

#Prints the dice values depending on how many dice were rolled.
def printDice(lista):
    if lista[0] == "x":
        throwDice(lista)
    else:
        for x in range(int(lista[0])):
            throwDice(lista)
#Calculates the dice values which in turn get passed to printer.
def throwDice(lista):
    num2 = int(lista[1])   
    if lista[2] == "+":
        num4 = int(lista[3])
        function = (random.randint(1,num2)+num4)

    elif lista[2] == "-":
        num4 = int(lista[3])
        function = (random.randint(1,num2)-num4)

    else:
        function = (random.randint(1,num2))
    
    with open("log.txt", "a") as log:
        s = str(function)
        log.write(s+"\n")

    print(function)
    
def InitLogger():
    with open("log.txt", "w") as log:
        log.write("History of dice rolls:\n")
        
          
Init()