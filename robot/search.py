from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# This is a fairly useless algorithm!
dir = 1
while True:
  move()
  
  if touch() == "wall":
    turn(dir)
    move()
    turn(dir)
    dir=-dir