<h1 style="text-align: center;">ADQUISICIÓN DE SEÑALES Y GRAFICACIÓN EN ARDUINO - GRUPO 2</h1>


</h3>Nombre de los Integrantes y código:
</h3>1.Melany Cama Bahamonde 72128361
</h3>2.Alessandra Valle Montoya  71098563
</h3>3.Catherine Boggio Vidal
</h3>4.Juan Jose Sandoval Barrantes 74145560



<h2 style="text-align: center;">Tabla de Contenidos</h2>

1. [Plotear señales en Arduino IDE provenientes del generador de señales](#Ploteo)
2. [Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio](#Comparar)
3. [Arduino Cloud](#Arduino)
4. [Docentes](#Docentes)
5. [Referencias](#Referencias)

<a id = "Ploteo" style></a>
<h2 style = "text-align: center;">Plotear señales en Arduino IDE provenientes del generador de señales</h2>

En el proceso para plotear una señal en Arduino, se utilizó el puerto analógico del Arduino nano 33 IoT, un generador de señales y se armó un pequeño circuito en un protoboard con un capacitor de 470uF en tierra y el pin como se puede observar en la figura 1.

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/circuito.png">
</p>
<h5 align="center">
  Figura [1]: Circuito armado
</h5>
</p>
</p>

En primer lugar, creamos las señales y verificamos que el voltaje generado por la onda no excediera los 3.3V, con el fin de proteger el Arduino Nano 33 IoT de posibles daños. Este proceso lo llevamos a cabo utilizando un osciloscopio digital. Sin embargo, es importante tener en cuenta que el cable de conexión al osciloscopio (BNC) que hemos utilizado opera con una atenuación de x10 [1].

Al observar la señal generada en el osciloscopio, nos dimos cuenta de que esta estaba siendo reducida diez veces debido a la atenuación del cable, como se muestra en la Figura 2. Esto nos permitió asegurarnos de que el voltaje aplicado al Arduino se mantuviera dentro de los límites seguros, evitando así cualquier posible daño al dispositivo.


<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/atenuacion.png">
</p>
 <h5 align="center">
Figura [2]: Demostración de la atenuación x10 del cable de osciloscopio BNC
 </h5>
</p>
</p>
Posteriormente, procedimos a desarrollar el código necesario para la lectura de la señal en Arduino. Antes de esto, es crucial descargar la librería SANDBoards para garantizar el funcionamiento adecuado del programa.

El objetivo principal del código es variar la frecuencia de la señal, así como la frecuencia de muestreo y el voltaje. Estos parámetros son esenciales para nuestra investigación y se pueden observar claramente en las Figuras 3 a 8.
Se debe tener en cuenta que las frecuencias que se toman son bajas debido a las limitaciones de velocidad del reloj, capacidad de procesamiento y diseño de la placa [1].

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/codig1.png">
</p>
<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/codig2.png">
</p>
 <h5 align="center">
Figura [3]: Código en Arduino
     </h5>
</p>
</p>

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/señal1.jpeg">
</p>
 <h5 align="center">
Figura [4]: Señal 1 Sinusoidal con amplitud 1V, frecuencia de 2Hz y Fmuestreo=5*F, sin capacitor
     </h5>
</p>
</p>

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/señal%202Hz%20sin.jpeg">
</p>
 <h5 align="center">
Figura [5]: Señal 2 Sinusoidal con amplitud 2.5V, frecuencia de 2Hz y Fmuestreo=10*F, sin capacitor
     </h5>
</p>
</p>

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/5HzSin.jpg">
</p>
 <h5 align="center">
Figura [6]: Señal 3 Sinusoidal con amplitud 2.5V, frecuencia de 5Hz y Fmuestreo=5*F, sin capacitor
     </h5>
</p>
</p>

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/Con2Hz.jpg">
</p>
 <h5 align="center">
Figura [7]: Señal 4 Sinusoidal con amplitud 2V, frecuencia de 2Hz y Fmuestreo=5*F, CON capacitor
     </h5>
</p>
</p>

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/Con5hz.jpg">
</p>
 <h5 align="center">
Figura [8]: Señal 5 Sinusoidal con amplitud 2V, frecuencia de 5Hz y Fmuestreo=5*F, CON capacitor
     </h5>
</p>
</p>

La presencia del capacitor en el circuito puede tener un impacto tanto en la reducción del ruido no deseado como en la disminución de la amplitud de la señal deseada. 

Cuando hablamos de un circuito donde se introduce un capacitor, como en un circuito RC (Resistencia-Capacitor), la presencia de este componente puede afectar la señal eléctrica. Este circuito atenúa o reduce el ruido no deseado que pueda estar presente en la señal, es decir, funciona como un filtro de componentes no deseados. Sin embargo, el capacitor también puede afectar la señal útil, dependiendo de la frecuencia de la señal y del valor del capacitor, este componente puede influir en cómo la señal se carga y descarga a través del circuito. En algunos casos, esto puede provocar una disminución en la amplitud de la señal deseada [2].

<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/rc.jpeg">
</p>
 <h5 align="center">
Figura [9]: Circuito RC 
</p>

<a id = "Comparar"></a>  
<h2 style = "text-align: center;">Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio</h2>
<p align="center">
  <img width="660" height="400" src="https://github.com/Melanyccb11/Intro_senales/blob/main/Im%C3%A1genes/compara.png">
</p>


Observaciones:
- Se ha logrado obtener gráficas a partir de la configuración del generador de señal (sinusoidal) en donde se ha ido variando la frecuencia entre 1-2Hz. 
- Se puede observar que, en la primera gráfica del arduino bajo una frecuencia de 2Hz se ve una señal recortada, esto debido a que la señal parece recortada porque la tensión de salida del generador de funciones excede el rango máximo de entrada del convertidor analógico a digital (ADC) de tu Arduino, que es de 5V. Al superar este límite, las partes de la señal que están por encima de 5V no se leen correctamente, lo que resulta en una señal recortada en la gráfica.
- Por otro lado, en la siguiente imagen la gráfica de Arduino ahora muestra una señal definida porque el voltaje de la señal del generador está dentro del rango que el Arduino puede leer sin recortar, y la configuración del ADC está correctamente ajustada para capturar toda la amplitud de la señal.



<a id = "Arduino"></a>
<h2 style = "text-align: center;">Arduino Cloud</h2>


<a id = "Docentes"></a>
<h2 style = "text-align: center;">Docentes del Curso</h2>

1. De la Cruz Rodriguez, Lewis - umbert.de.la.cruz@upch.pe
2. Meza Rodriguez, Moises - moises.meza@upch.pe
3. Venancio Huerta, Julissa - julissa.venancio@upch.pe
4. Cáceres del Aguila, Jose Alonso - jose.caceres.d@upch.pe

<a id = "Referencias"></a>
<h2 style = "text-align: center;">Referencias</h2>
[1]«Arduino Nano 33 IoT — Arduino Online Shop». Accedido: 5 de abril de 2024. [En línea]. Disponible en: https://store-usa.arduino.cc/products/arduino-nano-33-iot?selectedStore=us

[2]  A. S. C. Pérez, G. Á. Rodríguez, and R. P. Gómez, “DISEÑO DE UN FILTRO DIGITAL PASA BAJAS DE PRIMER Y SEGUNDO ORDEN A PARTIR DE CIRCUITO RC,” Pistas Educativas, vol. 38, no. 120, 2018. 

