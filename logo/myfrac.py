from tealight.logo import move, turn

def segment(scale, detail):
  
  if detail <= 0:
     return
  else:
     segment(scale, detail - 1)
     move(-scale)
     turn(120)
     move(-scale)
     turn(120)
     move(-scale)
     turn(120)
#     segment(scale / 2.0, detail - 1)
#     turn(-120)
#     segment(scale / 2.0, detail - 1)
#     turn(-120) 
#     segment(scale / 2.0, detail - 1)
#     turn(120)
#     segment(scale / 2.0, detail - 1)
#     turn(-120)
     
    

turn(-90)
move(150)
segment(300,2)
#move(-300)


 #   segment(scale, detail - 1)
  #  turn(120)
   # segment(scale / 2.0, detail - 1)
    #turn(120)
#    segment(scale / 2.0, detail - 1)
 #   turn(-120)
  #  segment(scale / 2.0, detail - 1)
   # turn(-120)
    #segment(scale / 2.0, detail - 1)
#    turn(120)
 #   segment(scale / 2.0, detail - 1)
  #  turn(120)
   # segment(scale, detail - 1)