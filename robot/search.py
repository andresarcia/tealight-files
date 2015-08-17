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
  
  while (smell() and look() == -1):
    turn(1)