import pigpio
from time import sleep

class Waterpump:
    def __init__(self) -> None:
        print("Initialize Waterpump")
        self.pi = pigpio.pi()
        self.waterpump_pin = 23
        self.pi.write(self.waterpump_pin, 0)

    def turn_on_waterpump(self):
        # Turn on the waterpump
        self.pi.write(self.waterpump_pin, 1)
        print("waterpump is ON")

    def turn_off_waterpump(self):
        # Turn off the waterpump
        self.pi.write(self.waterpump_pin, 0)
        print("waterpump is OFF")

    def stop(self):
        print("Stop waterpump")
        self.pi.write(self.waterpump_pin, 0)
        self.pi.stop()




# import RPi.GPIO as GPIO
# from time import sleep

# # Disable warnings (optional)
# GPIO.setwarnings(False)

# waterpump = 23
# def setup_gpio():
#     try:
#         # Periksa apakah GPIO sudah diatur sebelumnya
#         if GPIO.getmode() is None:
#             # Jika belum, atur mode GPIO
#             GPIO.setmode(GPIO.BCM)

#         # Set water pump - pin 23 as output 
#         # waterpump = 23
#         GPIO.setup(waterpump, GPIO.OUT)

#         return True
#     except Exception as e:
#         print(f"Error setting up GPIO: {e}")
#         return False

# # # Select GPIO mode
# # GPIO.setmode(GPIO.BCM)

# # #  Set waterpump - pin 23 as output 
# # waterpump = 23
# # GPIO.setup(waterpump, GPIO.OUT)

# def on():
#     GPIO.output(waterpump, GPIO.HIGH)
#     # sleep(5)

# def off():
#     GPIO.output(waterpump, GPIO.LOW)

#     # Cleanup and exit the program
# # GPIO.cleanup()

# # Periksa apakah pengaturan GPIO berhasil sebelum melanjutkan
# if setup_gpio():
#     # Contoh penggunaan
#     try:
#         on()  # Nyalakan pompa air selama 5 detik
#         sleep(2)
#         off()  # Matikan pompa air
#     except KeyboardInterrupt:
#         # Tangani interrupt keyboard (Ctrl+C)
#         pass
#     finally:
#         # Pastikan pembersihan GPIO dilakukan sebelum keluar
#         GPIO.cleanup()