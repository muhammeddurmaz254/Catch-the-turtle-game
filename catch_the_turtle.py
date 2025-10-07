import turtle
import time
from random import randint

#Play board setup
turtle_play_board = turtle.Screen()
turtle_play_board.title("Catch The Turtle Game")
turtle_play_board.bgcolor("lightblue")
turtle_play_board.setup(width=800, height=600)
score = 0 #varieble to keep track of score

#Turtle setup
turtle_itself = turtle.Turtle()
turtle_itself.shape("turtle")
turtle_itself.speed(0)

#Function to update and display the score board
def display_the_score_board(score): 
    turtle_itself.clear()
    turtle_itself.teleport(0,250)
    turtle_itself.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    turtle_itself.teleport(0,0)

def game_scene():
    turtle_itself.hideturtle()
    turtle_itself.teleport(randint(-380,380), randint(-280, 280)) 
    time.sleep(1)
    turtle_itself.showturtle()
    time.sleep(1)
    turtle_itself.onclick(fxn)
    display_the_score_board(score)

def game_over(i, score):
    turtle_itself.teleport(0,0)
    turtle_itself.clear()
    turtle_itself.write("Game Over", align="center", font=("Courier", 24, "normal"))
    turtle_itself.teleport(0,-30)
    turtle_itself.write(f"{score} out of {i+1}", align="center", font=("Courier", 24, "normal"))

#Function to increase score when turtle is clicked
def fxn(x, y):
    turtle_itself.hideturtle()
    global score
    score +=1

#initial display scoreboard
display_the_score_board(score)
#Main game loop
for i in range(randint(10,20)):
    game_scene()
game_over(i, score)

turtle.mainloop()

