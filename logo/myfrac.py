from tealight.logo import move, turn

def tri(size):
     move(size)
     turn(120)
     move(size)
     turn(120)
     move(size)
     turn(120)

def segment(scale, n,pos):
  
  if n == 0:
     return
  else:
     if (pos==0):
       tri(scale)
     elif (pos==1):
       move(scale)
       tri(scale)
       move(-scale/2)
     elif (pos==2):
       turn(120)
       move(scale)
       turn(-120)
       tri(scale)
       turn(-120)
       move(scale)
       turn(120)
       
           
     segment(scale/2, n - 1, 0)
     segment(scale/2, n - 1, 1)
     segment(scale/2, n - 1, 2)
    

turn(-90)
move(150)
turn(180)

segment(150,3,0)
#move(-300)
