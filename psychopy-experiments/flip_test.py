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

print(psychopy.event.waitKeys())

win.flip()
#we didnt add anything after the flip(), then it wont appear at a second time.
print(psychopy.event.waitKeys())

win.close()
