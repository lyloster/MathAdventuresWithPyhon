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
//graph is reversed, need to account for it with ( '-' )
int yscl = -(5 * height/rangey);

void setup() {
 size(600,600);    
}

void draw() {
  //white
  background(255, 255, 255);
  //moves origing to center of screen
  translate(width/2, height/2);
  myGrid(xscl, yscl);
  //draws an ellipse at (3,6)
  //fill(0);
  //ellipse(3 * xscl, 6 * yscl, 10,10);
  graphFunction();
  
}

void myGrid(int xscl, int yscl){
  //cyan lines
  strokeWeight(3);
  stroke(0,255,255);
  //draws vertical lines
  for (int i = xmin; i<xmax+1; i++){ 
    line(i * xscl, ymin * yscl, i * xscl, ymax *yscl);
  }
    //draws horizontal lines
   for (int i = ymin; i<ymax+1; i++){ 
    line(xmin * xscl, i * yscl, xmax * xscl, i* yscl);
  }
  //draws axes
  stroke(0);
  line(0, ymin*yscl, 0, ymax*yscl);
  line(xmin*xscl, 0, xmax*xscl, 0);
}

double parabola(double x){
  return Math.pow(x, 2);
}

//draws a graph of a parabola statring at xmin and going up to xmax
void graphFunction(){
  double x = xmin;
  while( x<=xmax){
    fill(0);
    line((float)x*xscl,(float)parabola(x)*yscl,(float)(x+0.1)*xscl,(float)parabola(x+0.1)*yscl);
    x+=0.1;
  } 
}
