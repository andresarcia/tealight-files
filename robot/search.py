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
  
  while (smell() and look() != 'fruit'):
    turn(1)
  
if (!smell() and look() != 'fruit'):
  turn(randon(1,3))
  for i in range(1,5)
    move()