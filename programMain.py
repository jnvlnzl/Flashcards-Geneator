import csv

def CreateFlashCards():
    noOfTopics = int(input("Enter the number of topics: "))
    for i in range(noOfTopics):
        with open((input(f"Topic {str(i + 1)}:")) + '.csv', 'w', newline='') as file:
            flashcards = csv.writer(file)
            flashcards.writerow(["Questions", "Answers"])

            noOfItems = int(input("Enter the number of items: "))
            for j in range (noOfItems):
                questions = input(f"Question {str(j + 1)}:")
                answers = input(f"Answer {str(j + 1)}:")
                flashcards.writerow([questions, answers])

import csv
import random

def PracticeFlashCards():
    questionAndAnswer = list()

    # read csv and add to dictionary
    numOfTopicsToStudy = int(input("Enter number of topics to study: "))
    for i in range(numOfTopicsToStudy):
        with open((input("Enter the " + str(i + 1) + " st/nd/rd/th topic you would like to study \n "
        "[Note that the input should be the same as the file name for that specific topic without the '.csv']: ") + '.csv')) as file:
            reader = csv.DictReader(file)
            for row in reader:
                questionAndAnswer.append(row)

    score = 0
    numOfQuestions = int(input("Enter the number of questions:"))

    for i in range(numOfQuestions):
        qAndA = random.choice(questionAndAnswer)
        print("Question:", qAndA["Questions"])
        inputAnswer = input('Answer:')
        correctAnswer = str(qAndA["Answers"])

        if inputAnswer == correctAnswer:
            print("Correct!")
            score += 1
        else:
            print("Wrong.")
            score += 0

    print("Total Score:", score)

def PracticeChoice():
    practice = input("Start practice? \n [Input YES or NO] ")
    if practice.upper() == "YES":
        PracticeFlashCards()
    elif practice.upper() == "NO":
        exit()
    else:
        print("Invalid input. Try again.")
        PracticeChoice()

def ProgramChoice():
    start = input("\n 1. Create Flashcards \n 2. Practice with Flashcards?\n [Input 1 or 2] ")
    if start == "1":
        CreateFlashCards()
        PracticeChoice()

    elif start == "2":
        PracticeFlashCards()
    else:
        print("Invalid input. Try again.")
        ProgramChoice()

print ("Welcome to your Flashcards!")
print ("General Directions: ")
print ("1. This program allows you to create, save, and practice with your Flashcards.")
print ("2. Enter 'Create Flashcards' if you want to make flashcards. \n   Enter 'Practice with Flashcards' if you want to practice by taking a quiz.")
print ("3. Take note that all of the .py and .csv files should be in ONE folder. \n   [.csv files are where your flashcards per topic are saved. \n   The file name should follow the inputted topic title.]")
print ("4. You can choose how many topics to study and which specific topics you want to use.")
print ("5. You can choose the number of questions you want to answer.")
print ("6. The questions are randomized.")
print ("7. Your score will be revealed after the quiz.")

ProgramChoice()
