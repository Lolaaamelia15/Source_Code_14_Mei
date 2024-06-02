import pigpio
from time import sleep

class Servo:
    def __init__(self) -> None:
        print("Initialize Servo")
        self.pi = pigpio.pi()
        self.servoPin = 13
        self.pi.set_servo_pulsewidth(self.servoPin, 0)

    def open(self):
        print("Pintu Terbuka")
        self.pi.set_servo_pulsewidth(self.servoPin, 1500)
        sleep(2)

    def close(self):
        print("Pintu Tertutup")
        self.pi.set_servo_pulsewidth(self.servoPin, 500)
        sleep(2)

    def stop(self):
        print("Stop Servo")
        self.pi.set_servo_pulsewidth(self.servoPin, 0)
        self.pi.stop()

if __name__ == "__main__":
    servo = Servo()
    servo.open()
    servo.close()
    servo.stop()

