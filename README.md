## Working and studying EyeTracking with Tobii Pro Spark. 

Before I got started I've got to install Tobii Pro SDK Kit and Tobii Pro EyeTracker Manager. 
For this project, I've imported all the files from SDK KIT, but you can choose other way to go. 

- I've followed this guideline: <https://developer.tobiipro.com/python/python-step-by-step-guide.html>
- Using Python, of course.


1. The Beggining - Collecting data from eyetracker. [<collecting_data_from_both_eyes.py>](collecting_data_from_both_eyes.py)


### Project's development.
I've been keeping my thoughts, important links and daily improvements in these files: [project_development.md](project_development.md) and [notes.md](notes.md)

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