from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here
def go():
  move()
  if (touch()!='fruit'):
    turn(-1)
    go()
    return
  go()
  
go()