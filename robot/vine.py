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
  if (look()!='fruit'):
    return
  go()
  
print look()
go()