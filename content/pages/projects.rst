Projects
===============

:date: 2015-01-07 11:38
:modified: 2015-01-07 11:38
:tags: projects

Below is a list of software projects I have been involved with.

Visual3D
-----------------
In my first summer in graduate school at UF, with the help of one of my committee members, I landed an internship at the Physical Disabilities Branch at the NIH. There I had the priveledge of working with some great people on a great biomechanics/motion capture tool called Visual3D_. My internship started with tracking down a fairly tricky bug. While it was a real bug, it was also a bit of a test to make sure their new intern actually knew what he was doing! Once I found and fixed it, I was given the reigns to implement a new technique to calculate the 6D pose of body segments from the available marker data. 

For those interested in the details, at the time the only available method in Visual3D to reconstruct segment motion from marker data was to treat each body on which markers were placed as independent from every other body. In other words, the calculations assumed that each body with markers on it simply floated around in 6D space. In actuality bodies are often human body segments which have geometric constraints with other bodies (e.g. a knee joint between the thigh and shank). Because the calculations were not aware of these constraints, you would often see odd artifacts in the reconstructed segment motion (e.g. the shank 'bouncing' around relative to the foot and thigh on ankle impact). Several authors had addressed this issue in the literature at the time, so I took those published methods and wrote a plugin for Visual3D that implemented one of them.

I don't know whether the plugin made it into the commercial product but when I left my internship I had implemented 'constraint-aware' motion reconstruction algorithm.

.. _Visual3D: http://www.c-motion.com/products/visual3d/

JointTrack
-----------------
.. image:: {filename}/images/joint_track.jpg 
    :alt: JointTrack
    :align: right
    :width: 200px

JointTrack_ was the first major application that I authored. And my earlier work at NIH, it has been my only major foray into user-facing software design. As an interesting side note, JointTrack was probably going the be the foundation for my Ph.D. thesis work---that is until I abrubtly changed course into the robotics side of our lab about a year into this project (and good thing I did!).

JointTrack stemmed from some earlier software written by my advisor in `PV-WAVE`_ that would register 3D models of bones and joint implants to their single or bi-plane X-Ray images. If you had a series of X-Ray images taken from someone doing an activity (e.g. images of their knee during walking), you could measure (fairly precisley) the bone kinematics during that activity. JointTrack was an attempt to modernize his original software and I did that by writing it from scratch in, at that time, Microsoft's state-of-the-art MFC.

I learned a ton from this project: the vaunted Model-View-Controller pattern and software pattens in general, object-oriented design, modern UI design, and plugin frameworks. When I handed over development to one of my lab mates (`Shang Mu`_), I had developed a completely functional application in which you could pair different cost functions with various local optimizers (and possibly even a global optimizer.. can't remember) to solve the problem of registering models to their 2D projections.

.. _JointTrack: http://sourceforge.net/projects/jointtrack/
.. _PV-WAVE: http://www.roguewave.com/products-services/pv-wave
.. _Shang Mu: https://www.linkedin.com/in/shangmu

DRICS
-----------------
.. image:: {filename}/images/drics_logo.png 
    :alt: DRICS logo
    :align: right
    :width: 200px

DRICS or Dynamic Radiographic Imaging Control Software was my first ever large scale project to implement a real-time control framework for a robotic hardware system. Well that's not quite true. I believe the first ever attempt was a Windows-based application written by my then lab-mate and I to control the PA-106CE largely via manufacturer provided Windows' SDKs. We very quickly outgrew our initial source file. It turned into several files with functions and code that became completely unmanagable. But I learned some valuable lessons from this first attempt - things like the need for great version control tools and 

Since I left UF, the students there (very wisely) moved on from the low-level approach I 

https://drics.googlecode.com/svn/

TinySG
-----------------
.. image:: {filename}/images/tinysg_example.png 
    :alt: DRICS logo
    :align: right
    :width: 200px

Tiny Scene Graph (TinySG_) was my `second attempt`_ at rolling my own lightweight scene graph. At the time I wrote it, I thought things like OpenSG_ were just too complicated for what I needed and other excellent libraries like rbdl_ did not exist yet (although even rbdl would not have quite fit what I needed). Plus I was fairly young and eager to learn more about programming.

What did it do? Well I wrote it to solve a problem I faced in my thesis: I needed to quickly calculate the minimum disntance between objects. My CS colleage at the time (`Zach Ezzell`_) helped me select a good algorithm, Lin-Canny, for fast and efficient distance calculations [lincanny91]_. But the algorithm was only half the problem. I needed to run this algorithm on a couple dozen bodies and the relationship of those bodies needed to be fairly flexible to define - perfect job for a scene graph!

I thought there were some good ideas there. I worked up a fairly slick Matlab integration (albeit using the fairly esoteric `X Macro`_), collision queries via ODE_, a plugin architecture that made the whole library fairly extensible, support for forward kinematics, and had begun Python integration (but not sure I ever finished it..). In my spare time (ha!), I would really like to jump back into TinySG and apply everything I have learned since 2008!

.. _TinySG: https://github.com/yamokosk/tinysg
.. _second attempt: https://code.google.com/p/sceneml/
.. _OpenSG: http://www.opensg.org/
.. _rbdl: http://rbdl.bitbucket.org/
.. _Zach Ezzell: https://www.linkedin.com/pub/zach-ezzell/24/717/566
.. [lincanny91] M Lin and J Canny. *A fast algorithm for incremental distance calculation.* In IEEE Conference on Robotics and Automation, pp. 1008-1014, 1991.
.. _X Macro: http://en.wikipedia.org/wiki/X_Macro
.. _ODE: http://www.ode.org/

@NASA
-----------------
I have had the privledge of working in the Dexterous Robotics Laboratory (DRL) here at NASA/Johnson Space Center since graduating from UF in 2009. All of the projects I worked on graudate school were excellent preparation for the work I have been doing in the DRL. That has included more system design of real-time control systems and efficient algorithm implementations. Specifically I have worked on getting Robonaut 2 ready for it flight to the International Space Station and was the lead software designer on Valkyrie - JSC's entry into the DARPA Robotics Challenge. Those are the highlights - of course there has been a *lot* of coding efforts scattered around those efforts.. too many to list here.

.. image:: {filename}/images/robonaut2.jpg 
    :alt: DRICS logo
    :align: left
    :height: 200px

.. image:: {filename}/images/NASA-valkyrie.jpg 
    :alt: DRICS logo
    :align: right
    :height: 200px    