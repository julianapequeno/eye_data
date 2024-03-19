import psychopy.visual
import psychopy.event
import psychopy.core

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False
)

clock = psychopy.core.Clock()

text = psychopy.visual.TextStim(win=win)

grating = psychopy.visual.GratingStim(
    win=win,
    size=[200, 200],
    mask="circle",
    units="pix",
    sf=5.0 / 200.0
)

text.text = "Press any key to show the grating"

text.draw()

win.flip()

psychopy.event.waitKeys()

clock.reset()

while clock.getTime() < 0.5:
    grating.draw()
    win.flip()

text.text = "Press any key to finish"

text.draw()

win.flip()

psychopy.event.waitKeys()

win.close()
