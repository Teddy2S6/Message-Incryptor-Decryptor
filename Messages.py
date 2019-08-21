def encrypt(code):

    final = []
    anws = ""

    for elem in code:

        final.append(elem)

    for elem2 in final:

        if elem2 == "a":
            anws += "!"

        if elem2 == "b":
            anws += "@"

        if elem2 == "c":
            anws += "$"

        if elem2 == "d":
            anws += "&"

        if elem2 == "e":
            anws += "#"

        if elem2 == "f":
            anws += "*"

        if elem2 == "g":
            anws += "%"

        if elem2 == "h":
            anws += "?"

        if elem2 == "i":
            anws += "+"

        if elem2 == "j":
            anws += "-"

        if elem2 == "k":
            anws += "="

        if elem2 == "m":
            anws += "/"

        if elem2 == "n":
            anws += ">"

        if elem2 == "l":
            anws += "<"

        if elem2 == "o":
            anws += ":"

        if elem2 == "p":
            anws += "^"

        if elem2 == "q":
            anws += "~"

        if elem2 == "r":
            anws += ";"

        if elem2 == "s":
            anws += ","

        if elem2 == "t":
            anws += "{"

        if elem2 == "u":
            anws += "|"

        if elem2 == "v":
            anws += "["

        if elem2 == "w":
            anws += "]"

        if elem2 == "x":
            anws += "("

        if elem2 == "y":
            anws += ")"

        if elem2 == "z":
            anws += "}"

        if elem2 == " ":
            anws += "."

        if elem2 == ",":
            anws += "`"

        if elem2 == ".":
            anws += "_"

    print(anws)

def decrypt(code):

    final = []
    anws = ""

    for elem in code:

        final.append(elem)

    for elem2 in final:

        if elem2 == "!":
            anws += "a"

        if elem2 == "@":
            anws += "b"

        if elem2 == "$":
            anws += "c"

        if elem2 == "&":
            anws += "d"

        if elem2 == "#":
            anws += "e"

        if elem2 == "*":
            anws += "f"

        if elem2 == "%":
            anws += "g"

        if elem2 == "?":
            anws += "h"

        if elem2 == "+":
            anws += "i"

        if elem2 == "-":
            anws += "j"

        if elem2 == "=":
            anws += "k"

        if elem2 == "/":
            anws += "m"

        if elem2 == ">":
            anws += "n"

        if elem2 == "<":
            anws += "l"

        if elem2 == ":":
            anws += "o"

        if elem2 == "^":
            anws += "p"

        if elem2 == "~":
            anws += "q"

        if elem2 == ";":
            anws += "r"

        if elem2 == ",":
            anws += "s"

        if elem2 == "{":
            anws += "t"

        if elem2 == "|":
            anws += "u"

        if elem2 == "[":
            anws += "v"

        if elem2 == "]":
            anws += "w"

        if elem2 == "(":
            anws += "x"

        if elem2 == ")":
            anws += "y"

        if elem2 == "}":
            anws += "z"

        if elem2 == ".":
            anws += " "

        if elem2 == "`":
            anws += ","

        if elem2 == ".":
            anws += "_"

    print(anws)
