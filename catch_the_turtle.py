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


turtle.mainloop()

