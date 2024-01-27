# Question2: Write a program that prints a multiplication table for numbers up to 12
def multiplication_table(num):
    # initialize the list
    result = [[0 for i in range(num)]for j in range(num)]
    for i in range(1, num+1):
        for j in range(1, num+1):
            result[i-1][j-1] = i*j
    headings = [i+1 for i in range(num)]
    format_row = "{:>12}"*(num+1)

    print(format_row.format("", *headings))
    for col, row in zip(headings, result):
        print(format_row.format(col, *row))

multiplication_table(2)
multiplication_table(5)
multiplication_table(10)
multiplication_table(12)


# Question3: Write a program that asks a user to input a string and then determine if it’s a palindrome.
def is_Palindrome():
    flag = True

    def helper(str):
        if len(str) == 2:
            return str[1] == str[0]
        elif len(str) == 1:
            return True
        else:
            if str[0] != str[len(str)-1]:
                return False
            else:
                return helper(str[1:len(str)-1])
    while flag:
        input_string = input("Enter a String: ")
        if input_string == 'q':
            break
        elif helper(input_string):
            print("The string "+input_string+" is a palindrome")
        else:
            print("The string "+input_string+" is not a palindrome")

is_Palindrome()



# Question4: Write a program that asks the user to input two lists of equal length
def merge_lists():
    list1 = input("Input list1, use comma to separate each element: ").split(',')
    list2 = input("Input list2, use comma to separate each element: ").split(',')
    def helper(list1, list2):
        if len(list1) == 1:
            return [list1[0], list2[0]]
        else:
            return [list1[0], list2[0]]+helper(list1[1::],list2[1::])


    if len(list1) == len(list2):
        print(helper(list1, list2))
    else:
        print("The lists are not the same length")

merge_lists()

# Question5: Write a program that computes the list of the first 100 Fibonacci numbers.
def Fibonacci(int):
    out_put = [1,1]
    for i in range(2, int):
        out_put.append(out_put[-2]+out_put[-1])

    print(out_put)

Fibonacci(100)



# Question6: Write a program that determines if an inputed year is a leap year
def is_leap_year():
    while True:
        year = int(input("Enter a year: " ))
        flag = False
        if year % 4 == 0:
            flag =True
        if year % 100 == 0:
            flag = False
        if year % 400 == 0:
            flag = True
        if flag:
            print('The year: '+ str(year)+ ' is a leap year')
        else:
            print('The year: '+ str(year)+ ' is a not leap year')

is_leap_year()
