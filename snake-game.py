import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Snake head
head = turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 250)
score_display.write("Score: 0  High Score: 0", align="center", font=("Arial", 24, "bold"))

# Snake movement functions
def move_up():
    if head.direction != "down":
        head.direction = "up"

def move_down():
    if head.direction != "up":
        head.direction = "down"

def move_left():
    if head.direction != "right":
        head.direction = "left"

def move_right():
    if head.direction != "left":
        head.direction = "right"

# Move snake
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keypress bindings
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Snake body segments
segments = []

# Main game loop
while True:
    screen.update()

    # Check for border collision
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    # Check for food collision
    if head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        new_segment = turtle.Turtle()
        new_segment.shape("square")
        new_segment.color("orange")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score: high_score = score
        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Arial", 24, "bold"))

    # Move the segments
    for index in range(len(segments) - 1, 0, -1):
        segments[index].goto(segments[index - 1].xcor(), segments[index - 1].ycor())
    if segments:
        segments[0].goto(head.xcor(), head.ycor())

    move()

    # Check for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            score_display.clear()
            score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Lucida Console", 24, "bold"))

    time.sleep(delay)

screen.mainloop()
