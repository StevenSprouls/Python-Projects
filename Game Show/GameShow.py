
import random


def game():
    """This holds the function for the game"""
    # Sets score to 0 intially
    score = 0
    wrong = 0
    # Questions
    questions = [{"question": "What is the price of a motorcycle?",
                  "answers": ["$1000", "$5000", "$10000", "$15000"],
                  "correct": 2},
                 {"question": "How much is this toaster?",
                  "answers": ["$2", "$5", "$7"],
                  "correct": 2},
                 {"question": "What is the price of a dog?",
                  "answers": ["$1", "$5000", "$100", "$70"],
                  "correct": 3},
                 {"question": "How much is this electric pooper scooper?",
                  "answers": ["$200000", "$90", "$72.99"],
                  "correct": 3},
                 {"question": "What is the price of apple sauce?",
                  "answers": ["$.50", "$5", "$3", "$1"],
                  "correct": 4},
                 {"question": "is this lamborghini worth $100,000?",
                  "answers": ["True", "False"],
                  "correct": 1},
                 {"question":
                  "What is the price of a lifesize manaquin of batman?",
                  "answers": ["$2,530", "$500", "$100", "$45"],
                  "correct": 1},
                 {"question": "How much is this 1 night vacation in idaho?",
                  "answers": ["$400", "$1000", "$95"],
                  "correct": 3},
                 {"question": "What is the price of a honda Accord?",
                  "answers": ["$1000", "$9500", "$6000", "$18000"],
                  "correct": 4},
                 {"question":
                  "is this gold plated microwave worth over $2,000?",
                  "answers": ["True", "False"],
                  "correct": 1}]
    # Shuffles questions
    random.shuffle(questions)
    print("Welcome to the price is right!")
    # loop for questions
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["answers"]):
            print(str(i + 1) + ". " + choice)
        try:
            answer = int(input("Choose an answer: "))
        except ValueError:
            answer = 0
        while answer <= 0 or answer > len(question["answers"]):
            print("Bad input. Try again!")
            try:
                answer = int(input("Choose an answer: "))
            except ValueError:
                answer = 0
        if answer == question["correct"]:
            print("That is correct!")
            score = score + 1
        else:
            print("That answer is incorrect!")
            wrong = wrong + 1
    # Score + Thank you message
    print()
    print()
    print("Your total score is:", score, "right, and", wrong, "wrong.")
    print("Thanks for playing the price is right!")
    print()
    main()


def main():
    """Calls all options"""
    while True:
        print("Welcome to the Price is Right!"
              "I'm your host, Python! What would you like to start with?!")
        print()
        option = input("Play, View Credits, or Quit:")
        if option.lower() == "play":
            return game()
        elif option.lower() == "view credits":
            print("Created by: Steve Sprouls")
        elif option.lower() == "quit":
            exit()
        else:
            False
            print()
            print("Sorry, that is not a valid input, please try again!")
            print()

# Calls main
if __name__ == '__main__':
    main()
