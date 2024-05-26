# Import module 
import requests
import json
import new_detect
from time import sleep
from servo import Servo
# from buzzer import Buzzer
# from waterpump import Waterpump
import lcd

servo = Servo()
# waterpump = Waterpump()
# buzzer = Buzzer()

while(True):

    try:
    #     print("getting status..")
    #     x = requests.get('https://fishcounterta.000webhostapp.com/status.php')
    #     response_json = x.json()

    #     # Mengekstrak nilai dari JSON
    #     # id_value = response_json['id']
    #     hitung_status = response_json['hitung']

    #     if hitung_status == 'true':
    #         jumlah_value = int(response_json['jumlah'])
    #         harga_value = int(response_json['harga'])
            

            # waterpump.on()              # Hidupkan waterpump
            jumlah_value = 5
            harga_value = 100
            jumlah_ikan = 0
            while (jumlah_ikan < jumlah_value):
                servo.close()             # Matikan servo
                jumlah_ikan += new_detect.count(interval=25, total_terdetect=jumlah_ikan) # call hitung
                servo.open()                # Hidupkan servo
                sleep(5) # waktu untuk mengeluarkan ikan
            
            new_detect.stopProgram()
            print("Total ikan yang terdeteksi : {}".format(jumlah_ikan))
            lcd.tampil(jumlah_value=jumlah_value,harga_value=harga_value*jumlah_value)
            break
            # waterpump.off()           # Matikan waterpump
            # buzzer.setup_gpio()
            # buzzer.hidup()            # Bunyikan buzzer
            

            # print(jumlah_value*harga_value) # Print harga total di terminal

            # reset table status
            # x = requests.post('https://fishcounterta.000webhostapp.com/status.php') 
            # print(x.json())

    except KeyboardInterrupt:
        # waterpump.off()
        # servo.close()
        # lcd.close()
        break

    # except Exception as e:
        # waterpump.off()
        # servo.close()
        # lcd.close()
        # print(e.args)
        
    finally:
        sleep(3)
