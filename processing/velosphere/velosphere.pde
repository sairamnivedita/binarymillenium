/*\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
 * binarymillenium 2008
 * binarymillenium.com
 * GNU GPL
 *
 * Load csv point cloud files and convert to png height map files
 *//////////////////////////////////////////////////////////////

import processing.opengl.*;
//import java.util.*

BufferedReader reader;

CloudConverter converter;

void setup() {
 
  //String base = "/home/lucasw/gprocessing/velosphere/frames/";
  String base = "C:/cygwin/home/lucasw/google/processing2/velosphere/frames/";
  converter = new CloudConverter(base);

spectrum_setup();

update();
}

boolean run = true;

void draw() {
  if(run) update();
  else exit();
}

String outbase = "unit_46_Monterey_subset_";

void update() {
  
  counter++;

      
    reader = createReader("../velodyne/data/" + outbase + counter + ".csv");
    if (reader == null) {
      run = false;    
    }
    
    loadPoints();

    println(counter);

}

int counter = 1;

void loadPoints() {

    String raw[] = new String[0]; 

    boolean continuing = true;

    //while(continuing) {
    for (int i = 0; i <1280; i++){
      
      String newline = "";
      try {
        newline = reader.readLine();
      } catch(Exception e) {
         continuing = false;
         
      }
       
 
      if (continuing) raw = append(raw, newline);
    }
       
    converter.processStrings(raw); 

  return;
}


