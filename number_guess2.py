
def user_input():
    possible_input = ["too low", "too high", "you guessed"]
    while True:
        user_answer = input().lower()
        if user_answer in possible_input:
            break
        print("Input is not in ['too low', 'too high', 'you guessed']")
    return user_answer

def guess_the_number():
    print("Think about a number from 0 to 1000 and let me guess it!")
    print("Press Enter to continue")
    input()
    min = 0
    max = 1000
    answer = ""

    while answer != "you guessed":
        for i in range(10):
            guess = int((max - min) / 2) + min
            print("Guessing : " + str(guess))
            print()
            print("Tell me: -too low-, -too high- or -you guessed-")
            answer = user_input()

            if answer == "too high":
                max = guess
            elif answer == "too low":
                min = guess

        if i == 10:
            print("Don't cheat !!!")
            max = 1000
            min = 0
    print("I won !")

if __name__ == "__main__":
    guess_the_number()
