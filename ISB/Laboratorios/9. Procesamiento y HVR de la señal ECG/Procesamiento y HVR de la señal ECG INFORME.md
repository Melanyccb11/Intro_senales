<h1 style="text-align: center;">Laboratorio 9: Procesamiento y HVR de la señal ECG</h1>

</h3>Nombre de los Integrantes y código:

1. Melany Cama Bahamonde 72128361
2. Alessandra Valle Montoya  71098563
3. Catherine Boggio Vidal 71329106
4. Juan Jose Sandoval Barrantes 74145560
</p>

<h2 style="text-align: center;">Tabla de Contenidos</h2>

1. [Objetivos](#objetivo)
2. [Introducción](#intro)
3. [Materiales y equipos](#matereiales)
4. [Metodología](#metodo)
5. [Archivo de los datos de la señal ploteada](#archivosenal)
6. [Ploteo de la señal en Python](#python)
7. [Resumen y Discusión](#explic)
8. [Bibliografía](#Bibliografía)

<a id = "objetivo" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- <br />
- <br />
- <br />


<a id = "intro" style></a>
<h2 style = "text-align: center;">Introducción</h2>

bliblbi

### Filtros FIR (Respuesta al Impulso Finita):

depende si vamos a usar este o no, nos podemos guir del articulo 

 </p>
<p align="center">
 <img width="250" height="150" src="">
<h5 align="center">
  <i>Figura 1. </i></div>
<br /> </p>
</h5>

 </p>
<p align="center">
 <img width="660" height="400" src="">
<h5 align="center">
  <i>Figura 2. balbla.</i></div></h5>

####  Método de ventanas:

1. blibli



</p>
</h5>
 <p align="center" style="margin-bottom:0">
<img src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/6.%20Filtros%20IIR%20y%20FIR/Im%C3%A1genes/ventanas%20fir.png"/>
<div align="center"> 
 <h5 align="center">
 <i>Figura 3. .</i></div></h5>
<p>
 
</p>
</h5>
 <p align="center" style="margin-bottom:0">
<img src=""> 
<h5 align="center">
  <i>Figura 4. </i></div></h5>
<p>


### Filtros IIR (Respuesta al Impulso Infinita): 

DEpende si vamos a usar este o no 

 </p>
<p align="center">
 <img width="500" height="600" src=">
<h5 align="center">
  <i>Figura 5. </i></div>

#### Tipos de filtro:

1. biblibli


</p>
</h5>
 <p align="center" style="margin-bottom:0">
<img src="hbli" align="center" width="660" height="500"/>
 <h5 align="center">
 <i>Figura 6. Filtros IIR [X].</i></div></h5>
<p>

  

<a id = "matereiales"></a>  
<h2 style = "text-align: center;">Materiales y equipos</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
|      Laptop      | Una laptop equipada con Python, un lenguaje de programación versátil y poderoso, es ideal para realizar tareas de programación y análisis de datos en entornos de laboratorio. |<img width="200" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/6.%20Filtros%20IIR%20y%20FIR/Im%C3%A1genes/68af906e-92c2-4096-ab4c-06e60cba53f1.jpg">|

</div>


<a id = "metodo" style></a>
<h2 style = "text-align: center;">Metodolodía</h2>

### Metodología General
</p>

1. Pasitos


</p>


<a id = "archivosenal"></a>
<h2 style = "text-align: center;">Archivos de los datos de la señal ploteada</h2>
</h5>

#### EEG
1. [Registro 1 - Bitalino: Reposo](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/5.%20Adquisi%C3%B3n%20de%20Se%C3%B1ales%20EEG/Archivos%20Texto/EEG_PrimeroOsjoscerrados.txt)</p>
2. [Registro 2 - Bitalino: Abriendo/Cerrando ojos](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/5.%20Adquisi%C3%B3n%20de%20Se%C3%B1ales%20EEG/Archivos%20Texto/EEG_2_5s.txt)</p>
3. [Registro 3 - Bitalino: Resolviendo ejercicios](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/5.%20Adquisi%C3%B3n%20de%20Se%C3%B1ales%20EEG/Archivos%20Texto/ejmate.txt)</p>
#### EMG

### Archivos python 

1. [Código principal](http)</p>


<a id = "python"></a>
<h2 style = "text-align: center;">Ploteo de la señal en Python</h2>
</p>

hablar de lo que se hare en el archi de python</p>


## Para las señales de ECG 

VER SI ESTO SE QUEDA

Se realiza la elección de los filtros FIR e IIR, en el caso de del ECG, se eligen:
1. Selección de Filtro IIR:
   - Para mitigar el ruido presente en las señales adquiridas de electrocardiograma (ECG) en el laboratorio 4, hemos empleado el filtro Butterworth. Este tipo de filtro ha demostrado ser altamente efectivo en la eliminación del ruido de las señales de ECG afectadas [11]. Al observar la gráfica, podemos apreciar una notable reducción del ruido en comparación con la señal original. Este resultado se atribuye principalmente a la elección de la frecuencia de corte y al orden del filtro [12]. En nuestro estudio, hemos diseñado un filtro con una frecuencia de corte de 50 Hz y un orden de 4. No obstante, al aplicar el filtro, hemos observado una disminución en la amplitud de las ondas R y T. Este efecto se debe al orden del filtro seleccionado. Sin embargo, gracias a la frecuencia de corte, hemos notado una mejora significativa en la nitidez del complejo QRS [12].
2. Selección de Filtro FIR:
   - Además, implementamos un filtro FIR utilizando la ventana de Hamming y Blackman, con una frecuencia de corte de 50 Hz y con un orden de 101 [14]. Esta ventana se caracteriza por tener lóbulos laterales cercanos a cero, lo que significa que reduce significativamente la fuga de energía de la señal fuera de la banda de interés. Este enfoque ayuda a mejorar la selectividad del filtro y a minimizar la distorsión de la señal de interés [14]. Sin embargo, al representar gráficamente la señal filtrada, observamos un aumento en la amplitud dentro del intervalo ST, en comparación con la señal original, y también se detecta un retraso de la señal con respecto a la original. Este comportamiento puede ser atribuido al error y al retraso inherentes al filtro utilizado, a pesar de ello cumple con la función de filtrar la señal. [14].

</p>
</h5>
 <p align="center" style="margin-bottom:0">
<img width="800" height="600" src=""> 
<h5 align="center">
  <i>Figura 7. Filtros para la señal de ECG. [Elaboración propia]</i></div>
<p>



### Reposo :
bliblibli
</p>
<p align="center">
<img width="800" height="600" src="h">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>


</p>
<p align="center">
<img width="800" height="600" src="h">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>


(HABLAR DE HRV)

#### Interpretación:

VER SI ESTO SE QUEDAAAA...

1. Picos agudos en la señal original: Estos picos se observan claramente alrededor de los 20.50 segundos y 21.50 segundos. Estos probablemente corresponden a los complejos QRS, que son indicativos de la actividad eléctrica del corazón asociada con la contracción de los ventrículos. Son las características más notables en una señal de EKG y representan un punto de análisis crucial.
2. Respuesta de los filtros:
- FIR filtro Hamming: La señal filtrada con Hamming muestra una suavización de la señal pero sigue reflejando los picos, aunque con menos ruido y variaciones menores entre los picos.
- FIR filtro Blackman: Similar al filtro Hamming, este filtro también suaviza la señal pero mantiene una amplitud considerable en los picos QRS, mostrando una buena preservación de las características importantes del EKG.
- IIR filtro Butterworth: Este filtro muestra una respuesta más variable. Mientras que filtra bastante ruido, también parece alterar un poco más la amplitud y la forma de los picos QRS, especialmente notable alrededor de los 21.50 segundos donde el pico parece más distorsionado en comparación con los filtros FIR.
  
La ventana de interés más significativa estaría centrada alrededor de estos picos QRS, ya que son esenciales para analizar el ritmo cardíaco y la actividad eléctrica del corazón. Estos segmentos, específicamente alrededor de 20.50 y 21.50 segundos, serían los puntos focales para un análisis más detallado de la señal de reposo.

+ HRV

### Inhalando/Manteniendo/Exhalando por 5s

BLIBLI

</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/6.%20Filtros%20IIR%20y%20FIR/Im%C3%A1genes/ECG_IN_HOLS_EX.jpg">
</p>
<h5 align="center">
  Figura 11: Señal obtenida en python: Inhalando/Manteniendo/Exhalando por 5s. [Elaboración propia]
</h5>

(HABLAR DE HRV)

#### Interpretación:

VER SI ESTO SE QUEDA 

En la nueva gráfica, las ventanas de interés pueden identificarse alrededor de los picos más prominentes en la señal original, que son visibles cerca de los 20.50 segundos y 21.50 segundos. Estos picos, que probablemente representan los complejos QRS, son momentos clave en un EKG ya que indican la actividad eléctrica de los ventrículos del corazón.

- FIR filtro Hamming y FIR filtro Blackman: Ambos filtros han suavizado la señal, pero aún conservan las características de los picos, haciendo que estas características sean claramente visibles, aunque con una amplitud algo reducida. Estos filtros están logrando una buena balance entre reducir el ruido y preservar la información importante de los picos QRS.
- IIR filtro Butterworth: Este filtro muestra una reducción significativa en el ruido de la señal y una preservación adecuada de los picos, aunque con un efecto de suavizado más pronunciado que podría afectar la nitidez de los picos QRS.

La ventana de interés para un análisis más detallado sería entre 20.25 segundos y 21.75 segundos, abarcando ambos picos QRS y permitiendo evaluar la eficacia del filtro en preservar la integridad de estos importantes eventos cardíacos mientras reduce el ruido circundante.

+ HRV

### Después del ejercicio físico

BLIBL

</p>
<p align="center">
<img width="800" height="600" src="">
</p>
<h5 align="center">
  Figura 13. Señal obtenida en python: Después del ejercicio físico. [Elaboración propia]
</h5>

(HABLAR DE HRV)

#### Interpretación:

VER SI ESTO SE QUEDA 

En esta gráfica después de realizar un ejercicio físico, las ventanas de interés son claramente visibles alrededor de los picos más altos de la señal original, que se producen cerca de los 2.50 segundos y 3.25 segundos. Estos picos son indicativos de los complejos QRS, que son cruciales para analizar la actividad eléctrica del corazón, especialmente después del ejercicio.

- FIR filtro Hamming: Muestra una suavización significativa de la señal con menos ruido, pero aún conserva la forma de los picos QRS, lo que es esencial para mantener la información diagnóstica relevante.
- FIR filtro Blackman: Similar al filtro Hamming, también suaviza la señal mientras preserva los picos, aunque con una ligera distorsión en la forma y la amplitud de los picos.
- IIR filtro Butterworth: Este filtro muestra una respuesta más suave con cierta distorsión en los picos QRS, lo que podría ser relevante al analizar cómo afecta el ejercicio a la señal cardíaca.

La ventana de interés para el análisis detallado en este caso se extendería desde aproximadamente los 2.25 segundos hasta los 3.50 segundos, abarcando ambos picos QRS principales. Este rango incluye los eventos cardíacos más significativos en el periodo post-ejercicio, permitiendo una evaluación efectiva de cómo el ejercicio ha influido en la actividad eléctrica del corazón.

+ HRV

<a id = "explic"></a>
<h2 style = "text-align: center;">Resumen y Discusión</h2>

explicacion y resumen de lo identificado 

<a id = "Bibliografía"></a>
<h2 style = "text-align: center;">Bibliografía</h2>

[1]	 


