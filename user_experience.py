#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------
import random


#---------------------------------------

def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
    # Add your code here
    #------------------------
    difficultylevel = input("enter difficulty level").lower()
    if difficultylevel == "easy" or difficultylevel== "medium" or difficultylevel=="hard":
        return difficultylevel
    else:
        print("enter either easy medium or hard")
print(choose_difficulty())

#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
    # Add your code here
    #------------------------
    sorted_dict = dict(sorted(leaderboard.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict
    #------------------------
dic = {"ali": 34, "zaz": 67, "bob": 50, "dan": 45}
sorted_dic = display_leaderboard(dic)
print(sorted_dic)

#---------------------------------------

def save_score(player_name, score, file_path):
    with open(file_path,"a") as file:
        file.write(f"{player_name},{score}\n")
x = r"C:\Users\studentfcs\Desktop\lab22\scores.txt"
players_and_scores = [("Player1", 100), ("Player2", 150), ("Player3", 80)]

for player, score in players_and_scores:
    save_score(player, score, r"C:\Users\studentfcs\Desktop\lab22\scores.txt")




#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    leaderboard = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                player, score = line.strip().split(",")
                leaderboard[player] = int(score.split()[0])
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Creating a new one.")
    return leaderboard
print(load_top_scores(r"C:\Users\studentfcs\Desktop\lab22\scores.txt"))

#---------------------------------------

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")


#---------------------------------------

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    x = options.copy()
    x.remove(correct_answer)
    y = random.choice(x)
    a = [correct_answer,y]
    return a


#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------



