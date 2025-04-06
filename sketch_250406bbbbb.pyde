x=1
def setup():

    size(600,400)
    colorMode(HSB,360,100,100)
def draw():
    global x
    fill(100,100,x)
    ellipse(300,200,50,50)
    x=x+1
