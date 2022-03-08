def rom(input):
    while input != 0:
        if input >= 1000:
            print("M", end = '')
            input -= 1000
        elif input >= 900:
            print("CM", end = '')
            input -= 900
        elif input >= 500:
            print("D", end = '')
            input -= 500
        elif input >= 400:
            print("CD", end = '')
            input -= 400
        elif input >= 100:
            print("C", end = '')
            input -= 100
        elif input >= 90:
            print("XC", end = '')
            input -= 90
        elif input >= 50:
            print("L", end = '')
            input -= 50
        elif input >= 40:
            print("XL", end = '')
            input -= 40
        elif input >= 10:
            print("X", end = '')
            input -= 10
        elif input >= 9:
            print("IX", end = '')
            input -= 9
        elif input >= 5:
            print("V", end = '')
            input -= 5
        elif input >= 4:
            print("IV", end = '')
            input -= 4
        elif input > 1:
            print("I", end = '')
            input -= 1
        elif input == 1:
            print("I")
            input -= 1
        else:
            print(" ")
            return

deez = int(input())
rom(deez)