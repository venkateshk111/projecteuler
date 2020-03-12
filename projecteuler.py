# Python Program for Problems described at https://projecteuler.net/archives
def project_euler_1(maxnumber,number1,number2):
    result=0
    for num in range(1,maxnumber):
        if (num%number1 or num%number2 == 0):
            result += num
        num +=num
    print(f"Sum of all the multiples of {number1} or {number2} below {maxnumber} is: {result}")
def project_euler_2(max):
    first_num = 1
    second_num = 2
    fib_num = 0
    even_sum = 2
    while ((first_num + second_num) <= max):
        fib_num = first_num + second_num
        if fib_num % 2 == 0:
            even_sum = even_sum + fib_num
        first_num = second_num
        second_num = fib_num
    print(f"Even sum of fibo until {max} is:{even_sum}")
while True:
    print("Please select the the Program to be executed from the below list: ")
    menu = """
    1 ==> Multiples of 3 and 5
    2 ==> Even Fibonacci numbers
    3 ==> Largest prime factor
    -1 ==> Exit from the program
    """
    problem_id = int(input(menu))
    #print(problem_id)
    if problem_id == 1:
        project_euler_1(1000,3,5)
    elif problem_id == 2:
        project_euler_2(4000000)
    elif problem_id == 3:
        pass
    elif problem_id == -1:
        exit(0)
    else:
        print("\n\nInvalid Choice:Please choose from below or choose -1 to exit")
exit(0)
