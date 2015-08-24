from tealight.logo import move, turn


def sierpinsky (scale, detail):
  if (detail>0) :
    move(scale)
    turn(120)
    sierpinsky(scale/2, detail-1)
    pause(0.5)
  if (detail>0) :
    move(scale)
    turn(120)
    sierpinsky(scale/2, detail-1)
    sleep(0.5)
  if (detail>0) :
    move(scale)
    turn(120)
    sierpinsky(scale/2, detail-1)
    sleep(0.5)

    
turn(90)
sierpinsky(300,5)