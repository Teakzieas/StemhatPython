import time
import stemhat
import os

# Test LEDs
print("Testing LEDs...")
stemhat.SetLED(0, 255, 0, 0)  # Red
stemhat.SetLED(1, 0, 255, 0)  # Green

time.sleep(1)
stemhat.SetLED(0, 0, 0, 255)  # Blue
stemhat.SetLED(1, 255, 255, 255)  # White

time.sleep(1)
stemhat.SetLED(0, 0, 0, 0)
stemhat.SetLED(1, 0, 0, 0)

# Test Buzzer
print("Testing Buzzer...")
stemhat.SetBuzzer(1000)
time.sleep(1)
stemhat.SetBuzzer(0)

# Test Motors
print("Testing Motors...")
stemhat.SetMotors(50, 50)
time.sleep(1)
stemhat.SetMotors(-50, -50)
time.sleep(1)
stemhat.SetMotors(0, 0)

# Test Servos
print("Testing Servos...")
for angle in range(0, 181, 45):
    stemhat.SetServo(1, angle)
    stemhat.SetServo(2, angle)
    stemhat.SetServo(3, angle)
    stemhat.SetServo(4, angle)
    time.sleep(0.5)

# Test Sensors
print("Reading Sensors...")
print(f"Analog 0: {stemhat.GetAnalog(0)}")
print(f"Analog 1: {stemhat.GetAnalog(1)}")
print(f"Light Sensor: {stemhat.GetLightSensor()}")
print(f"Voltage: {stemhat.GetVoltage()}")
print(f"Temperature: {stemhat.GetTemperature()} C")
print(f"Humidity: {stemhat.GetHumidity()} %")
print(f"Ultrasonic: {stemhat.GetUltrasonic()}")

# Test Buttons
print("Testing Buttons...")
print("Press Button 5")
while True:
    if stemhat.GetButton(5):
        print("Button 5 Pressed - Testing LED")
        stemhat.SetLED(0, 255, 0, 0)  # Red
        time.sleep(1)
        stemhat.SetLED(0, 0, 0, 0)
        break
    time.sleep(0.1)

print("Press Button 6")
while True:
    if stemhat.GetButton(6):
        print("Button 6 Pressed - Testing Buzzer")
        stemhat.SetBuzzer(1000)
        time.sleep(1)
        stemhat.SetBuzzer(0)
        break
    time.sleep(0.1)

# Test OLED Display
print("Testing OLED Display...")
stemhat.OledClear()
stemhat.OledText(0, 0, "Hello World!", 10,1)
stemhat.OledRectangle(5, 5, 20, 50, 0, 1)
stemhat.OledLine(0, 0, 50, 30)
stemhat.OledPoint(20, 20, 1)
stemhat.OledCircles(40, 20, 10, 1, 1)
stemhat.OledUpdate()

time.sleep(3)

stemhat.OledClear()
stemhat.OledUpdate()
stemhat.OledClear()
script_dir = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(script_dir,"2.bmp")
stemhat.OledImage(0,0,image,1,1)
stemhat.OledUpdate()


# Reset stemhat
print("Resetting stemhat...")
stemhat.SetLED(1, 255, 255, 255)  # White
time.sleep(3)
stemhat.Reset()

stemhat.OledCircles(40, 20, 10, 1, 1)
stemhat.OledUpdate()
stemhat.OledScroll(1,7,0,7)
time.sleep(3)
stemhat.OledScrollStop()

x=3
while x==1:
    stemhat.APDSsetMode(1)
    proximity = stemhat.APDSread_proximity()
    print(proximity)
    time.sleep(0.1)

while x==2:
    stemhat.APDSsetMode(2)
    gesture = stemhat.APDSread_gesture()
    if gesture:
        print(f"Gesture detected: {gesture}")
    time.sleep(0.5)
    
while x==3:
    stemhat.APDSsetMode(3)
    color = stemhat.APDSread_color()
    if color:
        print(f"Color detected: R={color[0]}, G={color[1]}, B={color[2]}, Clear={color[3]}")
    time.sleep(0.1)


print("Test Complete!")
