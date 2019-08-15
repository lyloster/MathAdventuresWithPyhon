#set the range for x-values

xmin = -10
xmax = 10

#set range for y-values
ymin = -10
ymax = 10

#calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    #scaling the coordinates down
    
    global xscl, yscl
    size(600,600)
    
    #need to scale all x and y values when graphing, so they show up on the screen
    xscl = width/rangex
    yscl = height/rangey
    
    def draw():
        global xscl, yscl
        #white
        background(white)
        translate(width/2, height/2)
        #cyan lines
        strokeWeight(1)
        stroke(0,255,255)
        for i in range(xmin, xmax+1):
            line(i * xscl, ymin * yscl, i * xscl, ymax *yscl)
            line(xmin * xscl, i * yscl, xmax * xscl, i* yscl) 
        
        
