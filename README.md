# Chat Spammer
Este  script automatiza el envío repetido de un mensaje en un chat o aplicación al mover el cursor a la posición del campo de entrada, escribir el mensaje y enviarlo, todo dentro de un bucle controlado por el número de repeticiones especificado.

Este script de Python utiliza la biblioteca PyAutoGUI para automatizar el envío repetitivo de mensajes en una ventana de chat. Es útil para probar aplicaciones de chat o para cualquier otro propósito en el que se necesite enviar un mensaje repetidamente.

## Requisitos

- Python 3.x
- PyAutoGUI

## Instalación

1. Clona este repositorio en tu máquina local:
   
   `"git clone https://github.com/tu_usuario/nombre_del_repositorio.git"`

3. Instala PyAutoGUI utilizando pip:
   


   `"pip install pyautogui"`


## Uso
Asegúrate de tener la ventana de chat abierta en la pantalla.
Ejecuta el script desde la línea de comandos:


   `"python chat_spammer.py"`


El script moverá el cursor al campo de entrada de texto y enviará el mensaje especificado repetidamente.

## Configuración
Puedes personalizar el mensaje a enviar y el número de repeticiones modificando las variables en el script así como la localización del "click":

-mensaje: El mensaje que se enviará.
-input_position: La posición del campo de entrada de texto en la pantalla.
-El número de repeticiones en el bucle for.

**Ten en cuenta** que este script está configurado para esperar 5 segundos antes de comenzar a enviar mensajes para que puedas prepararte. **Puedes ajustar este tiempo cambiando el valor pasado a time.sleep().**

Contribuciones
¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar este script, no dudes en abrir un issue o enviar una solicitud de extracción.

Notas
Este script está diseñado con fines educativos y de prueba. Úsalo con responsabilidad y no abuses de su funcionalidad.
Es posible que necesites ajustar las coordenadas del campo de entrada de texto (input_position) para que coincidan con la posición en tu pantalla.
Asegúrate de tener la ventana de chat activa y visible mientras se ejecuta el script.
mathematica
Copy code

Asegúrate de reemplazar `"tu_usuario/nombre_del_repositorio"` con la URL de tu repositorio en GitHub y ajustar cualquier otro detalle según sea necesario. ¡Espero que esto te sea útil!






