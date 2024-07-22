import random

def game():
    #Greets
    print("Welcome to the game!")
    print("It will be printing random values from 1 to 100")
    
    #Getting random value
    score  = random.randint(1, 100)
    
    #if initial score is blank asign 0 else asign value itself
    with open("highScore.txt") as f:
        highScore = f.read()
        if(highScore==''):
            highScore = 0
        else:
            highScore = int(highScore)

    #if random value is greater that any previous value write that score in file            
    if(score>highScore):
        print("New high score achieved", score)
        with open("highScore.txt", "w") as f:
            f.write(str(score))
    else:
        print("Your score: ", score)

game()