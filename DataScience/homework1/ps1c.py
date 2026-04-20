def calc_saving(months:int, semi_annual_raise:float, r:float, start_salary:int,portion_saved:float):
    current_savings = 0
    months_spent = 0

    while months_spent < months:
        if months_spent%6==0 and months_spent > 0:
            start_salary += start_salary * semi_annual_raise
        current_savings += current_savings*r/12 + start_salary/12*portion_saved
        months_spent += 1
    return current_savings


def main():
    semi_annual_raise = 0.07
    r = 0.04
    portion_down_payment = 0.25
    total_cost = 1000000
    months_remaining = 36

    annual_salary = int(input("Jiliin tsalin oruulna uu: "))

    low = 0
    high = 10000
    steps = 0
    found = False

    while low <= high:
        mid = (low + high)/2
        saving = calc_saving(months_remaining, semi_annual_raise,r,annual_salary,mid/10000)
        steps += 1
        if abs(saving - total_cost*portion_down_payment)<=100:
            print(f"tsalingaas hadgalah tohiromjtoi huwi : {mid/10000:.4f}")
            print(f"hoyrtiin hailtiin alham: {steps}")
            found = True
            break
        if saving > total_cost*portion_down_payment:
            high = mid - 1
        else:
            low = mid+1
    if not found:
        print("Bolomjgiu")




if __name__ == "__main__":
    main()