import EOB_stats_module as stat
#Start of program
print("Welcome to the statistics calculator\n")

#Gets user input
running = True
values = []
print("Please input your list of numbers that you would like to analyze,enter \"done\" when you are finished adding to the list\n")
while running:
    inputt = (input("Enter your number: "))
    if inputt == "done":
        print()
        running = False
    elif inputt.isdigit():
        inputt = int(inputt)
        values.append(inputt)
    else:
        print("Invalid input try again...")
        continue

#printing menu
running = True
while running:
    stat.menu()
    option = input("Input your option: \n")
    if option == '1':
        average = stat.mean(values)
        print(f'The mean of your list of numbers is {average:.2f}\n')
    elif option == '2':
        calc = stat.variance(values)
        print(f'The variance of your list of numbers is {calc:.2f}\n')
    elif option == '3':
        sd = stat.standard_deviation(values)
        print(f'The standard deviation of your numbers is {sd:.2f}\n')
    elif option == '4':
        se = stat.standard_error(values)
        print(f'The standard error of your numbers is {se:.2f}\n')
    elif option == '5':
        new = int(input("Enter your new observation: "))
        z = stat.zscore(values, new)
        print(f'The z-score of the newly entered observation is {z:.2f}\n')
        values.append(new)
    elif option == '6':
        print(f'{stat.summary(values)}\n')

    elif option == 'q':
        running = False
    else:
        print("Enter a valid option....")
        continue



