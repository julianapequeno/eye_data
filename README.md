## Working and studying EyeTracking with Tobii Pro Spark. 
> ### Project's development.
> I've been keeping my thoughts 💡, important links and daily improvements in these files: [project_development.md](documentation/project_development.md) and [notes.md](documentation/notes.md)



### Updates | HeatMap 

<img src='../eye_data/heatmap/data_collected/20240419.svg'>

Lately I'm focusing in trying new things with the data collected by the EyeTracker. Then, I decided to start by ploting a heatmap of the gaze vector. After some strugles - learning how to work with pandas - I finally get my first glimpse of the heatmaps! 

### Tobii Pro SDK
Before I got started I've got to install Tobii Pro SDK Kit and Tobii Pro EyeTracker Manager. 
For this project, I've imported all the files from SDK KIT, but you can choose other way to go. 

- I've followed this guideline for my fist script collecting data from the eyetracker: <https://developer.tobiipro.com/python/python-step-by-step-guide.html>
- Here's the first script: [<collecting_data_from_both_eyes.py>](collecting_data_from_both_eyes.py). Using Python, of course.

### Virtual Environment
I had to create a virtual environment for my project due to Debian's Linux distro adopting PEP 668 - Marking Python base environments as “externally managed”.
- Here's how:
```
    python3 -m venv .venv
    source .venv/bin/activate
```

### Installing Psychopy

For this, I had to install wxPython package before. As I'm using a Ubuntu 23.04 distro, I couldnt install directly from the page [wxPython/extras](https://extras.wxpython.org/wxPython4/extras/linux/gtk3/). It didnt exist any version that I could use from the moment that I did this. Then I simply built my own wxPython, following this instructions: [Building wxPython for Linux](https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html).

Though they recommend you installing all that packages before, I just had to install `gtk`. Like this:

```
sudo apt-get install libgtk-3-dev
```

After, I've runned the command:
```
pip install wxpython
```

Lastly and finally, the one:
```
pip install psychopy
```

### Outdoors - Psychopy
I suggest you installing TobiiProManager, it is free and you can get it in Tobii's site. It is very easy to install and to use. The manager could be very helpful for quick calibrations and verifications.

### Indoors - Psychopy

In order to connect Tobii Pro Spark Eyetracker with Psychopy, I installed tobii plug-in. The newest release of psychopy changed it from being built-in to being a plug-in. Here is package github's repository: [psychopy-eyetracker-tobii](https://github.com/psychopy/psychopy-eyetracker-tobii). Or you can just download on the application itself, here's a discussion about this that can help: https://discourse.psychopy.org/t/connect-to-eye-tracking-device/36423.




### Learning - Psychopy

For initial studies I've decided to learn more about Psychopy through this course: [Psychopy and Python](https://www.djmannion.net/psych_programming/vision/index.html)

