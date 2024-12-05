from collections import Counter

def main():
    with open("input1.txt", "r") as f:
        lines = f.readlines()
        line1, line2 = [], []
        for line in lines:
            line = line.strip().split("   ")
            line1.append(int(line[0]))
            line2.append(int(line[1]))
        line2 = Counter(line2)
        sum = 0
        for i in range(len(line1)):
            sum += line1[i] * line2[line1[i]]
        print(sum)

if __name__ == "__main__":
    main()