import pyautogui as pg
import time

# Calcula la posición del input fuera del bucle
input_position = (1598, 991)

# Escribe el mensaje una vez
mensaje = "Escribe tu mensaje en este string"

# Espera unos segundos antes de comenzar el script (opcional)
# time.sleep(5)

time.sleep(5)

# Repite el envío del mensaje 150 veces
for _ in range(150):
    # Mueve el cursor al input
    pg.moveTo(input_position)
    
    # Escribe el mensaje en el chat
    pg.typewrite(mensaje, interval=0.01)  # intervalo opcional para simular la velocidad de escritura
    
    # Envía el mensaje en el chat
    pg.press('enter')
    
    # Reduce el tiempo de espera entre iteraciones
    time.sleep(0.1)

