# ---------------------------------------
#  Question Bank
#    Student B
# ---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"), ("what is the closest planet to sun?", "mercury"),
        ("what is chemical name of baking soda? ", "NaHCO3 "), ("who proposed the three laws of motion?", "newton")

    ],
    "Maths": [("what is the value of 5 factorial (5!)", "120"), ("what is the result of 12 divided by 3", "4"),
              ("sum of angles in a triangle", "180")

              ],
    "English": [("what is synonym of HAPPY?", "JOYFUL"), ("what is plural of child?", "children"),
                ("what is past tense of run", "ran")]
}

hints = {
    "Science": ["it starts with h", "it has 7 letters", "it contains Na", "bro had IQ of 150"
                # Pair each question with a corresponding hint.
                ], "maths": ["its >100", "use /", "add all the side angles"], "english": ["joy___", "8 letters",
                                                                                          "u to a"]
    # Repeat for other categories as needed.
}

# ---------------------------------------
import random


def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    questions = {
        "Science": [
            ("What is the chemical symbol for water?", "H2O"), ("what is the closest planet to sun?", "mercury"),
            ("what is chemical name of baking soda? ", "NaHCO3 "), ("who proposed the three laws of motion?", "newton")

        ],
        "Maths": [("what is the value of 5 factorial (5!)", "120"), ("what is the result of 12 divided by 3", "4"),
                  ("sum of angles in a triangle", "180")

                  ],
        "English": [("what is synonym of HAPPY?", "JOYFUL"), ("what is plural of child?", "children"),
                    ("what is past tense of run", "ran")]
    }
    for key, value in questions.items():
        if key == category:
            break
    chose = random.choice(value)
    a, b = chose
    return a

    # ------------------------

    # ------------------------

    # ------------------------


# ---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    # ------------------------
    if player_answer == correct_answer:
        return True
    else:
        return False
    # ------------------------

    # ------------------------


# ---------------------------------------

def remove_question(category):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    # ------------------------
    for c, value in questions.items():
        if c == category:
            index = 0
            for chose in value:
                a, b = chose
                if a == question:
                    break
                else:
                    index = index + 1

    questions[category].pop(index)




    # ------------------------

    # ------------------------


# ---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    # ------------------------

    # ------------------------
    print("Questions:", question)
    ans = input("enter your answer")
    return ans

    # ------------------------


# ---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    # ------------------------
    
    # ------------------------

    # ------------------------


# ---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    # ------------------------
    # Add your code here
    # ------------------------
    raise NotImplementedError("This function is not implemented yet.")
    # ------------------------

# ---------------------------------------
