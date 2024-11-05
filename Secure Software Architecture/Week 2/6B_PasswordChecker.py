def checkPassword(password):
    upper_characters, lower_characters, special_characters, digits, length = 0, 0, 0, 0, 0
    length = len(password)

    if length < 6:
        print("Password must be at least 6 characters long!\n")
    else:
        for i in range(0, length):
            if password[i].isupper():
                upper_characters += 1
            elif password[i].islower():
                lower_characters += 1
            elif password[i].isdigit():
                digits += 1
            else:
                special_characters += 1

    if upper_characters != 0 and lower_characters != 0 and digits != 0 and special_characters != 0:
        if length >= 10:
            print("The strength of password is strong.\n")
        else:
            print("The strength of password is medium.\n")
    else:
        if upper_characters == 0:
            print("Password must contain at least one uppercase character!\n")
        if lower_characters == 0:
            print("Password must contain at least one lowercase character!\n")
        if special_characters == 0:
            print("Password must contain at least one special character!\n")
        if digits == 0:
            print("Password must contain at least one digit!\n")


password = input("Please enter password: ")
checkPassword(password)
