def main():
    with open("input2.txt", "r") as f:
        lines = f.readlines()
        sum = 0
        for line in lines:
            line = line.strip().split(" ")
            line = [int(x) for x in line]
            safe = False
            if isSafe(line):
                safe = True
            for i in range(len(line)):
                if safe or isSafe(line[:i] + line[i + 1:]):
                    safe = True
                    break
            if safe:
                sum += 1
            print(line, safe)
        print(sum)

def isSafe(line):
    if line[0] > line[1]:
        #Descending
        for i in range(len(line) - 1):
            if line[i] < line[i + 1]:
                return False
            if abs(line[i] - line[i + 1]) < 1 or abs(line[i] - line[i + 1]) > 3:
                return False
    elif line[0] < line[1]:
        #Ascending
        for i in range(len(line) - 1):
            if line[i] > line[i + 1]:
                return False
            if abs(line[i] - line[i + 1]) < 1 or abs(line[i] - line[i + 1]) > 3:
                return False
    else:
        return False
    return True

def isSafe2(line):
    if line[0] > line[1]:
        #Descending
        for i in range(len(line) - 1):
            if line[i] < line[i + 1]:
                return False
            if abs(line[i] - line[i + 1]) < 1 or abs(line[i] - line[i + 1]) > 3:
                return False
    elif line[0] < line[1]:
        #Ascending
        for i in range(len(line) - 1):
            if line[i] > line[i + 1]:
                return False
            if abs(line[i] - line[i + 1]) < 1 or abs(line[i] - line[i + 1]) > 3:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    main()