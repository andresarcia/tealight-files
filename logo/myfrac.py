from tealight.logo import move, turn

def segment(scale, detail):
  
  if detail == 0:
    move(scale)
  else:
    segment(scale / 2.0, detail - 1)
    turn(60)
    segment(scale / 2.0, detail - 1)
    turn(120)
    segment(scale / 2.0, detail - 1)
    turn(120)
    segment(scale / 2.0, detail - 1)
    turn(-150)

    

turn(-90)
#move(-100)
segment(400,2)
#move(-300)