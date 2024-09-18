# Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random
import winsound
import time

# Score variable
score = 0
comp_score = 0

# Setup screen
turtle.setup(650, 650)
wn = turtle.Screen()
wn.bgcolor('black')
wn.bgpic('kbgame-bg.gif')
wn.tracer(1.8)

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.color('white')
for side in range(4):
  mypen.forward(600)
  mypen.left(90)
mypen.hideturtle()

# Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
player.speed(0)

# Create opponent turtle
comp = turtle.Turtle()
comp.color('red')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Create competition score
mypen2 = turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()


# Create food
maxFoods = 10
foods = []
for food in range(maxFoods):
  food = turtle.Turtle()
  food.shapesize(.5)
  food.color("lightgreen")
  food.shape("circle")
  food.penup()
  food.speed(0)
  food.setposition(random.randint(-290, 290), random.randint(-290, 290))
  foods.append(food)

# Set speed variable
speed = 1

# Set game time limit for 1 minute (60 seconds)
timeout = time.time() + 10*6


# Define functions
def turn_left():
  player.left(30)

def turn_right():
  player.right(30)

def increase_speed():
  global speed
  speed += 1

def reduce_speed():
  global speed
  # at speed = 0, turtle stops
  if speed == 0:
    speed = 0
  else:
    speed -= 1

def isCollision(obj1, obj2):
  d = math.sqrt(math.pow(obj2.xcor() - obj1.xcor(),2) + math.pow(obj2.ycor() - obj1.ycor(),2))
  if d < 20 :
    return True
  else:
    return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left,'Left')
turtle.onkey(turn_right,'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(reduce_speed, 'Down')

while True:
  gametime = 0
  if gametime == 6 or time.time() > timeout:
    break
  gametime = gametime - 1

  player.forward(speed)
  # Boundary Player Checking x coordinate
  if player.xcor() > 290 or player.xcor() < -290:
    player.right(180)
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
  # Boundary Player Checking y coordinate
  if player.ycor() > 290 or player.ycor() < -290:
    player.right(180)
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

  comp.forward(12)
    # Boundary Player Checking x coordinate
  if comp.xcor() > 290 or comp.xcor() < -290:
    comp.right(180)
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
  # Boundary Player Checking y coordinate
  if comp.ycor() > 290 or comp.ycor() < -290:
    comp.right(180)
    winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
  
  
  for food in foods:
    # Move goal around
    food.forward(3)

    if food.xcor() > 290 or food.xcor() < -290:
      food.right(180)
    if food.ycor() > 290 or food.ycor() < -290:
      food.right(180)

    # Collision Detection
    if isCollision(food, player):
      winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
      score += 1
      # Draw the score on the screen
      mypen.undo()
      mypen.penup()
      mypen.hideturtle()
      mypen.setposition(-290, 300)
      scorestring = "Score: %s" %score
      mypen.write(scorestring, False, align='left', font=('Arial', 12, 'normal'))
      food.setposition(random.randint(-290, 290), random.randint(-290, 290))
      food.right(random.randint(0, 360))

     # Collision Detection
    if isCollision(food, comp):
      winsound.PlaySound('chomp.wav', winsound.SND_ASYNC)
      comp_score += 1
      # Draw the score on the screen
      mypen2.undo()
      mypen2.penup()
      mypen2.hideturtle()
      mypen2.setposition(-290, 300)
      scorestring = "Score: %s" %scomp_core
      mypen2.write(scorestring, False, align='left', font=('Arial', 12, 'normal'))
      food.setposition(random.randint(-290, 290), random.randint(-290, 290))
      food.right(random.randint(0, 360))

if (int(score) > int(comp_score)):
  mypen.setposition(0,0)
  mypen.color("yellow")
  mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
  mypen.setposition(0,0)
  mypen.color("yellow")
  mypen.write("Game Over: Toy LOSE", False, align="center", font=("Arial", 28, "normal"))

delay = input("Press Enter to finish.")
