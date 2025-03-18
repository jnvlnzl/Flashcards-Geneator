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
