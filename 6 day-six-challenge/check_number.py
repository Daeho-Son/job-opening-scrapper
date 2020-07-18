def check(max_len=""): # max_len이 있으면 number, 없으면 amount
    try:
        if max_len:
            number = int(input("#: "))
            if int(number) >= max_len:
                print("Choose a number from the list.\n")
                return check(max_len)
            else:
                return number
        else:
            amount = float(input())
            return amount
    except ValueError:
        print("That wasn't a number.\n")
        return check(max_len)
