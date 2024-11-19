from turtle import Turtle, Screen
from tkinter import messagebox
import random
start=False
colors=['violet', 'indigo', 'blue', 'red','green', 'yellow', 'orange']
y_positions=[90,60,30,0,-30,-60,-90]
all_turtles=[]



screen = Screen()
screen.setup( width=500, height=400)
bet=screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? Enter a color:\n{', '.join(colors)}") 


for tindex in range(0,7):
  new_turtle = Turtle(shape='turtle')
  new_turtle.penup()
  new_turtle.goto(x=-230,y=y_positions[tindex])
  new_turtle.color(colors[tindex])
  all_turtles.append(new_turtle)

if bet:
  start=True

while start:
  for turtle in all_turtles:
    if turtle.xcor()>230:
      start=False
      if bet == turtle.pencolor():
        messagebox.showinfo("Result", f"You won! The winner is {turtle.pencolor()}")
        print(f"You won, The winner is {turtle.pencolor()}")
      else:
        messagebox.showinfo("Result", f"You lost! The winner is {turtle.pencolor()}")
        print(f"You lose, The winner is {turtle.pencolor()}")
      break      
        
    move=random.randint(0,10)
    turtle.forward(move)

screen.bye()



