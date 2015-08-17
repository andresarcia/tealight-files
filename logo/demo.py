from tealight.net import connect, send

connect("myapp")

def handle_message(msg):
  print "Received: "+msg
  print age()