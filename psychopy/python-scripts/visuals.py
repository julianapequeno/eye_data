import psychopy.visual as pv
import psychopy.event as pe
import psychopy.iohub as iohub
from psychopy.iohub import launchHubServer

win = pv.Window(
    size=[400,400],
    units="pix",
    fullscr=False,
    color=[1,1,1]
)

text = pv.TextStim(
    win=win,
    text='Hello World',
    color=[-1,-1,-1]
)

# From your script
io = launchHubServer()  
# get the keyboard device
iokeyboard = io.devices.keyboard


text.draw()

win.flip()

iokeyboard.waitForPresses(keys=[' '], clear=True)

win.close()
