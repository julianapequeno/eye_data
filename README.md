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