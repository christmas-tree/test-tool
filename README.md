Christmas tree open pixel control
================

This is a fork, and strip of https://github.com/zestyping/openpixelcontrol. It's 
intended use is for testing the christmas tree.  

Using this implementation, you can write your own patterns and animations and
test them in a simulator. This repository has been stripped to only include two 
programs: 

* `gl_server` (Mac or Linux only): Receives OPC commands from a client and
  displays the LED pixels in an OpenGL simulator.  Takes a "layout file"
  that specifies the locations of the pixels in a JSON array; each item
  in the array should be a JSON object of the form {"point": [x, y, z]}
  where x, y, z are the coordinates of the pixel in space.  Click and drag
  to rotate the 3-D view; hold shift and drag up or down to zoom.

* `layouts/tree.py` Creates json files to be used in `gl_server`. It takes 
  two parameters, the first parameter is the number of led strips, second 
  parameter is the number of controllable led's per strip. 


Quickstart (simulator)
----------------------

**Step 1.** If you're using Linux, first get the dependencies you need
(Mac users skip to step 2):

    apt-get install mesa-common-dev freeglut3-dev

**Step 2.** Compile and start the GL simulator:

    make
    bin/gl_server -l layouts/tree-<strips>-<pixels>.json
    
    Replace <strips> with the number of strips the code uses and <pixels> with the
    amount of pixels per strip your code is based on. 

**Step 3.** Start an animation
    
    Create an animation, like 'https://github.com/christmas-tree/animation-disco', 
    and run the main() method with the following enviroment vars:
    - MICRONAUT_SERVER_PORT=8081
    - CONSUL_ENABLED=false
    - ZIPKIN_ENABLED=false

**Step 4.** Start the christmas tree controller 

    Checkout 'https://github.com/christmas-tree/controller' and run the main() method with 
    the following enviroment vars: 
    - DEBUG=true
    - OPC_HOSTNAME=localhost
    - CONSUL_ENABLED=false
    - ZIPKIN_ENABLED=false

**Step 5.** Profit!

    If all goes well, an animation should be visible in your gl_server window. 

