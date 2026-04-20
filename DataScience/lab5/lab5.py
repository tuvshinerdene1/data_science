import pandas as pd


def calculate_letter_grade(grade:float):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else :
        return 'F'


def main():
    data = pd.read_csv('student_data.csv')
    # daalgawar 1 
    print(data.head())

    # daalgawar 2 
    print("dundaj"+str(data['Оноо'].mean()))
    print("median"+str(data['Оноо'].median()))
    print("minimum"+str(data['Оноо'].min()))
    print("maximum"+str(data['Оноо'].max()))
    print("standard hazailt"+str(data['Оноо'].std()))

    # daalgawar 3
    if 'letter_grade' not in data:
        data['letter_grade'] = data['Оноо'].apply(calculate_letter_grade)
        data.to_csv('new_data.csv', index=False)

    # daalgawar 4 
    if 'above_average' not in data:
        data['above_average'] =  data['Оноо'] > data['Оноо'].mean()
        data.to_csv('excercise4.csv', index=False)

    # daalgawar 5
    if 'normalized_grade' not in data:
        data['normalized_grade'] =  (data['Оноо'] - data['Оноо'].min())/(data['Оноо'].max() - data['Оноо'].min())
        data.to_csv('excercise5.csv', index=False)








if __name__ == "__main__":
    main()