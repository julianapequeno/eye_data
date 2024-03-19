import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[400, 400],
    units="pix",
    fullscr=False,
    color=[1, 1, 1]
)

text = psychopy.visual.TextStim(
    win=win,
    text="Hello, world!",
    color=[-1, -1, -1]
)

text.draw()

win.flip()

psychopy.event.waitKeys()

win.close()
