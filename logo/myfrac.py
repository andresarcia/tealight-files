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
     tri(scale)
     segment(scale, n - 1)
 

    

turn(-90)
move(150)
segment(300,4)
#move(-300)
