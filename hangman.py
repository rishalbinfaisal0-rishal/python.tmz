movies = [
    "Avatar",
    "Titanic",
    "Inception",
    "Interstellar",
    "Joker",
    "Batman",
    "Superman",
    "Spiderman",
    "Ironman",
    "Deadpool",
    "Gladiator",
    "Godfather",
    "Goodfellas",
    "Scarface",
    "Rocky",
    "Rambo",
    "Terminator",
    "Predator",
    "Alien",
    "Jaws",
    "Frozen",
    "Coco",
    "Moana",
    "Shrek",
    "Toy Story",
    "Finding Nemo",
    "Cars",
    "Up",
    "Ratatouille",
    "Zootopia",
    "Avengers",
    "Endgame",
    "Infinity War",
    "Thor",
    "Hulk",
    "Antman",
    "Doctor Strange",
    "Black Panther",
    "Aquaman",
    "Wonder Woman",
    "Harry Potter",
    "Twilight",
    "Divergent",
    "Hunger Games",
    "Maze Runner",
    "Jurassic Park",
    "King Kong",
    "Godzilla",
    "Transformers",
    "Fast Five",
    "The Dark Knight",
    "Pulp Fiction",
    "Forrest Gump",
    "The Matrix",
    "John Wick",
    "Mission Impossible",
    "Top Gun",
    "Cast Away",
    "The Lion King",
    "Aladdin",
    "Dangal",
    "3 Idiots",
    "PK",
    "Lagaan",
    "Sholay",
    "Drishyam",
    "Jawan",
    "Pathaan",
    "Dhoom",
    "Chennai Express",
    "Baahubali",
    "Pushpa",
    "RRR",
    "KGF",
    "Kantara",
    "Leo",
    "Vikram",
    "Master",
    "Kaithi",
    "Thuppakki",
    "Premam",
    "Manichitrathazhu",
    "Drishyam 2",
    "Bangalore Days",
    "Charlie",
    "Kumbalangi Nights",
    "Lucifer",
    "Aavesham",
    "Bheeshma Parvam",
    "Minnal Murali",
    "2018",
    "Jallikattu",
    "Uyare",
    "Traffic",
    "Mumbai Police",
    "Narasimham",
    "Devasuram",
    "Kilukkam",
    "Ramji Rao Speaking",
    "Thudarum"
] 
import random

selected_movie = random.choice(movies).upper()
hidden_movie = ""
upd_movie = ""
player_guess = ""
chances = 5
guessed_chars = []
print(selected_movie)

for i in selected_movie:
    if i == " ":
        hidden_movie = hidden_movie + "  "
    else:
        hidden_movie = hidden_movie + "_ "

print(hidden_movie)

while chances > 0 and upd_movie != selected_movie:
    player_guess = input(
        "Guess a character or the movie name: ").upper().strip()
    

    if player_guess == selected_movie:
        upd_movie = selected_movie
        print("Correct! You guessed the movie!")
        break

    elif len(player_guess) == 1:
        if player_guess in guessed_chars:
            print("You already guessed that character!")
            continue

        guessed_chars.append(player_guess)

        if player_guess in selected_movie:
            print("Correct character!")

            upd_movie = ""
            for i in selected_movie:
                if i == " ":
                    upd_movie = upd_movie + "  "
                elif i in guessed_chars:
                    upd_movie = upd_movie + i + " "
                else:
                    upd_movie = upd_movie + "_ "
        else:
            chances -= 1
            print("Wrong guess!")

    else:
        chances -= 1
        print("Wrong movie name!")

    print(upd_movie if upd_movie else hidden_movie)
    print(f"Chances left: {chances}")

if upd_movie == selected_movie:
    print("You win!")
else:
    print(f"Game over! The movie was {selected_movie}")
