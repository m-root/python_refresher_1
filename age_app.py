def age_app1():
    enter_age = input("Please enter your age in (s) or (y): ")

    if enter_age == "s":
        seconds_input = input("Please enter the number of seconds you have lived: ")
        print("You have lived for {} years since you were born".format(int(seconds_input)/60/60/24/365))

    elif enter_age == "y":
        years_input = input("Please enter the number of years you have been around: ")
        print("You have managed to live for {} seconds in this world".format(int(years_input)*60*60*24*365))
    else:
        print("Please enter the values correctly")

age_app1()
