import random
import time


# Functions

def sleep1(amount=1):
    time.sleep(amount)


def new_line():
    print("\n")


# Variables
n_problems = 5  # could get user input to customize this value
count = 0
term1 = 0
term2 = 0
book_1_keys = []
attempts = 3  # could get user input to customize this value
answer = 0
score = 0  # NEED to implement results calculation

# Dictionaries
book_1 = {
}
book_1_answers = {

}

# Build Dictionary based off the value in n_problems
# Takes the randomly generated numbers in term1 & 2 creates a math equation, solves it
# Stores the answer & equation in a dictionary.
# Quizzes you and grades your answer in real time

print("Multiplication Exercises\n")
sleep1()

for i in range(n_problems):  # for loop to generate math problems and answers
    count += 1  # tracks current value in sequence
    term_1 = random.randint(1, 9)  # generates a random value
    term_2 = random.randint(1, 9)

    answer = term_1 * term_2  # evaluates expressions
    equation = str(term_1) + " * " + str(term_2)  # converters int to str

    # appends the dictionary book_1 with they key (count), value (equation)
    # book_1 will store the problem number and equation to print to the screen
    book_1[count] = equation

    # appends the dictionary book_1_answer with the key (count), value (answer)
    # book_1_answers will be used to compare user input with the corresponding answer to ensure correctness
    book_1_answers[count] = answer

for key, value in book_1.items():  # use for loop to access store values and print to screen

    print(value, " =\n")  # prints value(equation from book_1)
    answer = int(input("What is your answer:  "))  # receive input from user

    if answer == book_1_answers.get(key):  # if answer is correct go to the next question
        print("That is correct! Next question.")

    # while the users answer is wrong, and they did not run out of attempts, get the users input and check the answer
    while not attempts < 1 and answer != book_1_answers.get(key):

        attempts -= 1  # decrements the value store in attempts variable
        print("That is incorrect, try again.")
        answer = int(input("What is your answer:  "))  # receive input from user

        if answer == book_1_answers.get(key):  # if answer is correct go to the next question

            print("That is correct! Next question.")
            break  # exits loop for the current problem

        elif not attempts > 1:  # no more attempts, next question

            print("You have ran out of attempts.")
            break  # exits loop for the current problem
