from RPLCD import i2c
from time import sleep 

class LCD:
    def __init__(self) -> None:
        self.lcdmode = 'i2c'
        self.cols = 16
        self.rows = 2
        self.charmap = 'A00'
        self.i2c_expander = 'PCF8574'
        self.address = 0x27
        self.port = 1
        self.lcd = i2c.CharLCD(self.i2c_expander, self.address, port=self.port, charmap=self.charmap, cols=self.cols, rows=self.rows)

    def tampil(self, jumlah_value=0, harga_satuan=0):
        self.lcd.write_string("Jumlah: {}\r\nHarga: Rp{}".format(jumlah_value, harga_satuan*jumlah_value))
        sleep(15)
        self.lcd.close(clear=True)

if __name__ == "__main__":
    lcd = LCD()
    lcd.tampil(1000,5000)