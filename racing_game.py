# Racing game
# player and computer race
# each round randomly moves the players forward
# first to reach 50 points wins
# add speed / boost options
import random

player_score = 0
comp_score = 0
ch_lst = ["normal", "boost"]
current_player = "humn"
ch = [True, False]
choice = ""


while player_score <= 50 and comp_score <= 50:
    print(f"your score {player_score}\ncomputer score {comp_score}")

    def boost():
        score = random.randint(8, 15)
        return score

    def normal():
        score = random.randint(1, 8)
        return score

    if current_player == "humn":
        choice = str(input("Chose Your Car's Speed(normal or boost)"))
    else:
        choice = random.choice(ch_lst)

    if choice == "boost":
        if current_player == "humn":
            score = boost()
            rand_ch = random.choice(ch)
            if rand_ch:
                player_score = player_score + score
            current_player = "comp"
        else:
            rand_ch = random.choice(ch)
            score = boost()
            if rand_ch:
                comp_score = comp_score + score
            current_player = "humn"
    else:
        if current_player == "humn":
            score = normal()
            player_score = player_score + score
            current_player = "comp"
        else:
            score = normal()
            comp_score = comp_score + score
            current_player = "humn"

if player_score >= 50:
    print("You Win")
elif comp_score >= 50:
    print("Computer Win, you lose!!")