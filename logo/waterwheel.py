from tealight.logo import move, turn


def square(side):
  for i in range(0,4):
    move(side)
    turn(90)
    
def tri(side):
  for i in range(0,3):
    move(side)
    turn(120)

def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 2
  for i in range(0, edges):
    move(size)
    tri(decoration)
    turn(angle)

turn(-90)
waterwheel(12,75)
