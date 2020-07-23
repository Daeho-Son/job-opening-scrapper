def check(max_len):
    try:
        number = int(input("#: "))
        if int(number) >= max_len:
            print("Choose a number from the list.")
            return check(max_len)
        else:
            return number
    except ValueError:
        print("That wasn't a number.")
        return check(max_len)
