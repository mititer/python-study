try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print("error: " + str(err))
except ValueError:
    print("error: value error")
except:
    print("error: unexpected error")
