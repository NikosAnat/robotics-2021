import gpiozero
import tflite_runtime.interpreter as tflite

motor_RW = Motor()
motor_RB = Motor()
motor_LW = Motor() 
motor_LB = Motor() 
motor_CF = Motor()
sensorDist_REF = DistanceSensor(echo=18, trigger=17)
cameraman_CAM = PiCamera()

while(1):
    datetime = datetime.now().isoformat()
    photo = camera.capture('/home/pi/frame%03d.jpg' % frame)
    frame += 1
    x = neuroniko(photo)
    if x == 1 : 
    	motor_RB.forward(50)
        motor_RW.forward(50)
        motor_LB.backward(50)
        motor_LW.backward(50)

    if x == 2 : 
    	motor_RB.forward(50)
        motor_RW.forward(50)
        motor_LB.backward(50)
        motor_LW.backward(50)

    if x == 3 : 
    	motor_RB.forward(50)
        motor_RW.forward(50)
        motor_LB.backward(50)
        motor_LW.backward(50)

    if x == 4 : 
    	motor_RB.forward(50)
        motor_RW.forward(50)
        motor_LB.backward(50)
        motor_LW.backward(50)