---
#title: " <center> Last Mile Embodied Visual Navigation </center>"
title: ""
excerpt: "<img src='/portfolio/gif/onlineTopMapView.gif' width='300'><img src='/portfolio/gif/map.gif' width='250'>"
collection: portfolio
---
<html>
<head>
  <meta charset="utf-8">
  <meta name="description"
        content="Last Mile Embodied Visual Navigation ">
  <meta name="keywords" content="SLING, last-mile-navigation, embodied-AI">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Last-Mile Embodied Visual Navigation</title>

  <!-- Global site tag (gtag.js) - Google Analytics -->
  <script>
    window.dataLayer = window.dataLayer || [];

    function gtag() {
      dataLayer.push(arguments);
    }

    gtag('js', new Date());

    gtag('config', 'G-PYVRSFMDRL');
  </script>

  <link href="https://fonts.googleapis.com/css?family=Google+Sans|Noto+Sans|Castoro"
        rel="stylesheet">

  <link rel="stylesheet" href="./static/css/bulma.min.css">
  <link rel="stylesheet" href="./static/css/bulma-carousel.min.css">
  <link rel="stylesheet" href="./static/css/bulma-slider.min.css">
  <link rel="stylesheet" href="./static/css/fontawesome.all.min.css">
  <link rel="stylesheet"
        href="https://cdn.jsdelivr.net/gh/jpswalsh/academicons@1/css/academicons.min.css">
  <link rel="stylesheet" href="./static/css/index.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script defer src="./static/js/fontawesome.all.min.js"></script>
  <script src="./static/js/bulma-carousel.min.js"></script>
  <script src="./static/js/bulma-slider.min.js"></script>
  <script src="./static/js/index.js"></script>
</head>
<body>



<section class="hero">
  <div class="hero-body">
    <div class="container is-max-desktop">
      <div class="columns is-centered">
        <div class="column has-text-centered">
          <h1 class="title is-1 publication-title">Last-Mile Embodied Visual Navigation </h1>
          <div class="is-size-5 publication-authors">
            <span class="author-block">
              <a href="https://jbwasse2.github.io/">Justin Wasserman</a><sup>1*†</sup>,</span>
            <span class="author-block">
              <a href="https://www.karmeshyadav.com/">Karmesh Yadav</a><sup>2</sup>,</span>
            <span class="author-block">
              <a href="http://daslab.illinois.edu/">Girish Chowdhary</a><sup>1†</sup>,
            </span>
            <span class="author-block">
              <a href="http://www.cs.cmu.edu/~abhinavg/">Abhinav Gupta</a><sup>3</sup>,
            </span>
            <span class="author-block">
              <a href="https://unnat.github.io/">Unnat Jain</a><sup>2*</sup>,
            </span>
          </div>

          <div class="is-size-6 publication-authors">
            <span class="author-block"><sup>1</sup>University of Illinois at Urbana-Champaign,</span>
            <span class="author-block"><sup>2</sup>Facebook AI Research,</span>
            <span class="author-block"><sup>3</sup>Carnegie Mellon University</span><br>
            <span class="author-block"><sup>*</sup>Equal Contribution</span>
            <span class="author-block"><sup>†</sup>Corresponding Authors</span>
          </div>

          <div class="column has-text-centered">
            <div class="publication-links">
              <!-- PDF Link. -->
              <span class="link-block">
                <a href="../../files/sling.pdf"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fas fa-file-pdf"></i>
                  </span>
                  <span>Paper</span>
                </a>
              </span>
              <!-- Video Link. 
              <span class="link-block">
                <a href="https://www.youtube.com/watch?v=MrKrnHhk8IA"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fab fa-youtube"></i>
                  </span>
                  <span>Video</span> 
                </a>
              </span>-->
              <!-- Code Link. -->
              <span class="link-block">
                <a href="https://github.com/Jbwasse2/SLING"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fab fa-github"></i>
                  </span>
                  <span>Code</span>
                  </a>
              </span>
<!--            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section> -->


<section class="hero teaser">
  <div class="container is-max-desktop">
    <div class="hero-body">
    <div class="images">
      <video id="teaser" autoplay controls muted loop playsinline>
        <source src="/portfolio/vids/full_nav.mp4"
                type="video/mp4">
      </video>
      <img src='/portfolio/images/sling/improv1.svg'>
    </div>
    Left video sped up x20
<!--      <video id="teaser" autoplay muted loop playsinline width="58%">
        <source src="/portfolio/vids/full_nav.mp4"
                type="video/mp4">
      </video>
      <img src='/portfolio/images/sling/improv1.svg' height='2%'>
        <h2 class="subtitle has-text-centered">
        <span class="dnerf">SLING</span> can be used with previous image-goal navigation methods to improve last-mile navigation. Left video sped up x20.
      </h2>-->
    </div>
  </div>
</section>



<section class="section">
  <div class="container is-max-desktop">
    <!-- Abstract. -->
    <div class="columns is-centered has-text-centered">
      <div class="column is-four-fifths">
        <h2 class="title is-3">Abstract</h2>
        <div class="content has-text-justified">
          <p>
           Realistic long-horizon tasks like image-goal navigation involve exploratory and exploitative phases. Assigned with an image of the goal, an embodied agent must explore to discover the goal, i.e., search efficiently using learned priors. Once the goal is discovered, the agent must accurately calibrate the last-mile of navigation to the goal. As with any robust system, switches between exploratory goal discovery and exploitative last-mile navigation enable better recovery from errors. Following these intuitive guide rails, we propose SLING to improve performance of existing image-goal navigation systems. Entirely complementing prior methods, we focus on last-mile navigation, and leverage the underlying geometric structure of the problem with neural descriptors. With simple but effective switches, we can easily connect SLING with heuristic, reinforcement learning, and neural modular policies.
          </p>
          <p>
           On a standardized image-goal navigation benchmark, we improve performance across policies, scenes, and episode complexity, raising the state-of-the-art from 45% to 55% success rate and 28.0% to 37.4% SPL. Beyond photorealistic simulation, we conduct real-robot experiments in three physical scenes and find these improvements to transfer well to real environments.
          </p>
        </div>
      </div>
    </div>
    <!--/ Abstract. -->

  </div>
</section>

<section class="section">
  <div class="container is-max-desktop">
    <!-- SLING -->
    <div class="columns is-centered has-text-centered">
      <div class="column">
        <h2 class="title is-3">SLING</h2>
      <img src='/portfolio/images/sling/overview_lmn.svg' width='300'>
      We propose <strong>S</strong>witchable <strong>L</strong>ast-Mile <strong>I</strong>mage-Goal <strong>N</strong>avi<strong>g</strong>ation<p style="margin-top:0.5cm; margin-bottom:1cm;"> <strong>(SLING)</strong> -- a simple yet very effective geometric navigation module and associated switches. Our approach can be combined with any off-the-shelf learned policy that uses semantic priors to explore the scene. As soon as the object or view of interest is detected, the SLING switches to the geometric navigation module.
      </p>
        <video id="dollyzoom" autoplay controls muted loop playsinline width="100%">
            <source src="/portfolio/vids/sling/slides2.mp4"
                    type="video/mp4">
        </video>
        <p style="margin-top:0.5cm;">
           <strong>Last-Mile Navigation: </strong>Neural keypoint features descriptors are extracted and matched to obtain correspondences between agent's view and image-goal. The geometric problem of estimating the relative pose between the agent and goal view is solved using efficient perspective-n-point. The estimations are fed into a local policy head to decide the agent's actions.
        </p>
      </div>
    </div>
  </div>
</section>


<!-- Results. -->
<!--<section class="section">
  <div class="container is-max-desktop">
    <div class="columns is-centered has-text-centered">
      <div class="column">
        <h2 class="title is-3">Results</h2>
      <img src='/portfolio/images/sling/improv1.svg' width='950'>
        <h2 class="subtitle has-text-centered">
        <p style="margin-top:0.5cm;">
        <span class="dnerf">SLING</span> improves navigation results across all baselines and datasets.
        </p>
      </h2>
      </div>
    </div>
  </div>
</section> -->

<section class="section">
  <div class="container is-max-desktop">
    <!-- Results. -->
    <div class="columns is-centered has-text-centered">
      <div class="column">
        <h2 class="title is-3">Results</h2>
        <p style="margin-top:0.5cm;">
        <h2 class="title is-4">Last-Mile Navigation Only</h2>
        <div class="containerhl1">
          <p>
          <b>Previous Method:</b> In this real-world last-mile navigation example, the previous method predicted a waypoint (red square in top down map) that was not within 1 meter of the goal (blue square/circle in top down map, visualized in top left corner). Even worst, it caused the robot to hit the corn! Video sped up x3.
          <br><span style="color: #ff0000">Failure</span>
          </p>
        <video id="dollyzoom" autoplay controls muted playsinline width="100%">
            <source src="/portfolio/vids/nrns.m4v"
                    type="video/mp4">
        </video>
        <br>
          <p>
          <b>SLING:</b> However, with SLING, the agent predicted a valid waypoint and was able to navigate towards the goal. Video sped up x3.
          <br><span style="color: #00ff00">Success</span>
          </p>
        <video id="dollyzoom" autoplay controls muted playsinline width="100%">
            <source src="/portfolio/vids/sling.m4v"
                    type="video/mp4">
        </video>
        </div>
        <br>
        <h2 class="title is-4">Geometric Switches Improve Success Rate</h2>
        <div class="containerhl2">
          <p>
          <b>Previous Method:</b> The switching mechanism at (0:02) fails to notice that the agent is close to the goal and continues exploring the environment. This causes the agent to explore more and then once in the kitchen at (0:36), it believes it is near the goal causing it to navigate to the final waypoint and fail. The goal is shown in the topdown map as a the red circle, and the agent is the blue circle.
          <br><span style="color: #ff0000">Failure</span>
          </p>
          <video id="dollyzoom" autoplay controls muted playsinline width="100%">
              <source src="/portfolio/vids/sling/nrns/2t7WUuJeko7_80.mp4"
                      type="video/mp4">
          </video>
          <br>
          <p>
          <b>SLING:</b> Our switching mechanism notices the goal at (0:02) and navigates to a point near the goal. 
          <br><span style="color: #00ff00">Success</span>
          </p>
          <video id="dollyzoom" autoplay controls muted playsinline width="100%">
              <source src="/portfolio/vids/sling/sling/2t7WUuJeko7_80.mp4"
                      type="video/mp4">
          </video>
        </div>
        <br>
        <h2 class="title is-4">SLING Improves Last-Mile Navigation Over Previous Methods</h2>
        <div class="containerhl1">
          <p>
          <b>Previous Method:</b> In the following video, even though the robot sees the goal in front of it, the previous method poorly predicts the final waypoint to the goal and fails.
          <br><span style="color: #ff0000">Failure</span>
          </p>
          <video id="dollyzoom" autoplay controls muted playsinline width="100%">
              <source src="/portfolio/vids/sling/nrns/RPmz2sHmrrY_457.mp4"
                      type="video/mp4">
          </video>
          <br>
          <p>
          <b>SLING:</b> However, SLING gives more accurate predictions of the relative pose to the goal, allowing it to succeed.
          <br><span style="color: #00ff00">Success</span>
          </p>
          <video id="dollyzoom" autoplay controls muted playsinline width="100%">
              <source src="/portfolio/vids/sling/sling/RPmz2sHmrrY_457.mp4"
                      type="video/mp4">
          </video>
        </div>
        </p>
      </div>
    </div>
  </div>
</section>


<section class="section" id="BibTeX">
<p align="left">
  <div class="containerjw">
    <h2 class="title">BibTeX</h2>
    <pre>
    <code>
@inproceedings{
wasserman2022lastmile,
title={Last-Mile Embodied Visual Navigation},
author={Justin Wasserman and Karmesh Yadav and Girish Chowdhary and Abhinav Gupta and Unnat Jain},
booktitle={6th Annual Conference on Robot Learning},
year={2022},
url={https://openreview.net/forum?id=RgJwDQwW82y}
}
    </code>
    </pre>
  </div>
</p>
</section>


<p>
<a
  href="https://github.com/nerfies/nerfies.github.io">Website source code</a>
</p>


