def getIntInput(prompt = "Enter an integer: ", exceptStatement = "Invalid input. "):
    while True:
        try:
            var = int(input(prompt))
            return var

        except ValueError:
            print(exceptStatement, end = "")

while True:
    # get input
    dayNum = getIntInput("Enter day (1-Sunday, 2-Monday, etc.) [0 to exit]: ")

    if dayNum == 0:
        break

    while dayNum < 1 or dayNum > 7:
        dayNum = getIntInput("Incorrect input. Enter day (1-Sunday, 2-Monday, etc.): ", "")

    daysInMonth = getIntInput("Enter the number of days in month: ")

    # create days of the week
    weekDays = ["Sun", "Mon", "Tue", "Wed", "Thr", "Fri", "Sat"]

    print(" ".join(weekDays))

    # add spacing
    spacesBetweenNumbers = [2, 6, 10, 14, 18, 22, 26]
    spacingIdx = " " * spacesBetweenNumbers[dayNum-1]
    print(spacingIdx, end="")
    spacingIdx = len(spacingIdx)

    # add day numbers
    for day in range(1, daysInMonth+1):
        if day < 9:
            print(f"{day}   ", end="")

        else:
            print(f"{day}  ", end="")

        spacingIdx += 4

        if day < 9:
            if spacingIdx > 27:
                print("\n  ", end="")
                spacingIdx = 1
        else:
            if spacingIdx > 27:
                print("\n ", end="")
                spacingIdx = 1
    print("\n")