from tealight


def sierpisky (scale, detail):
  if (detail>0) :
    move(scale)
    turn(120)
    sierpinsky(scale/2, detail-1)
  if (detail>0) :
    move(scale)
    turn(120)
    sierpinsky(scale/2, detail-1)
  if (detail>0) :
    move(scale)
    turn(120)
    sierpinsky(scale/2, detail-1)
    
    
turn(90)
sierpinsky(200)