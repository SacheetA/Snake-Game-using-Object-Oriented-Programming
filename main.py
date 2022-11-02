"""
Imports:
Snake.py which contains the Snake class
Food.py which contains the Food class
Turtle module to implement game graphics
"""

import Snake
import Food
import turtle
import time

""""
The main file for the program that implements the Python game using 
the turtle module. 

Global variables:

DELAY: The value after which the main game loop reruns. This sets how 
fast the snake moves. This value is to be slowly decremented as the 
game progresses.

COUNTER: Variable to keep count of the number of elapsed frames since
the last decrement of the DELAY variable.
"""
DELAY = 100
COUNTER = 0
SCORE = 0

def game_loop() -> None:

    """
    Function that implements the main game loop. All updations are to be
    done in this function. Function should also implement GAME OVER logic
    and do the decrement in DELAY appropriately.
    :return: None
    """

    global DELAY
    global COUNTER
    global SCORE
    global eraseble
    
    # keep snake on screen
    snake_obj.keep_snake_onscreen()

    if snake_obj.check_food_collision(food_obj.position):
        # new snake segment using turtle object
        new_segment = turtle.Turtle("circle")
        new_segment.color('green')
        new_segment.penup()

        # add segment towards the tail
        snake_obj.shape.append(new_segment)
        food_obj.update_random_food_position(snake_obj.shape)
        food_turtle.goto(food_obj.position)

        # keep count of score
        SCORE += 1
        eraseble.clear()
        eraseble = erasableWrite(t, f"Score: {SCORE}", font = ("Comic Sans", 16, "bold"), align = "center")

        # speed regulator
        if DELAY > 25 and COUNTER == 1:
            DELAY -= 1
            COUNTER = 0
        COUNTER += 1

    # snake controls
    if snake_obj.direction == 'Up':
            snake_obj.go_up()
    elif snake_obj.direction == 'Down':
            snake_obj.go_down()
    elif snake_obj.direction == 'Left':
            snake_obj.go_left()
    elif snake_obj.direction == 'Right':
            snake_obj.go_right()

    # check if game over
    game_over = snake_obj.update_snake()
    
    # update screen
    screen.update()

    # handle game over
    if game_over:
        turtle.write(f'GAME OVER', align = 'center', font=('Comic Sans', 16, 'bold'))
    else:
        turtle.ontimer(game_loop, DELAY)
    
        

def erasableWrite(tortoise, name, font, align, reuse=None):
    eraser = turtle.Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser


#####################################################################################################3

if __name__ == "__main__":
    """
    The main for the program.
    DO NOT CHANGE    
    """

    screen_height = 500
    screen_width = 500
    start_time = time.time()

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Python in Python")
    screen.bgcolor("blue")
    screen.tracer(0)

    snake_obj = Snake.Snake(window_size=(screen_width, screen_height))
    food_obj = Food.Food(window_size=(screen_width, screen_height))
    food_obj.update_random_food_position(snake_obj.shape)

    snake_turtle = turtle.Turtle("circle")
    snake_turtle.color(snake_obj.color)
    snake_turtle.penup()

    food_turtle = turtle.Turtle()
    food_turtle.shape(food_obj.shape)
    food_turtle.color(food_obj.color)
    food_turtle.pensize(food_obj.size)
    food_turtle.penup()

    screen.listen()
    screen.onkey(snake_obj.go_up, "Up")
    screen.onkey(snake_obj.go_down, "Down")
    screen.onkey(snake_obj.go_right, "Right")
    screen.onkey(snake_obj.go_left, "Left")

    # Initialize snake head and food turtle
    snake_obj.shape.append(snake_turtle)
    food_turtle.goto(food_obj.position)

    t = turtle.Turtle()
    t.hideturtle()
    t.up()
    t.goto(0, 225)
    eraseble = erasableWrite(t, "Score: 0", font=("Comic Sans", 16, "bold"), align = "center")

    game_loop()
    turtle.done()

    ######################################################################################################