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
        qAndA = random.shuffe(questionAndAnswer)
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
