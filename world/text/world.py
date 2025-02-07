import sys
if "maze" in sys.argv:
    import maze.maze as obstacles
else:
    import maze.obstacles as obstacles
# list of valid command names
valid_commands = ['off', 'help', 'replay', 'forward', 'back', 'right', 'left', 'sprint']
move_commands = valid_commands[3:]

# variables tracking position and direction
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0


# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100

#commands history
history = []