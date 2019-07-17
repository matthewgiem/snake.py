import random
import curses
import math
# use curses to initialize the screen
s = curses.initscr()
# set the curser to 0 so it doesn't show up on the screen
curses.curs_set(0)
# get the screen hight and the screen witdth
sh, sw = s.getmaxyx()
# create a new window with the hight and witch of the screen and starting at the top left hand corner of the screen
w = curses.newwin(sh, sw, 0, 0)
# accepts keypad input
w.keypad(1)
# refreshes the screen every 100 mili seconds
w.timeout(100)
#

snake_x = math.floor(sw/4)

snake_y = math.floor(sh/2)

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x -1 ],
    [snake_y, snake_x - 2]
]

food = [math.floor(sh/2), math.floor(sw/2)]

w.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        food = None
        while food is None:
            new_food = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]

            # food = new_food if new_food not in snake else None
            food = new_food

        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)
