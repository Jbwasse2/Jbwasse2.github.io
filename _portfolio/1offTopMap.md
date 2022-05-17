---
title: "Offline topological mapping [TerraSentia robot, Habitat, PyTorch]"
excerpt: "<img src='/portfolio/gif/top2_fast.gif' width='400'>"
collection: portfolio
---

At the start of graduate school I got interested in [topological mapping](https://arxiv.org/pdf/1803.00653.pdf). I ended up implementing the work of [Meng et al.](https://arxiv.org/pdf/1909.12329.pdf) on the [TerraSentia robot](https://www.nytimes.com/2020/02/13/science/farm-agriculture-robots.html)
. The topological map built from this work (right) is shown in contrast to the metric map built using [RTAB-Map](http://wiki.ros.org/rtabmap_ros) (left) of the lab I work in.

<img src="/portfolio/images/maps.png" width="720" style="display: block; margin: 0 auto" />

One can then use this topological map as well as a few trained models in order to navigate the robot to a goal image. This GIF is sped up by 2X.

<img src="/portfolio/gif/top2_fast.gif" width="400" style="display: block; margin: 0 auto" />

One point of failure in the topological map creation was in the edges that span across the map.

<img src="/portfolio/images/topmapwRed.png" width="340" style="display: block; margin: 0 auto" />

This would mean that two parts of the graph that are actually far apart are represented as being close in the topological map, causing the robot to fail to navigate to the goal. [Emmons et al.](https://arxiv.org/pdf/2003.06417.pdf) would coin this phenomenon as a wormhole.

When I applied Meng's method to the [Gibson dataset](http://gibsonenv.stanford.edu/database/) inside of [Habitat](https://arxiv.org/abs/1904.01201), the creation of wormholes in the topological map was still prevalent. In the following figure are image pairs connected in the topological map that were predicted to be similar, but were actually 5-20 meters apart.

<img src="/portfolio/images/wormholes.png" width="480" style="display: block; margin: 0 auto" />

One way that I seeked to eliminate wormholes was to incorporate pose estimates from [ORB-SLAM2](https://github.com/raulmur/ORB_SLAM2).

<img src="/portfolio/images/system.png" width="720" style="display: block; margin: 0 auto" />

Using Meng's method, on average 7.29% of edges in the Gibson maps were wormholes. After incorporating pose I was able to reduce that to get an average of 0.19% of edges being wormholes. When using the respective maps on a down stream image-goal navigation task I found pruning the wormholes improved navigation success from 15.3% to 28.1%.

I am currently following a line of research where topological maps are made online for embodied AI tasks.
