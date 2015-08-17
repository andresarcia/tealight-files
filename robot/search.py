from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
from random import random

# This is a fairly useless algorithm!
dir = 1
while True:
  move()
  
  while (smell() and look() != 'fruit'):
    turn(1)
  
  if smell()==0 and look() != 'fruit':
    steps = int(3*random())
    turn(steps)
    for i in range(1,5):
      move()