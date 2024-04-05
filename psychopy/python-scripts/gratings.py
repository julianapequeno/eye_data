import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[150, 150]
)

grating.draw()

win.flip()

print(psychopy.event.waitKeys(keyList=['tab','right','left']))

win.close()