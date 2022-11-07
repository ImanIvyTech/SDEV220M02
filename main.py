# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def m02lab(lastname, firstname, gpa):
    # Use a breakpoint in the code line below to debug your script.
    if gpa >= 3.5:
        print("Student has made the Dean's List")
    if gpa >= 3.25:
        print("Student has made the Honor Roll")
    while lastname != 'ZZZ':
        m02lab(lastname, firstname, gpa)

# Press the green button in the gutter to run the script.


def m02assignment4():
    secret = 5
    guess = 6
    if guess > secret:
        print('too high')
    elif guess < secret:
        print('too low')
    elif guess == secret:
        print('just right')
    small = True
    green = True
    if small & green:
        print('pea')
    if small & ~green:
        print('cherry')
    if ~small & green:
        print('watermelon')
    if ~small & ~green:
        print('pumpkin')


def m02assignment6():
    list = [3, 2, 1, 0]
    for integer in list:
        print(integer)
    guess_me = 7
    number = 1
    while number <= guess_me:
        if number < guess_me:
            print('too low')
        if number > guess_me:
            print('oops')
            break
        if number == guess_me:
            print('found it!')
        number += 1
    guess_me_too = 5
    for num in range(0, 10):
        if num < guess_me_too:
            print('too low')
        if num > guess_me_too:
            print('oops')
            break
        if num == guess_me_too:
            print('found it!')
            break


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
