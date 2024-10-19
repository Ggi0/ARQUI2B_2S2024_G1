import smbus
import time

# Inicializa el bus I2C
bus = smbus.SMBus(1)
arduino_address = 0x08  # Direcci�n I2C del Arduino

def send_two_numbers(high_number, low_number):
    # Asegurarse de que los n�meros est�n dentro del rango de un byte (0-255)
    high_byte = high_number & 0xFF
    low_byte = low_number & 0xFF
    
    # Enviar los dos bytes (uno para el high byte y otro para el low byte)
    bus.write_i2c_block_data(arduino_address, 1, [high_byte, low_byte])

# Enviar dos n�meros (por ejemplo, 200 y 55)
send_two_numbers(1, 55)
time.sleep(1)
