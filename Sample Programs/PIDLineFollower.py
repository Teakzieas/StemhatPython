import stemhat
import time


print("Press Button 5 to start and stop the robot")

while True:
    stemhat.SetMotors(0, 0)
    
    while not stemhat.GetButton(5):
        pass
    time.sleep(0.5)
    intergral = 0
    last_error = 0
    while True:
        # Read the light sensor
        sensor = stemhat.GetAnalog(0)

        # Calculate the error
        error = 122.5 - sensor
        # calculate the proportional
        proportional = error * 0.3
        # Calculate the intergral
        intergral = intergral + error * 0
        # Calculate the derivative
        derivative = (error - last_error) * 0.2
        # Calculate the output
        correction = proportional + intergral + derivative
        # Save the error
        last_error = error


        # Limit the correction
        if(correction > 20):
            correction = 20
        if(correction < -20):
            correction = -20
        
        # Set the motors
        stemhat.SetMotors(80-correction, 80+correction)



        if(stemhat.GetButton(5)):
            time.sleep(0.5)
            break

     


  