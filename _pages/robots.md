---
title: "Robotic Demos"
permalink: /robots/
redirect_from:
author_profile: true
  - /robots/
  - /robots.html

---

{% include base_path %}
-------------------------------

DASlab and the TerraSentia (Girish Chowdhary)
======

## Offline Topological Maps
At the start of graduate school I got interested in [topological mapping](https://arxiv.org/pdf/1803.00653.pdf). I ended up implementing the work of [Meng et al.](https://arxiv.org/pdf/1909.12329.pdf) on the [TerraSentia robot](https://www.nytimes.com/2020/02/13/science/farm-agriculture-robots.html)
. The topological map built from this work (right) is shown in contrast to the metric map built using [RTAB-Map](http://wiki.ros.org/rtabmap_ros) (left).

<img src="images/maps.png" width="720" style="display: block; margin: 0 auto" />

One can then use this topological map as well as a few trained models in order to navigate the robot to a goal image. This GIF is sped up by 2X.

<img src="gif/top2_fast.gif" width="400" style="display: block; margin: 0 auto" />

One point of failure in the topological map creation was in the edges that span across the map.

<img src="images/topmapwRed.png" width="340" style="display: block; margin: 0 auto" />

This would mean that two parts of the graph that are actually far apart are represented as being close in the topological map, causing the robot to fail to navigate to the goal. [Emmons et al.](https://arxiv.org/pdf/2003.06417.pdf) would coin this phenomenon as a wormhole.

When I applied Meng's method to the [Gibson dataset](http://gibsonenv.stanford.edu/database/) inside of [Habitat](https://arxiv.org/abs/1904.01201), the creation of wormholes in the topological map was still prevalent. In the following figure are image pairs connected in the topological map that were predicted to be similar, but were actually 5-20 meters apart.

<img src="images/wormholes.png" width="480" style="display: block; margin: 0 auto" />

One way that I seeked to eliminate wormholes was to incorporate pose estimates from [ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2).

<img src="images/system.png" width="720" style="display: block; margin: 0 auto" />

Using Meng's method, on average 7.29% of edges in the Gibson maps were wormholes. After incorporating pose I was able to reduce that to get an average of 0.19% of edges being wormholes. When using the respective maps on a down stream navigation task I found pruning the wormholes improved navigation success from 15.3% to 28.1%.

## Online Topological Maps
I am currently following a line of research where topological maps are made online for embodied AI tasks.

## Agriculture Robots
Agriculture is a very cool application of robotics. The robot will have to complete tasks in a GPS denied environment where everything looks the same, is slightly dynamic, with constant camera occlusion. When I first joined DASlab I assisted with two projects for the TerraSentia robot. The first project involved training a deep learning model to predict whether the robot is in a crop row or not. This was useful for other navigation and planning tasks performed by the robot such turning into a new row of crops. The model I trained ended up getting around 96% accuracy on this task.

<img src="gif/cornBot.gif" width="480" style="display: block; margin: 0 auto" />


The second project consisted of writing some scripts to do nightly testing of the robot's software. This interfaced with some external hardware as well as a Gazebo simulation.
<img src="images/ts.jpg" width="480" style="display: block; margin: 0 auto" />


Weasel Bots (Steven LaValle)
======
For my undergraduate thesis I worked on a "weasel bot" which was a simple, random, bouncing robot. I was interested in designing a mechanical structure that goes around the weasel bot that allows it to connect with other weasel bots. The ultimate goal in this project was to study what tasks can be accomplished through minimal sensing including pushing an object and having the robots join together in a configuration.

<img src="gif/weasel.gif" width="480" style="display: block; margin: 0 auto" />

This project resulted in a publication at MRS 2018 and also allowed me to open source a python package that was [more efficient](https://core.ac.uk/download/pdf/210999288.pdf) than SciPy at solving a system of equations when the equations were represented through a sparse Kronecker product.

Yaskawa (Industrial Robots)
======
At Yaskawa the applications engineering teams are responsible for making [some](https://www.youtube.com/watch?v=O3XyDLbaUmU) [cool](https://www.youtube.com/watch?v=xQB9AAZJluw) [robotics](https://www.youtube.com/watch?v=1F4-plhdnj0) [demos](https://www.youtube.com/watch?v=0-bw1PujfwQ). On this team I helped develop a motion planning library used for various applications of industrial robots.

I mostly ran my code on the following gantry robot in the thumbnail that was presented at a trade show.

[<img src="gif/gantry.gif" width="480" style="display: block; margin: 0 auto" />]( https://www.youtube.com/watch?v=DrRHJZl1ArQ "Gantry Prototype Robot")

Another system that I would test my code on was a robot arm demo that was designed to use its suction cups to grasp onto blocks from the green conveyor belt and pack them into a square on the white conveyor belt.

<img src="images/yaskawaPack.jpg" width="480" style="display: block; margin: 0 auto" />

A cool extension of the prototype gantry robot was on a gigantic 3D printer with a robot arm at one end that I helped a customer debug. The final demo of this project had the gantries 3D print a boat.

[<img src="gif/3dp.gif" width="480" style="display: block; margin: 0 auto" />]( https://www.youtube.com/watch?v=CYjeOOWMPA8 "Gigantic 3D Printer")

I have some further experience with factory robotics from when I did a separate internship at a plastic injection molding factory. That experience gave me some good experience in human-robotic interactions in an industrial setting as well as some insight into the lack of computer vision in industrial robotics processes.

BattleBots
======
During my Freshman and Sophomore year of college I was involved in the battlebots competitions. During my Freshman year I assisted with the machining, CAD, and some of the basic electronics for a battlebot that ultimately [failed to run](https://www.youtube.com/watch?v=yUQY5pSI5T0). During my Sophomore year I was head of electronics for the robot "Who Do You Know Here" which had weapon failure due to the weapon motor breaking shortly before its fight. This robot got destroyed so badly that to this day the local battlebots club uses it in their promo videos.
[<img src="gif/battlebot.gif" width="480" style="display: block; margin: 0 auto" />]( https://www.youtube.com/watch?v=55PbpuUi2n0 "WDYKH" )

Arity
======
At Arity I was responsible for creating a robotics demo that could help visualize the sensor readings from a car. For example, in this project the Stewart Platform would tilt backwords when the car was accelerating, forward when the car was deaccelerating, and to the side when turning. This tilt would also be affected by the speed of the car.

<img src="images/arity.jpg" width="480" style="display: block; margin: 0 auto" />

Robotics Outreach (FLL/FTC/FRC)
======
I am very passionate about outreach as I didn't have the opportunity to get involved in robotics until I got to UIUC. I previously mentored middle school aged students in FLL. I then went on to help expand the university's robotics outreach program to the local high schools to facilitate the creation and mentoring of some of the local FTC and FRC teams. I was also a judge for some local and regional FLL tournaments.
