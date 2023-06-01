# hand-tracking-for-computer-control
Hand tracking software that utilizes media pipes object detection capabilities to track the users hand and number of fingers raised. based on the number of fingers raised the user can control various actions on their computer (it is set up for Mac users only)
The main intention of this project was to be able to control a computer without touching it. This project was a stepping stone into another project I have had in mind for setting up a camera in my living room to control smart appliances such as lights, TV, etc. by just using your fingers. 
This is a summary of the basic controls
start by holding up 0 fingers. Essentially make a fist with your hand and it should be fine. 

2 Fingers up: Scrolls the page or document down

3 Fingers up: Scrolls the page or document up

4 Fingers up: Minimizes the window

5 Fingers up: enters and exits full screen

6 fingers up: reloads a browser. 

The way it works is if you hold up a finger then that specific fingers count will incrase by 1 every time the program goes through its main while loop. If 2 and 3 are held for a long time then it scrolls one tick each time through the loop. To reset the count of each finger simply make a fist or take your hands out of the screen and it will reset all of the finger counts back to 0. 
