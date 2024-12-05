def main():
    with open("input3.txt", "r") as f:
        lines = f.readlines()
        line = ""
        sum = 0
        do = True
        for l in lines:
            line += l
        for i, c in enumerate(line):
            #check for a do() or don't() command
            if c == 'd':
                lineToCheck = line[i:i+7]
                print(lineToCheck)
                if lineToCheck[:4] == "do()":
                    do = True
                elif lineToCheck[:7] == "don't()":
                    do = False
            if c == 'm':
                lineToCheck = line[i:i+12]
                if do and lineToCheck[0:4] == "mul(":
                    print(lineToCheck)
                    #found a possible mul command (x,y) (xxx,yyy)
                    #find a closing parenthesis in the next 4-8 characters
                    for j, c2 in enumerate(lineToCheck[4:]):
                        if c2 == ')':
                            #found a closing parenthesis
                            mulCommand = lineToCheck[4:j+4]
                            #check if there is a comma
                            if "," in mulCommand:
                                x, y = mulCommand.split(",")
                                #check if x and y are numbers
                                if x.isdigit() and y.isdigit():
                                    sum += int(x) * int(y)
                            break
        print(sum)
if __name__ == "__main__":
    main()