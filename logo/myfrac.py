from tealight.logo import move, turn

def tri(size):
     move(-size)
     turn(120)
     move(-size)
     turn(120)
     move(-size)
     turn(120)

def segment(scale, n,pos):
  
  if n == 0:
     return
  else:
     if (pos==0):
       tri(scale/2)
     elif (pos==1):
       move(-scale/2)
       tri(scale/2)
     elif (pos==2):
       turn(60)
       move(-scale/2)
       turn(60)
       tri(scale/2)
       turn(120)
       move(-scale/2)
       turn(-60)
       move(-scale/2)
       turn(180)
           
     segment(scale/2, n - 1, 0)
     segment(scale/2, n - 1, 1)
     segment(scale/2, n - 1, 2)
    

#turn(-90)
move(150)

#segment(300,3,0)
#move(-300)
