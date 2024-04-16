from psychopy.iohub import launchHubServer
from psychopy.core import getTime, wait
import time
from tobiiresearch.implementation import EyeTracker, ScreenBasedCalibration

var = EyeTracker.find_all_eyetrackers()
my_eyetracker = var[0]

def gaze_data_callback(gaze_data):
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))
    
# para que o SDK saiba que deve chamar a funcao acima toda vez que houver nova data 
my_eyetracker.subscribe_to(EyeTracker.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
#deixa o programa printar a data por um tempo
time.sleep(5)
#unsubscribe dizendo que terminamos
my_eyetracker.unsubscribe_from(EyeTracker.EYETRACKER_GAZE_DATA, gaze_data_callback)