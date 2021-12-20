import re


def parseInput():
    list = []
    x = input("Enter your dice roll.\n")
    r = re.findall(r"^(\d+)",x)
    list.append(r)
    print(r)
    r2 = re.findall(r"d(\d+)",x)
    list.append(r2)
    print(r2)
    r3 = re.findall(r"\+|-(?=\d)",x)
    list.append(r3)
    print(r3)
    r4 = re.findall(r"(?<=\+|-)[\d]",x)
    list.append(r4)
    print(r4)
    r5 = re.findall(r"quit",x)
    list.append(r5)
    print(r5)
    return list

while True:
    s = parseInput()
    if 'quit' in s[4]:
        break
    for x in s:
        print(x)
print("looppi ohi")

//Tee vaan yks metodi nii sit hoidan loput tosta ja yritän puhuu meidät irti
tosta miks meillä ei oo noi kaikki vaatimukset täytettyin :--D//