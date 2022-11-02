from math import ceil, floor
class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """

        self.__offsets__ = {'Up': self.go_up, 'Down': self.go_down, 'Right': self.go_right, 'Left': self.go_left}
        self.shape = []
        self.direction = ''
        self.color = 'red'
        self.window_size = window_size
        self.GAME_OVER = False

    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """

        proceed = False
        if self.direction != 'Down':
            self.direction = 'Up'
            proceed = True
        if proceed:
            for i in range(len(self.shape)):
                if i == 0:
                    x = self.shape[i].xcor()
                    y = ceil(self.shape[i].ycor())
                    self.shape[i].sety(y + 20)
                else:
                    x1 = self.shape[i].xcor()
                    x2 = self.shape[i].ycor()
                    self.shape[i].goto(x, y)
                    x = x1
                    y = x2
        return None
    
    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """

        proceed = False
        if self.direction != 'Up':
            self.direction = 'Down'
            proceed = True
        if proceed:
            for i in range(len(self.shape)):
                if i == 0:
                    x = self.shape[i].xcor()
                    y = floor(self.shape[i].ycor())
                    self.shape[i].sety(y - 20)
                else:
                    x1 = self.shape[i].xcor()
                    x2 = self.shape[i].ycor()
                    self.shape[i].goto(x, y)
                    x = x1
                    y = x2              
        return None

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """

        proceed = False
        if self.direction != 'Right':
            self.direction = 'Left'
            proceed = True
        if proceed:
            for i in range(len(self.shape)):
                if i == 0:
                    x = self.shape[i].xcor()
                    y = floor(self.shape[i].ycor())
                    self.shape[i].setx(x - 20)
                else:
                    x1 = self.shape[i].xcor()
                    x2 = self.shape[i].ycor()
                    self.shape[i].goto(x, y)
                    x = x1
                    y = x2              
        return None

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """

        proceed = False
        if self.direction != 'Left':
            self.direction = 'Right'
            proceed = True
        if proceed:
            for i in range(len(self.shape)):
                if i == 0:
                    x = self.shape[i].xcor()
                    y = ceil(self.shape[i].ycor())
                    self.shape[i].setx(x + 20)
                else:
                    x1 = self.shape[i].xcor()
                    x2 = self.shape[i].ycor()
                    self.shape[i].goto(x, y)
                    x = x1
                    y = x2             
        return None

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        fc = False
        if self.shape[0].distance(current_food_position) < 20:
            fc = True
        return fc


    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """

        if self.shape[0].xcor() > self.window_size[0] / 2:
            self.shape[0].setx(-self.window_size[0] / 2)

        elif self.shape[0].xcor() < -self.window_size[0] / 2:
            self.shape[0].setx(self.window_size[0] / 2)

        elif self.shape[0].ycor() > self.window_size[1] / 2 - 40:
            self.shape[0].sety(-self.window_size[1] / 2)

        elif self.shape[0].ycor() < -self.window_size[1] / 2:
            self.shape[0].sety(self.window_size[1] / 2 - 40)

        return None


    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: boolean
        """

        for i in range(1, len(self.shape)):
            if self.shape[0].distance(self.shape[i]) < 20:
                self.GAME_OVER = True
                self.shape.clear()
                self.direction = ''
                break
        return self.GAME_OVER

    
