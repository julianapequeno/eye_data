import time
from tobiiresearch.implementation import EyeTracker, ScreenBasedCalibration

var = EyeTracker.find_all_eyetrackers()
my_eyetracker = var[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

def gaze_data_callback(gaze_data):
    # Print gaze points of left and right eye
    print("Left eye: ({gaze_left_eye}) \t Right eye: ({gaze_right_eye})".format(
        gaze_left_eye=gaze_data['left_gaze_point_on_display_area'],
        gaze_right_eye=gaze_data['right_gaze_point_on_display_area']))

# para que o SDK saiba que deve chamar a funcao acima toda vez que houver nova data 
my_eyetracker.subscribe_to(EyeTracker.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
#deixa o programa printar a data por um tempo
time.sleep(5)
#unsubscribe dizendo que terminamos
my_eyetracker.unsubscribe_from(EyeTracker.EYETRACKER_GAZE_DATA, gaze_data_callback)


calibration = ScreenBasedCalibration.ScreenBasedCalibration(var[0])
print(calibration)


def calibration_func():
    # Enter calibration mode.
    calibration.enter_calibration_mode()
    print ("Entered calibration mode for eye tracker with serial number {0}.".format(var[0].serial_number))

    # Define the points on screen we should calibrate at.
    # The coordinates are normalized, i.e. (0.0, 0.0) is the upper left corner and (1.0, 1.0) is the lower right corner.
    points_to_calibrate = [(0.5, 0.5), (0.1, 0.1), (0.1, 0.9), (0.9, 0.1), (0.9, 0.9)]
    for point in points_to_calibrate:
        print("Show a point on screen at {0}.".format(point))
            # Wait a little for user to focus.
        time.sleep(0.7)
        print ("Collecting data at {0}.".format(point))
    if calibration.collect_data(point[0], point[1]) != ScreenBasedCalibration.CALIBRATION_STATUS_SUCCESS:
        # Try again if it didn't go well the first time.
        # Not all eye tracker models will fail at this point, but instead fail on ComputeAndApply.
            calibration.collect_data(point[0], point[1])
    print ("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print  ("Compute and apply returned {0} and collected at {1} points.".\
            format(calibration_result.status, len(calibration_result.calibration_points)))

    # Analyze the data and maybe remove points that weren't good.
    recalibrate_point = (0.1, 0.1)
    print ("Removing calibration point at {0}.".format(recalibrate_point))
    calibration.discard_data(recalibrate_point[0], recalibrate_point[1])

    # Redo collection at the discarded point
    print ("Show a point on screen at {0}.".format(recalibrate_point))
    calibration.collect_data(recalibrate_point[0], recalibrate_point[1])


    # Compute and apply again.
    print ("Computing and applying calibration.")
    calibration_result = calibration.compute_and_apply()
    print ("Compute and apply returned {0} and collected at {1} points.".\
        format(calibration_result.status, len(calibration_result.calibration_points)))


    # See that you're happy with the result.
    # The calibration is done. Leave calibration mode.
    calibration.leave_calibration_mode()
    print ("Left calibration mode.")