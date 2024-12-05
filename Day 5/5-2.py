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
                numbers = line.strip().split(",")
                numbers = reorderNumbers(rules, numbers)
                sum += int(numbers[len(numbers) // 2])
        print(sum)

def reorderNumbers(rules, numbers):
    #If a number is out of order, reorder it
    #Only reorder the numbers that are out of order, not the entire list
    solution = [numbers[0]]
    for n in numbers[1:]:
        #check if a number n has to come before another number that is already in the solution
        #if it does, insert it before the number
        added = False
        if n in rules:
            for r in rules[n]:
                if r in solution:
                    added = True
                    solution.insert(solution.index(r), n)
                    break
            if not added:
                solution.append(n)
        else:
            solution.append(n)
    print(solution)
    return solution

if __name__ == "__main__":
    main()

    #97 13 75 29 47
    #97 75 47 29 13
    #75 97 47 61 53
    #97 75 47 61 53