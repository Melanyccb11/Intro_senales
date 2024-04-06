<h1 style="text-align: center;">ADQUISICIÓN DE SEÑALES Y GRAFICACIÓN EN ARDUINO - GRUPO 2</h1>


</h3>Nombre de los Integrantes y código:
</h3>1. Melanie
</h3>2.Alessandra Valle Montoya  71098563
</h3>3. cat
</h3>4.Juan Jose Sandoval Barrantes 74145560



<h2 style="text-align: center;">Tabla de Contenidos</h2>

1. [Plotear señales en Arduino IDE provenientes del generador de señales](#Ploteo)
2. [Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio](#Comparar)
3. [Arduino Cloud](#Arduino)
4. [Docentes](#Docentes)
5. [Referencias](#Referencias)

<a id = "Ploteo" style></a>
<h2 style = "text-align: center;">Plotear señales en Arduino IDE provenientes del generador de señales</h2>

En el proceso para plotear una señal en Arduino, se utilizó el puerto analógico del Arduino nano 33 IoT, un generador de señales y se armó un pequeño circuito en un protoboard con un capacitor en tierra y el pin como se puede observar en la figura 1.

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/circuito.png" align="center" width="120" height="150"/>
</p>

Primero creamos la señales, por lo que usamos un osciloscopio digital.Debido a que el cable de osciloscopio BNC trabaja con una atenuación x10, nos percatamos que el osciloscopio, la señal puesta en el generador de señales será reducía 10 veces.

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/atenuacion.png " align="center" width="120" height="150"/>
</p>
Figura [2]: Demostración de la atenuación x10 del cable de osciloscopio BNC

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/codig1.png" align="center" width="120" height="150"/>
</p>
<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/codig2.png" align="center" width="120" height="150"/>
</p>
Figura [3]: Código en Arduino

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/señal1.jpeg" align="center" width="120" height="150"/>
</p>
Figura [4]: Señal 1 Sinusoidal con amplitud 1V, frecuencia de 2Hz y Fmuestreo=5*F, sin capacitor

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/señal 2Hz sin.jpeg" align="center" width="120" height="150"/>
</p>
Figura [5]: Señal 2 Sinusoidal con amplitud 2.5V, frecuencia de 2Hz y Fmuestreo=10*F, sin capacitor

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/5HzSin.jpg" align="center" width="120" height="150"/>
</p>
Figura [6]: Señal 3 Sinusoidal con amplitud 2.5V, frecuencia de 5Hz y Fmuestreo=5*F, sin capacitor

<p align="center">
<img src="<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/Con2Hz.jpg" align="center" width="120" height="150"/>" align="center" width="120" height="150"/>
</p>
Figura [7]: Señal 4 Sinusoidal con amplitud 2V, frecuencia de 2Hz y Fmuestreo=5*F, CON capacitor

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/Con5hz.jpg" align="center" width="120" height="150"/>
</p>
Figura [8]: Señal 5 Sinusoidal con amplitud 2V, frecuencia de 5Hz y Fmuestreo=5*F, CON capacitor

La presencia del capacitor en el circuito puede tener un impacto tanto en la reducción del ruido no deseado como en la disminución de la amplitud de la señal deseada. 

Cuando hablamos de un circuito donde se introduce un capacitor, como en un circuito RC (Resistencia-Capacitor), la presencia de este componente puede afectar la señal eléctrica. Este circuito atenúa o reduce el ruido no deseado que pueda estar presente en la señal, es decir, funciona como un filtro de componentes no deseados. Sin embargo, el capacitor también puede afectar la señal útil, dependiendo de la frecuencia de la señal y del valor del capacitor, este componente puede influir en cómo la señal se carga y descarga a través del circuito. En algunos casos, esto puede provocar una disminución en la amplitud de la señal deseada.[1]

<p align="center">
<img src="Documentación/2. Ploteo de Señales/Imagenes Lab2/rc.jpeg" align="center" width="120" height="150"/>
</p>
Figura [9]: Circuito RC 


<a id = "Comparar"></a>  
<h2 style = "text-align: center;">Comparar las señales graficadas del Arduino IDE con las gráficas obtenidas del osciloscopio</h2>

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
