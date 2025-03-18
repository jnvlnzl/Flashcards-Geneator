from createFlashcards import CreateFlashCards
from practiceFlashcards import PracticeFlashCards
from programChoice import ProgramChoice

def PracticeChoice():
    if start == "1":
        CreateFlashCards()
        practice = input("Start practice? \n [Input YES or NO] ")
        if practice.upper() == "YES":
            PracticeFlashCards()
        elif practice.upper() == "NO":
            exit()
        else:
            print("Invalid input. Try again.")
            PracticeChoice()

    elif start == "2":
        PracticeFlashCards()
    else:
        print("Invalid input. Try again.")
        ProgramChoice()
