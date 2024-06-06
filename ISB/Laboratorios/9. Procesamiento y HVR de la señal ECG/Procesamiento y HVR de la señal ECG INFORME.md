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

bliblbiblbelbei florito de HRV


qué parametros para el hvr 
<br />hablar del RMSSD
<br />hablar del SNRR
<br />hablar del PNN50</p>



### Filtros Notch 

first order DC-notch IIR high-pass 
filter with following transfer function este esta en el mini paper pero ampliar con info ustdes 

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

#### filtro Wavelet:

1. blibli



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
  <i>Figura 2. balbla.</i></div></h5>>
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

#### ECG
1. [Registro 1 - Bitalino: Reposo](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/4.%20Adquisi%C3%B3n%20de%20Se%C3%B1ales%20ECG/Archivo%20texto/NormalBreath30s.txt)</p>
2. [Registro 2 - Bitalino: Aguantando la respiracion 5 segundos](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/4.%20Adquisi%C3%B3n%20de%20Se%C3%B1ales%20ECG/Archivo%20texto/InHoldEx5s.txt)</p>
3. [Registro 3 - Bitalino: Luego de hacer ejercicio](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/4.%20Adquisi%C3%B3n%20de%20Se%C3%B1ales%20ECG/Archivo%20texto/ReposandoBurpee30s.txt)</p>

### Archivos python 

1. [Código principal](https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/LAB9_HVR_Filter.ipynb)</p>


<a id = "python"></a>
<h2 style = "text-align: center;">Ploteo de la señal en Python</h2>
</p>

El código se realizó en base al artículo “A Robust Algorithm for Derivation of Heart Rate Variability Spectra from ECG and PPG Signals” de Ajay Verma [1]. Este comienza importando las librerías necesarias para el procesamiento de señales y la visualización de datos. Estas incluyen librerías como numpy para el manejo de matrices y cálculos numéricos, pandas para la manipulación de datos, matplotlib para la creación de gráficos, y scipy para el procesamiento de señales.

Se carga la señal ECG desde un archivo o una fuente de datos. Esto se realiza generalmente con funciones de pandas o numpy, que permiten leer datos de archivos CSV u otros formatos y almacenarlos en estructuras de datos fáciles de manipular:

Para mejorar la calidad de la señal ECG y eliminar componentes de baja frecuencia (tendencias), se aplica un filtro pasa alto. Este filtro es implementado utilizando una función que aplica un filtro digital de primer orden.

Para resaltar los picos R, se utiliza la Transformada Discreta de Wavelet (DWT) seguida de la cuadratura de la señal. Esto ayuda a incrementar el rango dinámico de los picos dominantes en la señal, facilitando su detección

Se implementa un algoritmo para detectar los picos R en la señal procesada. Esto se hace utilizando la función `find_peaks` de scipy, que permite identificar las posiciones de los picos en la señal.
```python
peaks, _ = find_peaks(squared_ecg, distance=150)
r_peaks = np.array([i for i in peaks if squared_ecg[i] > umbral])
```

A partir de los picos R detectados, se calculan los intervalos RR, que son la diferencia entre los tiempos de ocurrencia de picos sucesivos. Estos intervalos son cruciales para el análisis de la variabilidad de la frecuencia cardíaca:
```python
rr_intervals = np.diff(r_peaks) / fs  # fs es la frecuencia de muestreo
```

Para obtener una señal HRV equidistante, se realiza una interpolación cúbica. Esto permite convertir las ubicaciones de tiempo de los intervalos RR, que no están equidistantemente muestreadas, en una señal HRV equidistante.
</p>


## Para las señales de ECG 

VER SI ESTO SE QUEDA

elegi fitro notch y luego le aplique db6 con umbral MIREN EL CODIGOOOOO o el papersssss


## Reposo :

Primero evaluamos la señal original, para eso le sacamos su Transformada de Fourier<p>
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft1.jpg">
</p>
<h5 align="center">
  Figura 1: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

Procemos a la aplicación de los filtros mencionados, primero el filtro notch segudno de del filtro wavelet dB6 con umbral, seguido de la Transformada de Fourier de cada uno.</p>
#### Notch:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft11.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Wavelet:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft12.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

Acontinuación se presentará la extracción de los picos utilizando la función: scipy.signal.find_peaks de sciPy API, luego se procedará con la extración de los intervalos RR, seguido de la determinación HRV con los parámetros más importantes y evaluar los parámetros más importante y compararlos con nuestro sujeto de estudio.</p>

#### Picos R:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/peaks1.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Intervalors RR:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/ipeaks1.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Parámetros importantes:
1. RMSSD: 0.0373
2. SDNN: 0.0373
3. PNN50: 4.347 %


#### Interpretación:
RECUEDDEN QUE ESTA EN REPOSO</p>
(HABLAR DE HRV) y lo que se espera ver aqui tipo los parametros normales TIPO SI JUANJO ESTA BIEN </p>
+ HRV</p>



## Inhalando/Manteniendo/Exhalando por 5s

Primero evaluamos la señal original, para eso le sacamos su Transformada de Fourier<p>
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft2.jpg">
</p>
<h5 align="center">
  Figura 1: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

Procemos a la aplicación de los filtros mencionados, primero el filtro notch segudno de del filtro wavelet dB6 con umbral, seguido de la Transformada de Fourier de cada uno.</p>
#### Notch:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft21.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Wavelet:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft22.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

Acontinuación se presentará la extracción de los picos utilizando la función: scipy.signal.find_peaks de sciPy API, luego se procedará con la extración de los intervalos RR, seguido de la determinación HRV con los parámetros más importantes y evaluar los parámetros más importante y compararlos con nuestro sujeto de estudio.</p>

#### Picos R:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/peaks2.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Intervalors RR:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/ipeaks2.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Parámetros importantes:
1. RMSSD: 0.49033
2. SDNN: 0.3513
3. PNN50: 10.3448 %



#### Interpretación:
RECUERDEN QUE ESTA AGUANTANDO LA RESPIRACION POR 5S</p>
(HABLAR DE HRV) y lo que se espera ver aqui tipo los parametros normales TIPO SI JUANJO ESTA BIEN </p>
+ HRV



## Después del ejercicio físico

Primero evaluamos la señal original, para eso le sacamos su Transformada de Fourier<p>
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft3.jpg">
</p>
<h5 align="center">
  Figura 1: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

Procemos a la aplicación de los filtros mencionados, primero el filtro notch segudno de del filtro wavelet dB6 con umbral, seguido de la Transformada de Fourier de cada uno.</p>
#### Notch:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft31.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Wavelet:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/fft32.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

Acontinuación se presentará la extracción de los picos utilizando la función: scipy.signal.find_peaks de sciPy API, luego se procedará con la extración de los intervalos RR, seguido de la determinación HRV con los parámetros más importantes y evaluar los parámetros más importante y compararlos con nuestro sujeto de estudio.</p>

#### Picos R:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/peaks3.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Intervalors RR:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/ipeaks3.jpg">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Actividad en reposo.[Elaboración propia]
</h5>

#### Parámetros importantes:
1. RMSSD: 0.1653
2. SDNN: 0.1345
3. PNN50: 9.5238 %

#### Interpretación:
RECUEDDEN QUE ESTA EN REPOSO</p>
(HABLAR DE HRV) y lo que se espera ver aqui tipo los parametros normales TIPO SI JUANJO ESTA BIEN </p>
+ HRV</p>


<a id = "explic"></a>
<h2 style = "text-align: center;">Resumen y Discusión</h2>

explicacion y resumen de lo identificado ya estudes saben floro

<a id = "Bibliografía"></a>
<h2 style = "text-align: center;">Bibliografía</h2>

[1]	 


