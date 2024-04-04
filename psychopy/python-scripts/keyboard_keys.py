import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)


keys = psychopy.event.waitKeys(keyList=["left", "right"])
 #it just finish when the user press some of these keys 

win.close()