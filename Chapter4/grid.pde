//set the range for x-values
int xmin = -10;
int xmax = 10;

//set range for y-values
int ymin = -10;
int ymax = 10;

//calculate the range
int rangex = xmax - xmin;
int rangey = ymax - ymin;

//need to scale all x and y values when graphing, so they show up on the screen
int xscl = 5 * width/rangex;
int yscl = 5 * height/rangey;

void setup() {
 size(600,600);    
}

void draw() {
  //white
  background(255, 255, 255);
  translate(width/2, height/2);
  //cyan lines
  strokeWeight(3);
  stroke(0,255,255);
  //draws horizontal lines
  for (int i = xmin; i<xmax+1; i++){ 
    line(i * xscl, ymin * yscl, i * xscl, ymax *yscl);
  }
  //draws vertical lines
   for (int i = ymin; i<ymax+1; i++){ 
    line(xmin * xscl, i * yscl, xmax * xscl, i* yscl);
  }
  stroke(0);
  line(0, ymin*yscl, 0, ymax*yscl);
  line(xmin*xscl, 0, xmax*xscl, 0);
}
