def ask_yes_no_question(question):
    while True:
        answer = input(question + " (yes/no): ").lower()
        if answer in ["yes", "no"]:
            return answer
        else:
            print("Invalid input. Please enter 'yes' or 'no.'")


def main():
    # Ask question 1
    answer_1 = ask_yes_no_question("Question 1: Is the amount of matrix in the rock is less than 15%?")

    if answer_1 == "yes":
        # Ask question 2 if the answer to question 1 is "yes"
        answer_2 = ask_yes_no_question("Question 2: Are the grains of the rock well-sorted?")

        if answer_2 == "yes":
            # Ask question 3 if the answer to question 2 is "yes"
            answer_3 = ask_yes_no_question("Question 3: Are the grains of the rock well-rounded?")

            if answer_3 == "yes":
                print("The rock is SUPERMATURE")
            else:
                print("The rock is MATURE")
        else:
            print("The rock is SUBMATURE")
    else:
        print("The rock is IMMATURE")


if __name__ == "__main__":
    main()
