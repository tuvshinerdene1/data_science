def calculate_average(scores):
    sum = 0
    for x in scores:
        sum += x
    average = sum / len(scores)
    if average >= 90 :
        grade = 'A'
    elif 80 <= average and average < 90 :
        grade = 'B'
    elif 70 <= average and average <80:
        grade = 'C'
    elif 60 <= average and average < 70:
        grade = 'D'
    else:
        grade = 'F'

    print(f"average = {average}")
    print(f"letter grade : {grade}")


def main():
    scores = [85,92,78,90,88]
    calculate_average(scores)

if __name__ == "__main__":
    main()