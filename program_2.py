# Program #2: Math Quiz
# Write a program that gives simple math quizzes.
# The program should display two random numbers to be added, such as 247 + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random

def mathProblem():
    x = random.randint(0,1000) # googled random.randint to generate random numbers
    y = random.randint(0,1000)
    correctAnswer = x + y
    print('what is', x, '+', y)

    StudentAnswer = int(input('Please type the answer: '))


    if correctAnswer == StudentAnswer:
        print("Correct answer!")
    else:
        print("Wrong! The correct answer is ", correctAnswer)

    #print(answer)

if __name__ == '__main__':
    mathProblem()
