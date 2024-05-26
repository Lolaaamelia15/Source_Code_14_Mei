from RPLCD import i2c
from time import sleep 

lcdmode = 'i2c'
cols = 16
rows = 2
charmap = 'A00'
i2c_expander = 'PCF8574'

address = 0x27
port = 1

lcd = i2c.CharLCD(i2c_expander, address, port=port, charmap=charmap, cols=cols, rows=rows)

def tampil(jumlah_value=0, harga_value=0):
    lcd.write_string("Jumlah: {} \r\nHarga: {}".format(jumlah_value, harga_value))
    sleep(15)

    lcd.close(clear=True)

# tampil(20,100)