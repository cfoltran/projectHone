void setup(){
  size(320, 360);
  background(120); 
  for(int i=0; i<600; i++){
    float x = random(width);
    float y = random(height);
    float r = random(0, 360);
    float b = random(210, 220);
    //noStroke();
    fill(r, 100, b, 200);
    ellipse(x, y, 24, 16);
  }
    save("test.png");
    exit();
  
}