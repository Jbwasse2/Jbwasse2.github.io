---
title: "Image goal navigation [TerraSentia robot, Habitat, PyTorch]"
excerpt: "<img src='/portfolio/gif/onlineTopMapView.gif' width='300'><img src='/portfolio/gif/map.gif' width='250'>"
collection: portfolio
---
Mentors: [Unnat Jain](https://unnat.github.io/) and [Girish Chowdhary](http://daslab.illinois.edu/)

Recently I have been working on improving results on the image goal navigation task. I currently have a paper in this area under double blind review, so details are going to be kept to a minimum. But here are some cool visualizations!

Here is our method performing image goal navigation in Habitat on the Gibson dataset. The top down map shows our topological map being projected on a ground truth metric map (used for visualization purposes only)

<img src="/portfolio/gif/fullOnline.gif" width="700" style="display: block; margin: 0 auto" />

<img src="/portfolio/gif/greigsville500.gif" width="700" style="display: block; margin: 0 auto" />

Here is a demonstration of a part of our method that is tasked with moving the robot from the current view to the goal view by estimating a waypoint and then moving by utilizing Model Predictive Control.

<img src="/portfolio/gif/robot_view.gif" width="700" style="display: block; margin: 0 auto" />
