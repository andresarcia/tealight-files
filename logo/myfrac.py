from tealight.logo import move, turn

def tri(size):
     move(-size)
     turn(120)
     move(-size)
     turn(120)
     move(-size)
     turn(120)

def segment(scale, n):
  
  if n <= 0:
     return
  else:
     segment(scale/2, n - 1)
     move(-scale/2)
     tri(scale/2)
      
 

    

turn(-90)
move(150)
segment(300,2)
#move(-300)
