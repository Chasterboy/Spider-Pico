import machine
import utime

# Configura los pines GPIO para controlar los servos de cada pata
pata1_servo_pin_1 = machine.Pin(2)
pata1_servo_pin_2 = machine.Pin(3)
pata1_servo_pin_3 = machine.Pin(12)

pata2_servo_pin_1 = machine.Pin(4)
pata2_servo_pin_2 = machine.Pin(5)
pata2_servo_pin_3 = machine.Pin(13)

pata3_servo_pin_1 = machine.Pin(6)
pata3_servo_pin_2 = machine.Pin(7)
pata3_servo_pin_3 = machine.Pin(14)

pata4_servo_pin_1 = machine.Pin(8)
pata4_servo_pin_2 = machine.Pin(9)
pata4_servo_pin_3 = machine.Pin(15)

# Configura el objeto PWM para cada servo de cada pata
pata1_servo_1 = machine.PWM(pata1_servo_pin_1)
pata1_servo_2 = machine.PWM(pata1_servo_pin_2)
pata1_servo_3 = machine.PWM(pata1_servo_pin_3)

pata2_servo_1 = machine.PWM(pata2_servo_pin_1)
pata2_servo_2 = machine.PWM(pata2_servo_pin_2)
pata2_servo_3 = machine.PWM(pata2_servo_pin_3)

pata3_servo_1 = machine.PWM(pata3_servo_pin_1)
pata3_servo_2 = machine.PWM(pata3_servo_pin_2)
pata3_servo_3 = machine.PWM(pata3_servo_pin_3)

pata4_servo_1 = machine.PWM(pata4_servo_pin_1)
pata4_servo_2 = machine.PWM(pata4_servo_pin_2)
pata4_servo_3 = machine.PWM(pata4_servo_pin_3)

# Define la frecuencia de la señal PWM (ajusta esto según sea necesario para tus servos)
pwm_frequency = 50  # Puedes probar con valores entre 50 y 100 Hz

# Inicializa los servos con una señal de 90 grados
pata1_servo_1.freq(pwm_frequency)
pata1_servo_2.freq(pwm_frequency)
pata1_servo_3.freq(pwm_frequency)

pata2_servo_1.freq(pwm_frequency)
pata2_servo_2.freq(pwm_frequency)
pata2_servo_3.freq(pwm_frequency)

pata3_servo_1.freq(pwm_frequency)
pata3_servo_2.freq(pwm_frequency)
pata3_servo_3.freq(pwm_frequency)

pata4_servo_1.freq(pwm_frequency)
pata4_servo_2.freq(pwm_frequency)
pata4_servo_3.freq(pwm_frequency)

# Función para mover cada pata a una posición específica en grados
def move_pata1_servos(degrees_1, degrees_2, degrees_3):
    # Convierte el ángulo en grados a un valor de ciclo de trabajo en nanosegundos
    duty_ns_1 = int(500000 + (degrees_1 * 1000000 / 180))
    duty_ns_2 = int(500000 + (degrees_2 * 1000000 / 180))
    duty_ns_3 = int(500000 + (degrees_3 * 1000000 / 180))

    pata1_servo_1.duty_ns(duty_ns_1)
    pata1_servo_2.duty_ns(duty_ns_2)
    pata1_servo_3.duty_ns(duty_ns_3)

def move_pata2_servos(degrees_1, degrees_2, degrees_3):
    duty_ns_1 = int(500000 + (degrees_1 * 1000000 / 180))
    duty_ns_2 = int(500000 + (degrees_2 * 1000000 / 180))
    duty_ns_3 = int(500000 + (degrees_3 * 1000000 / 180))

    pata2_servo_1.duty_ns(duty_ns_1)
    pata2_servo_2.duty_ns(duty_ns_2)
    pata2_servo_3.duty_ns(duty_ns_3)

def move_pata3_servos(degrees_1, degrees_2, degrees_3):
    duty_ns_1 = int(500000 + (degrees_1 * 1000000 / 180))
    duty_ns_2 = int(500000 + (degrees_2 * 1000000 / 180))
    duty_ns_3 = int(500000 + (degrees_3 * 1000000 / 180))

    pata3_servo_1.duty_ns(duty_ns_1)
    pata3_servo_2.duty_ns(duty_ns_2)
    pata3_servo_3.duty_ns(duty_ns_3)

def move_pata4_servos(degrees_1, degrees_2, degrees_3):
    duty_ns_1 = int(500000 + (degrees_1 * 1000000 / 180))
    duty_ns_2 = int(500000 + (degrees_2 * 1000000 / 180))
    duty_ns_3 = int(500000 + (degrees_3 * 1000000 / 180))

    pata4_servo_1.duty_ns(duty_ns_1)
    pata4_servo_2.duty_ns(duty_ns_2)
    pata4_servo_3.duty_ns(duty_ns_3)

# Bucle principal: Mueve las patas para simular el ciclo de caminar
while True:
    # Paso 1: Posición inicial de las patas (todas las articulaciones a 0 grados o cerca de 0 grados)
    move_pata1_servos(0, 0, 0)
    move_pata2_servos(0, 0, 0)
    move_pata3_servos(0, 0, 0)
    move_pata4_servos(0, 0, 0)
    utime.sleep(0.5)  # Espera 0.5 segundos para que los servos alcancen la posición

    # Paso 2: Simula la posición de "pata baja" (bajando la articulación de la tibia)
    move_pata1_servos(30, 20, 30)
    move_pata2_servos(30, 20, 30)
    move_pata3_servos(30, 20, 30)
    move_pata4_servos(30, 20, 30)
    utime.sleep(0.5)

    # Paso 3: Simula la posición de "fémur" (articulación del fémur) al elevar las patas
    move_pata1_servos(60, 60, -30)
    move_pata2_servos(60, 60, -30)
    move_pata3_servos(60, 60, -30)
    move_pata4_servos(60, 60, -30)
    utime.sleep(0.5)

    # Paso 4: Simula la unión al cuerpo (coxa) de las patas, ajustando la posición del tercer servo
    move_pata1_servos(30, 60, -60)
    move_pata2_servos(30, 60, -60)
    move_pata3_servos(30, 60, -60)
    move_pata4_servos(30, 60, -60)
    utime.sleep(0.5)

    # Vuelve a la posición inicial para prepararse para el siguiente ciclo de caminar
    move_pata1_servos(0, 0, 0)
    move_pata2_servos(0, 0, 0)
    move_pata3_servos(0, 0, 0)
    move_pata4_servos(0, 0, 0)
    utime.sleep(0.5)
