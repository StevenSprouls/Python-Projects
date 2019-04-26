
Difficulty = input("please enter what level of difficulty. \n"
                   "beginner/intermediate/advanced: ")


questions = int(input("how many questions: "))

correct = 0

# this is to gen our random numbers for beginner
if Difficulty.lower() == "beginner":
    for i in range(questions):
        random_num1 = randint(1, 10)
        random_num2 = randint(1, 10)
        add_sub = randint(1, 2)
        if add_sub == 1:
            answer = input("What is %d + %d? " % (random_num1, random_num2))
            product = (random_num1+random_num2)
            if float(product) == float(answer):
                print("CORRECT!")
                correct = correct+1
            else:
                print("Wrong!")
        elif add_sub == 2:
            answer = input("What is %d - %d? " % (random_num1, random_num2))
            product = (random_num1-random_num2)
            if float(product) == float(answer):
                print("CORRECT!")
                correct = correct+1
            else:
                print("Wrong!")
        else:
            print("error")
# this is to random gen for intermediate
elif Difficulty.lower() == "intermediate":
    for i in range(questions):
        random_num1 = randint(1, 25)
        random_num2 = randint(1, 25)
        add_sub = randint(1, 4)
        if add_sub == 1:
            answer = float(input("What is %d x %d? " %
                                 (random_num1, random_num2)))
            product = (random_num1 * random_num2)
            if round(float(product), 2) == round(float(answer), 2):
                print("CORRECT!")
                correct = correct + 1
            else:
                print("Wrong!")
        elif add_sub == 2:
            answer = float(input("What is %d / %d? " %
                                 (random_num1, random_num2)))
            product = (random_num1 / random_num2)
            if round(float(product), 2) == round(float(answer), 2):
                print("CORRECT!")
                correct = correct + 1
            else:
                print("Wrong!")
        elif add_sub == 3:
            answer = input("What is %d - %d? " % (random_num1, random_num2))
            product = (random_num1 - random_num2)
            if round(float(product), 2) == round(float(answer), 2):
                print("CORRECT!")
                correct = correct + 1
            else:
                print("Wrong!")
        elif add_sub == 4:
            answer = input("What is %d + %d? " % (random_num1, random_num2))
            product = (random_num1 + random_num2)
            if round(float(product), 2) == round(float(answer), 2):
                print("CORRECT!")
                correct = correct + 1
            else:
                print("Wrong!")
        else:
            print("error")


# this random gens the advanced questions
elif Difficulty == "advanced":
    if Difficulty.lower() == "advanced":
        for i in range(questions):
            random_num1 = randint(1, 10)
            random_num2 = randint(1, 10)
            random_num3 = randint(1, 10)
            add_sub = randint(1, 5)
            if add_sub == 1:
                answer = input("What is %d * %d²? " %
                               (random_num1, random_num2))
                product = (random_num1*random_num2**2)
                if round(float(product), 2) == round(float(answer), 2):
                    print("CORRECT!")
                    correct = correct+1
                else:
                    print("Wrong!")
            elif add_sub == 2:
                answer = input("What is (%d - %d)/%d²? " %
                               (random_num1, random_num2, random_num3))
                product = ((random_num1-random_num2)/(random_num3**2))
                if round(float(product), 2) == round(float(answer), 2):
                    print("CORRECT!")
                    correct = correct+1
                else:
                    print("Wrong!")
            elif add_sub == 3:
                answer = input("What is (%d / %d)/(%d/%d)? " %
                               (random_num1, random_num2,
                                random_num3, random_num1))
                product = ((random_num1/random_num2)/(random_num3/random_num1))
                if round(float(product), 2) == round(float(answer), 2):
                    print("CORRECT!")
                else:
                    print("Wrong!")
            elif add_sub == 4:
                answer = input("What is ((%d²)(2))/%d² ? " %
                               (random_num1, random_num2))
                product = ((random_num1**2)(2)/(random_num2**2))
                if round(float(product), 2) == round(float(answer), 2):
                    print("CORRECT!")
                    correct = correct+1
                else:
                    print("Wrong!")
            elif add_sub == 5:
                answer = input("What is %d*%d^%d? " %
                               (random_num1, random_num2, random_num3))
                product = (random_num1*random_num2**random_num3)
                if round(float(product), 2) == round(float(answer), 2):
                    print("CORRECT!")
                    correct = correct+1
                else:
                    print("Wrong!")
            else:
                print("error")
# this is for when the user is stupid
else:
    print("please choose one of the given levels")
# this calculates the percentage
percentage = int((correct/questions)*100)

# this tells the user what to do after they finish the test
if percentage > 66:
    print("Well done!")
elif 66 >= percentage >= 33:
    print("You need more practice!")
else:
    print("Please talk to your math teacher!")

print("Your total correct is: ", percentage, "%")
