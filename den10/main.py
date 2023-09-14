hodnoty = open("hodnoty.txt").read().splitlines()

if __name__ == '__main__':
    tmp =[""]
    skore = 0

    for radek in hodnoty:
        for symbol in radek:
            if symbol == "(":
                tmp.append(symbol)
            elif symbol == "<":
                tmp.append(symbol)
            elif symbol == "{":
                tmp.append(symbol)
            elif symbol == "[":
                tmp.append(symbol)

            elif symbol == ">":
                if tmp.pop() == "<":
                    print("all good")
                else:
                    skore = skore + 25137
            elif symbol == ")":
                if tmp.pop() == "(":
                    print("all good")
                else:
                    skore = skore + 3
            elif symbol == "}":
                if tmp.pop() == "{":
                    print("all good")
                else:
                    skore = skore + 1197
            elif symbol == "]":
                if tmp.pop() == "[":
                    print("all good")
                else:
                    skore = skore + 57
    print(skore)

