def check_number(
    max_len="", from_code="", to_code=""
):  # max_len이 있으면 number, 없으면 amount
    try:
        if max_len:  # currency_code의 list 범위 체크
            number = int(input("#: "))
            if int(number) >= max_len:
                print("Choose a number from the list.\n")
                return check_number(max_len, from_code, to_code)
            else:
                return number
        else:  # amount가 문자인지 체크
            print(f"How many {from_code} do you want to convert to {to_code}?")
            amount = float(input())
            return amount
    except ValueError:
        print("That wasn't a number.\n")
        return check_number(max_len, from_code, to_code)
