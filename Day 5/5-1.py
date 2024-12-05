def main():
    with open("input5.txt", "r") as f:
        lines = f.readlines()
        rules = {}
        sum = 0
        for line in lines:
            #Check if the line has a "|"
            if "|" in line:
                #Split the line into 2 parts
                before, after = line.strip().split("|")
                rules.setdefault(before, []).append(after)
            elif len(line.strip()) > 1:
                valid = True
                numbers = line.strip().split(",")
                for i, numberToCheck in enumerate(numbers):
                    if numberToCheck in rules:
                        #if the number is in the rules, it must come before some other numbers
                        after_numbers = rules[numberToCheck]
                        for after_number in after_numbers:
                            if after_number in numbers:
                                #If the after_number is in the numbers, it must come after the numberToCheck
                                if numbers.index(after_number) < i:
                                    valid = False
                                    break
                if valid:
                    #add the middle number to the sum
                    sum += int(numbers[len(numbers) // 2])
        print(sum)



if __name__ == "__main__":
    main()