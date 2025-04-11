import random
def ex01():
    for i in range(1,11):
        print(i)

def ex02():
    n = int(input("Enter a number: "))
    sum = 0
    for i in range(1, n):
        sum += i
    print("The sum is", sum)

def ex03():
    n = int(input("Enter a number: "))
    sum_even = 0
    sum_odd = 0
    for i in range(1, n):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    print("The sum even is", sum_even)
    print("The sum odd is", sum_odd)

def ex04():
    s = input("Enter a string: ")

    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in s:
        if i in vowels:
            count += 1
    print("The number of vowels in the string is: ", count)

def ex05():
    s = input("Enter a string: ")
    print("The string is: ", s)
    print("The number of words in the string is: ", len(s.split()))

def ex06():
    num = random.randint(1, 100)

    print("Select level:")
    print("1. Easy (10 times guess)")
    print("2. Medium (6 times guess)")
    print("3. Hard (4 times guess)")
    level = input("Enter the level you want: ").lower()

    if level == "easy":
        max_attempts = 10
    elif level == "medium":
        max_attempts = 6
    elif level == "hard":
        max_attempts = 4
    else:
        print("The level is invalid. It is set to medium in default.")
        max_attempts = 6

    print(f"\nYou have {max_attempts} times to guess the number from 1 to 100.")
    for i in range(1, max_attempts + 1):
        guess_num = int(input("Enter a number: "))
        if num == guess_num:
            print(f"Correct! You guessed the number in {i} times.")
        else:
            if num > guess_num:
                print(f"Sorry, the number you guessed is lower than the random number.")
            else:
                print(f"Sorry, the number you guessed is higher than the random number.")
    print("Game Over! The random number is: ", num)

if __name__ == '__main__':
    # ex01()
    # ex02()
    # ex03()
    # ex04()
    # ex05()
    ex06()