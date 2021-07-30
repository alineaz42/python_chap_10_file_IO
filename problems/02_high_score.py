def game():
    return 100


score = game()

# reading the score board
with open("highScore.txt", "r") as f:
    hiscore = f.read()
# if the score board is empty
if hiscore == '':
    with open("highScore.txt", "w") as f:
        f.write(str(score))
        print(f"your score was updated {score} ")

# if the score board is not empty
elif int(hiscore) < score:
    with open("highScore.txt", "w") as f:
        f.write(str(score))
else:
    print(f"You score was {score} which is less than hiscore {hiscore} ")
