from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

distance = 10
#for n in range(0, distance):
while touch() == 'fruit':
  move() 
  if left_side() == 'fruit':
      turn(-1)
  if right_side() == 'fruit':
      turn(1)