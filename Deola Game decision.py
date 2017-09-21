while True:  # while this truth remains this code will run. It will loop infinitely unless I break it at some point.

    your_answers = ["yes", "no", "maybe", "maybe not"]
    print("Welcome to this fun game by Olu T. Oni.\n")
    print("\nPlease enter: Yes, No, Maybe or Maybe not. Note that each start with a capital letter")
    print("\nThis application is strictly for Deola. If you are not Deola you will be insulted")

    name = input("\nwhat is your name?  ")

    if name != "Deola":
        print("\nDear {}, This application is not for you so buzz off".format(name))
        break
    else:
        ans = input(name + " " + "Do you want to take Erhabhor seriously?: ")
        ans = ans.lower()

    if ans not in your_answers:  # if here imposes some condition. It it were 'for' then it will look in an iterable list. for x in b <= thats how its used
        print("\n{} Be smart. You could have typed \"No\" or something like that! Try again".format(
            name))  # if answer is unacceptable it prints this and runs again

    elif ans != "no":
        print("\nWrong decision {}. I don't trust Erhabhor and so shouldn't you".format(
            name))  # if not no it prints this and goes to the beginning again
        quit()

    else:  # if it is found in your_answers or not no, then it prints the below
        print(
            "correct decision {}. you have a good head on your shoulders. The world is tough but you are tougher".format(
                name))
        print("Have a blissful day or night {}. ".format(name))
        input("Please enter to quit awesome game Adeola\n")

