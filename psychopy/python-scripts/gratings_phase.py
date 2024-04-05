import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[1000, 1000],
    units="pix",
    fullscr=True,
    color='#F5A2A2'
)

grating = psychopy.visual.GratingStim(
    win=win,
    units="pix",
    size=[280, 280]
)

grating_vpos = [150, 50, -50, -150]
grating_phase = [0.0, 0.30, 0.43, 0.75]

for i_phase in range(4):

    grating.phase = grating_phase[i_phase]

    grating.pos = [0, grating_vpos[i_phase]]

    grating.draw()

win.flip()

psychopy.event.waitKeys()

win.close()
