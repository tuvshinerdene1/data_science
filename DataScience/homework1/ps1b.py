def calc_months():
    annual_salary = int(input("Jiliin tsalin oruulna uu: "))
    portion_saved = float(input("Tsalingaas hadgalah huwi: "))
    semi_annual_raise = float(input("Hagas jiliin tsalingiin usult: "))
    total_cost = int(input("muruudliin baishingiin une: "))

    portion_down_payment = 0.25
    current_savings = 0
    r=0.04
    
    months_spent = 0
    target_price = total_cost * portion_down_payment

    while(current_savings < target_price):
        if months_spent%6 ==0 and months_spent > 0:
            annual_salary += annual_salary * semi_annual_raise
        current_savings += current_savings*r/12 + annual_salary/12*portion_saved
        months_spent += 1
    print(f"shaardagdah sar = {months_spent}")


def main():
    calc_months()
    

    


if __name__ == "__main__":
    main()