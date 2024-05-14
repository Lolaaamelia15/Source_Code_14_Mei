# from drivers import i2c_dev as driver
# from time import sleep
# display = driver.Lcd()
# display.lcd_clear()



# def tampil(jumlah_value=0, harga_value=0):
#     display.lcd_clear()
#     display.lcd_display_string(string="Jumlah: "+ str(jumlah_value), line = 1)
#     display.lcd_display_string(string="Harga: " + str(harga_value), line = 2)
#     sleep(10)

# tampil(10,100)
# from RPLCD.i2c import CharLCD
# import time

# lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2, dotsize=8)
# lcd.clear()

# def display(jumlah_value=0, harga_value=0):
#     lcd.clear()
#     lcd.write_string("Jumlah: {} \r\nHarga: {}".format(jumlah_value, harga_value))

# def stop():
#     lcd.clear()
#     lcd.close()


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

# display(19,199)