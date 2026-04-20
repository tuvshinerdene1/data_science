def monitorTemp(temps):
    ltemps = temps[:]
    print(f"max temp = {max(ltemps)}")
    print(f"min temp = {min(ltemps)}")
    print(f"avg temp = {sum(ltemps)/len(ltemps):.1f}")
    print(f"temps higher than avg temp = {len([x for x in ltemps if x > sum(ltemps)/len(ltemps)])}")



def main():
    temps = [72, 68, 75, 70, 73, 69, 71]
    monitorTemp(temps)

if __name__ == "__main__":
    main()