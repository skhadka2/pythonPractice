# Praciting how to do error handling in Python

from webbrowser import get


while True:
    try:
        get_age = int(input("What is yout age: "))

        if get_age <= 0 :
            raise Exception("That age is invalid. Try again.")
    except Exception as err:
        print(f"This is invalid {err}")

    except ValueError:
        print('please enter a number')

    
    else:
        print (f" Thanks your age is: {get_age}")
        break