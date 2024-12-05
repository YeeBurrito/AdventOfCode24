def main():
    with open("input1.txt", "r") as f:
        lines = f.readlines()
        line1, line2 = [], []
        for line in lines:
            line = line.strip().split("   ")
            line1.append(int(line[0]))
            line2.append(int(line[1]))
        line1, line2 = sorted(line1), sorted(line2)
        sum = 0
        for i in range(len(line1)):
            sum += abs(line1[i] - line2[i])
        print(sum)

if __name__ == "__main__":
    main()