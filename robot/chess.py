from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

distance = 10
longest_d = 0
#for n in range(0, distance):
while touch() == 'fruit':
  move() 
  if touch() != 'fruit':
    if longest_d == 0
       longest_d = moves
    if left_side() == 'fruit' and longest_d and :
        turn(-1)
    elif right_side() == 'fruit':
        turn(1)
  if right_side() == 'fruit':
    turn(1)
  elif left_side() == 'fruit':
    turn(-1)