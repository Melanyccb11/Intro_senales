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
- Por medio de la literatura, hallar los valores normales variabilidad de la frecuencia cardiaca (HRV).<br />
- Plotear los picos de la onda R de las señales de ECG antes tomadas y graficarlas utilizando python. <br />


<a id = "intro" style></a>
<h2 style = "text-align: center;">Introducción</h2>

La Variabilidad de la Frecuencia Cardíaca (HRV) es un parámetro vital significativo que refleja la actividad del Sistema Nervioso Autónomo (ANS). Es la variación en el tiempo entre latidos cardíacos consecutivos, y se mide en milisegundos. HRV es un indicador de la salud cardiovascular y la adaptabilidad del ANS ante diferentes estímulos y estrés​​​​.
HRV se deriva principalmente de los intervalos RR, que son las diferencias de tiempo entre picos R sucesivos en un electrocardiograma (ECG). La precisión en la detección de estos picos R es crucial para una medición fiable de HRV. Métodos modernos incluyen el uso de filtros digitales, transformada de ondícula y algoritmos de aprendizaje automático para mejorar la detección y localización de estos pico [1], [2], [3].

### Métodos aplicados para calcular HRV

Detección de Picos R: Utiliza algoritmos como el de Pan-Tompkins y modificaciones que incluyen filtros de paso de banda y técnicas de emparejamiento de plantillas para localizar con precisión los picos R en señales ECG [2]​​.
Extracción de Intervalos RR: Una vez detectados los picos R, se calculan los intervalos RR como la diferencia temporal entre picos consecutivos.
Análisis Espectral: Los intervalos RR se interpolan y se utiliza una transformada rápida de Fourier (FFT) o métodos autorregresivos para obtener el espectro de potencia de HRV. Se calculan índices como la potencia de baja frecuencia (LF) y alta frecuencia (HF), y su relación (LF/HF), para evaluar el balance simpático-vagal​​ [3].

 </p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/9.%20Procesamiento%20y%20HVR%20de%20la%20se%C3%B1al%20ECG/Im%C3%A1genes/hrv.png">
<h5 align="center">
  <i>Figura 1. La variabilidad de la frecuencia cardíaca [4] </i></div>
<br /> </p>
</h5>

<a id = "matereiales"></a>  
<h2 style = "text-align: center;">Materiales y equipos</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
|      Laptop      | Una laptop equipada con Python, un lenguaje de programación versátil y poderoso, es ideal para realizar tareas de programación y análisis de datos en entornos de laboratorio. |<img width="200" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/6.%20Filtros%20IIR%20y%20FIR/Im%C3%A1genes/68af906e-92c2-4096-ab4c-06e60cba53f1.jpg">|

</div>


<a id = "metodo" style></a>
<h2 style = "text-align: center;">Metodolodía</h2>

#### Metodología General
</p>

La Variabilidad de la Frecuencia Cardíaca (HRV) es un parámetro vital que refleja la actividad del Sistema Nervioso Autónomo (ANS). La HRV se mide a partir de los intervalos RR, que son las diferencias de tiempo entre picos R sucesivos en un electrocardiograma (ECG). Este análisis es esencial para evaluar la salud cardiovascular y la respuesta del ANS a diferentes estímulos y estrés. [3][6]

- Adquisición de señales ECG: 
Para realizar este análisis, utilizamos señales ECG previamente adquiridas y filtradas. Las señales deben ser capturadas con una frecuencia adecuada, para asegurar la captura de detalles finos de las ondas ECG. [6]

- Procesamiento de la señal:
Primero, se aplica un filtro pasa alta para eliminar componentes de baja frecuencia y tendencias de la señal ECG. Luego, utilizamos la Transformada Discreta de Wavelet (DWT) para resaltar los picos R en la señal, y cuadramos la señal resultante para incrementar el rango dinámico de los picos dominantes, facilitando su detección.[3]

- Detección de Picos R: 
Implementamos el algoritmo de Pan-Tompkins que incluye técnicas de emparejamiento de plantillas y filtros de pasa banda, para detectar con precisión los picos R. [6]
Utilizaremos la función ‘fin_peaks’ de la biblioteca scipy para identificar las posiciones de los picos en la señal procesada.

- Cálculo de intervalos RR: 
Una vez detectados los picos R, calculamos los intervalos RR, que son las diferencias de tiempo entre los tiempos de ocurrencia de los picos sucesivos. Estos intervalos son cruciales para el análisis de la HRV.[3]

- Interpolación de intervalos RR:
Para obtener una señal HRV equidistante, realizaremos una interpolación cúbica de los intervalos RR. Esto convierte las ubicaciones de tiempo de los intervalos RR, que no están equidistantemente muestreadas, en una señal HRV equidistante. [3]

- Análisis Espectral:
Calculamos la densidad espectral de potencia (PSD) de la señal HRV utilizando el método de Welch. Este método nos permite analizar los componentes de frecuencia de la señal HRV, proporcionando una visión detallada de la variabilidad de la frecuencia cardiaca. [5]

- Visualización de Resultados:
Graficamos tanto la señal ECG original como la señal procesada, resaltando los picos R detectados. También graficamos la señal HRV y su PSD. Estas visualizaciones son esenciales para entender la calidad de las señales y los resultados del procesamiento.

- Evaluación de la HRV:
Comparamos los valores obtenidos (RMSSD, SDNN, pNN50) con los valores normales reportados en la literatura. [5] Evaluamos la salud cardiovascular y la adaptabilidad del ANS basándonos en estos resultados, proporcionando una interpretación detallada de la HRV en el contexto del estudio.




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

Con el fin de resaltar los picos R, se utiliza la Transformada Discreta de Wavelet (DWT) seguida de la cuadratura de la señal. Esto ayuda a incrementar el rango dinámico de los picos dominantes en la señal, facilitando su detección

Se implementa un algoritmo para detectar los picos R en la señal procesada. Esto se hace utilizando la función `find_peaks` de scipy, que permite identificar las posiciones de los picos en la señal.
```python
peaks, _ = find_peaks(squared_ecg, distance=150)
r_peaks = np.array([i for i in peaks if squared_ecg[i] > umbral])
```

Para obtener una señal HRV equidistante, se realiza una interpolación cúbica. Esto permite convertir las ubicaciones de tiempo de los intervalos RR, que no están equidistantemente muestreadas, en una señal HRV equidistante:
```python
time_rr = np.cumsum(rr_intervals) / fs
cs = CubicSpline(time_rr, rr_intervals)
time_hrv = np.arange(time_rr[0], time_rr[-1], 1/fs)
hrv_signal = cs(time_hrv)
```

Se calcula la densidad espectral de potencia (PSD) de la señal HRV usando el método de Welch. Este método es útil para analizar las componentes de frecuencia de la señal HRV:
```python
frequencies, psd = welch(hrv_signal, fs, nperseg=256)
```

Finalmente, se grafican tanto la señal ECG original y procesada, como la señal HRV y su PSD. Estas visualizaciones son esenciales para entender la calidad de las señales y los resultados del procesamiento

</p>


## Para las señales de ECG 

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
1. RMSSD: 0.0373 s
2. SDNN: 0.0373 s
3. PNN50: 4.347 %


#### Interpretación:
- RMSSD: Los valores normales de RMSSD en adultos sanos generalmente oscilan entre 19 y 75 ms, con un promedio de alrededor de 42 ms [4]. En nuestro caso, el valor obtenido de RMSSD es de 37.3 ms, lo cual se encuentra dentro del rango normal, aunque ligeramente por debajo del promedio. Esto sugiere una variabilidad de frecuencia cardíaca adecuada con una respuesta vagal saludable.
- SDNN: Los valores normales de SDNN en grabaciones a corto plazo (~5 minutos) para adultos sanos están en el rango de 32 a 93 ms, con un promedio de 50 ms. El valor obtenido de SDNN es de 37.3 ms, lo cual se encuentra dentro del rango normal, aunque por debajo del promedio. Esto indica una variabilidad total de la frecuencia cardíaca en un nivel considerado saludable, pero podría ser mejor [4].
- pNN50: Los valores normales de pNN50 en adultos sanos generalmente oscilan entre 1 y 45%, con un promedio de alrededor de 18%. En nuestro caso, el valor obtenido de pNN50 es de 4.347%, lo cual está dentro del rango normal, pero significativamente por debajo del promedio. Esto sugiere una menor variabilidad de alta frecuencia, reflejando una actividad parasimpática menos prominente [4].




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
1. RMSSD: 0.49033 s
2. SDNN: 0.3513 s
3. PNN50: 10.3448 %



#### Interpretación:
- RMSSD: En este caso, el valor obtenido de RMSSD durante el ejercicio de respiración es de 490.33 ms, lo cual es significativamente más alto que el rango normal. Esto sugiere una altísima variabilidad de frecuencia cardíaca, indicando una fuerte actividad parasimpática inducida por el ejercicio de respiración controlada [4].
- SDNN: El valor obtenido de SDNN durante el ejercicio de respiración es de 351.3 ms, lo cual es significativamente más alto que el rango normal. Esto indica una variabilidad total de la frecuencia cardíaca extremadamente alta, reflejando una fuerte actividad autónoma, posiblemente debido a la sincronización de la respiración con la frecuencia cardíaca[4].
- pNN50: En este caso, el valor obtenido de pNN50 durante el ejercicio de respiración es de 10.3448%, lo cual está dentro del rango normal pero por debajo del promedio. Esto sugiere una menor variabilidad de alta frecuencia comparada con los otros índices, aunque todavía en un nivel saludable y reflejando una actividad parasimpática moderada [4].




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

- RMSSD el valor obtenido de RMSSD durante el estado de reposo luego del ejercicio de respiración es de 165.3 ms, lo cual es significativamente más alto que el rango normal. Esto sugiere una altísima variabilidad de frecuencia cardíaca, indicando una fuerte actividad parasimpática inducida por el ejercicio de respiración controlada[4].
- SDNN: El valor obtenido de SDNN durante el estado de reposo luego del ejercicio de respiración es de 134.5 ms, lo cual es significativamente más alto que el rango normal. Esto indica una variabilidad total de la frecuencia cardíaca extremadamente alta, reflejando una fuerte actividad autónoma, posiblemente debido a la sincronización de la respiración con la frecuencia cardíaca [4].
- pNN50. En este caso, el valor obtenido de 9.5238%, está dentro del rango normal pero por debajo del promedio. Esto sugiere una menor variabilidad de alta frecuencia comparada con los otros índices, aunque todavía en un nivel saludable y reflejando una actividad parasimpática moderada [4].


<a id = "explic"></a>
<h2 style = "text-align: center;">Resumen y Discusión</h2>

### Discusión

La Variabilidad de la Frecuencia Cardíaca (HRV) es un parámetro esencial para evaluar la actividad del Sistema Nervioso Autónomo (ANS). En este estudio, analizamos los valores de HRV en diferentes condiciones: reposo, durante un ejercicio de respiración controlada y en reposo después del ejercicio. Utilizamos los índices RMSSD, SDNN y pNN50 para evaluar la HRV y compararlos con los valores normales reportados en la literatura.

En reposo, el RMSSD obtenido fue de 37.3 ms, situándose dentro del rango normal (19-75 ms) pero ligeramente por debajo del promedio de 42 ms [4]. Esto sugiere una variabilidad de frecuencia cardíaca adecuada con una respuesta vagal saludable. El SDNN fue de 37.3 ms, también dentro del rango normal (32-93 ms) pero por debajo del promedio de 50 ms, indicando una variabilidad total de la frecuencia cardíaca en un nivel saludable, aunque podría ser mejor. El pNN50 fue de 4.347%, dentro del rango normal (1-45%) pero significativamente por debajo del promedio de 18%, lo que sugiere una menor variabilidad de alta frecuencia y una actividad parasimpática menos prominente [4].

Durante el ejercicio de respiración (inhalación 5 segundos, mantenimiento 5 segundos, exhalación 5 segundos), el RMSSD alcanzó 490.33 ms, un valor significativamente más alto que el rango normal, indicando una altísima variabilidad de frecuencia cardíaca y una fuerte actividad parasimpática inducida por la respiración controlada. El SDNN fue de 351.3 ms, también muy por encima del rango normal, reflejando una variabilidad total de la frecuencia cardíaca extremadamente alta debido a la sincronización de la respiración con la frecuencia cardíaca. El pNN50 fue de 10.3448%, dentro del rango normal pero por debajo del promedio, sugiriendo una menor variabilidad de alta frecuencia comparada con los otros índices, aunque todavía en un nivel saludable[4].

En el estado de reposo luego del ejercicio de respiración, el RMSSD fue de 165.3 ms, significativamente más alto que el rango normal, sugiriendo una altísima variabilidad de frecuencia cardíaca y una fuerte actividad parasimpática. El SDNN fue de 134.5 ms, también muy por encima del rango normal, indicando una variabilidad total de la frecuencia cardíaca extremadamente alta. El pNN50 fue de 9.5238%, dentro del rango normal pero por debajo del promedio, reflejando una actividad parasimpática moderada pero saludable[4].

Estos resultados demuestran que el ejercicio de respiración controlada tiene un impacto significativo en la HRV, aumentando notablemente la variabilidad de la frecuencia cardíaca y la actividad parasimpática. Esto sugiere que tales ejercicios pueden ser útiles para mejorar la función del sistema nervioso autónomo y la salud cardiovascular en general.

### Resumen

Los objetivos de este estudio fueron determinar los valores normales de la variabilidad de la frecuencia cardíaca (HRV) a partir de la literatura y plotear los picos de la onda R de las señales de ECG previamente obtenidas, utilizando Python. La HRV es un indicador crucial de la salud cardiovascular y la capacidad de adaptación del ANS a diferentes estímulos. La HRV se calcula a partir de los intervalos RR, derivados de los picos R en un ECG.

Para este análisis, se utilizaron señales ECG previamente adquiridas y filtradas. Los picos R se detectaron mediante el algoritmo de Pan-Tompkins y se calcularon los intervalos RR. La señal HRV se obtuvo mediante interpolación cúbica y se analizó utilizando el método de Welch para calcular la densidad espectral de potencia (PSD).

En reposo, los valores de RMSSD, SDNN y pNN50 se situaron dentro del rango normal pero por debajo del promedio, indicando una variabilidad de frecuencia cardíaca adecuada pero mejorable. Durante el ejercicio de respiración controlada, los valores aumentaron significativamente, reflejando una fuerte actividad parasimpática y una alta variabilidad de la frecuencia cardíaca. Después del ejercicio, los valores permanecieron elevados, sugiriendo una sostenida actividad autónoma y una eficiente respuesta parasimpática.

En conclusión, el ejercicio de respiración controlada mejora significativamente la HRV y la actividad parasimpática, promoviendo una mejor recuperación y equilibrio homeostático. Estos resultados destacan la efectividad de los ejercicios de respiración en la mejora de la función del sistema nervioso autónomo y la salud cardiovascular.


<a id = "Bibliografía"></a>
<h2 style = "text-align: center;">Bibliografía</h2>

[1]	R. Tiwari, R. Kumar, S. Malik, T. Raj, and P. Kumar, “Analysis of Heart Rate Variability and Implication of Different Factors on Heart Rate Variability,” Curr. Cardiol. Rev., vol. 17, no. 5, p. e160721189770, Oct. 2021, doi: 10.2174/1573403X16999201231203854. </p>
[2]	D. Zhai, X. Bao, X. Long, T. Ru, and G. Zhou, “Precise detection and localization of R-peaks from ECG signals,” Math. Biosci. Eng., vol. 20, no. 11, pp. 19191–19208, 2023, doi: 10.3934/mbe.2023848.</p>
[3]	A. Verma, S. Cabrera, A. Mayorga, and H. Nazeran, “A robust algorithm for derivation of heart rate variability spectra from ECG and PPG signals,” in 2013 29th southern biomedical engineering conference, IEEE, 2013, pp. 35–36. doi: http://dx.doi.org/10.1109/SBEC.2013.26.</p>
[4]	A. R. Crecelius, “Heart rate variability – what to know about this biometric most fitness trackers measure,” The Conversation. Accessed: Jun. 06, 2024. [Online]. Available: http://theconversation.com/heart-rate-variability-what-to-know-about-this-biometric-most-fitness-trackers-measure-194898. </p>
[5]	F. Shaffer and J. P. Ginsberg, "An Overview of Heart Rate Variability Metrics and Norms," Frontiers in Public Health, vol. 5, pp. 258, Sept. 2017. doi: 10.3389/fpubh.2017.00258..</p>
[6]	J. Pan and W. J. Tompkins, "A real-time QRS detection algorithm," IEEE Transactions on Biomedical Engineering, vol. BME-32, no. 3, pp. 230-236, Mar. 1985. doi: 10.1109/TBME.1985.325532..</p>



