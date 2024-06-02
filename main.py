# Import module 
import requests
import new_detect
from time import sleep
from servo import Servo
from buzzer import Buzzer
from lcd import LCD
from datetime import datetime
import cProfile 

servo = Servo()
buzzer = Buzzer()
lcd = LCD()

while(True):
    try:
        date = datetime.now()
        print(f"{date} : getting status..")
        response = requests.get('https://fishcounterta.000webhostapp.com/status.php')
        if response.status_code == 404:
            print("404 Not Found")
            continue

        response_json = response.json()

        # Mengekstrak nilai dari JSON
        # id_value = response_json['id']
        hitung_status = response_json['hitung']

        if hitung_status == 'true':
            jumlah_value = int(response_json['jumlah'])
            harga_value = int(response_json['harga'])
            
            jumlah_ikan = 0
            while (jumlah_ikan < jumlah_value):
                servo.close()             # Matikan servo
                jumlah_ikan += new_detect.count(interval=25, total_terdetect=jumlah_ikan) # call hitung
                servo.open()                # Hidupkan servo
                sleep(5) # waktu untuk mengeluarkan ikan
            
            new_detect.stopProgram()
            print("Total ikan yang terdeteksi : {}".format(jumlah_ikan))
            buzzer.turn_on_buzzer()
            lcd.tampil(jumlah_value=jumlah_value,harga_satuan=harga_value)

            # reset table status
            x = requests.post('https://fishcounterta.000webhostapp.com/status.php') 
            print(x.json())

    except KeyboardInterrupt:
        servo.stop()
        buzzer.stop()
        break
    
    except ConnectionError as errcon:
        print(errcon.args)

    # except Exception as e:
    #     print(e.args)
        
    finally:
        sleep(3)
