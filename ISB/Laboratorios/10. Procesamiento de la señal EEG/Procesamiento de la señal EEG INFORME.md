<h1 style="text-align: center;">Laboratorio 10: Procesamiento de la señal EEG</h1>

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
   - Usar de bases de datos de PhysioNet que contengan señales EEG.<br />
   - Filtrar de las señales EEG para eliminar ruido.<br />
   - Establecer las bases para el preprocesimento de la señal. <br />
   - Extraer las características relevantes de la señal EEG. <br /> </p>


<a id = "intro" style></a>
<h2 style = "text-align: center;">Introducción</h2>

El electroencefalograma (EEG) es una técnica neurofisiológica no invasiva que mide y cuantifica la actividad neuronal en diversas regiones del cerebro mediante la colocación de electrodos en el cuero cabelludo. Esta metodología permite a los investigadores capturar señales eléctricas generadas por el cerebro, proporcionando valiosa información sobre los mecanismos operativos del mismo. El procesamiento de estas señales enfrenta desafíos significativos debido a sus características inherentes. Estas señales son altamente susceptibles a la interferencia del ruido, lo que resulta en una baja relación señal-ruido. Además, su naturaleza no lineal y su falta de conformidad con una distribución normal las distinguen de las señales convencionales. Factores individuales como la edad, el estado psicológico y el entorno de prueba también pueden causar variaciones significativas en las señales EEG. Por lo tanto, es esencial desarrollar metodologías avanzadas para el análisis de señales y explorar técnicas de aprendizaje automático para entender mejor las señales EEG [1] . </p>
En los últimos años, las técnicas de procesamiento de señales EEG han avanzado considerablemente. Métodos de preprocesamiento y extracción de características han sido propuestos para mejorar la calidad de las señales y permitir una mejor interpretación de los datos. La eliminación efectiva del ruido es crucial para extraer información significativa que refleje con precisión la actividad y los estados cerebrales [2] .  </p>

Este informe se centra en el análisis de señales EEG, a partir de las señales que obtuvimos en laboratorios pasados y una base de datos fisiológico se hará realizará un filtrado, preprocesamiento,  extracción de características y su clasificación. </p>



### Métodos aplicados para calcular HRV

bliblibli

 </p>
<p align="center">
 <img width="250" height="150" src="figurita">
<h5 align="center">
  <i>Figura 1. blibli. </i></div>
<br /> </p>
</h5>

<a id = "matereiales"></a>  
<h2 style = "text-align: center;">Materiales y equipos</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
|      Laptop      | Una laptop equipada con Python, un lenguaje de programación versátil y poderoso, es ideal para realizar tareas de programación y análisis de datos en entornos de laboratorio. |<img width="200" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/6.%20Filtros%20IIR%20y%20FIR/Im%C3%A1genes/68af906e-92c2-4096-ab4c-06e60cba53f1.jpg">|
|      Database     | La Base de base datos de PhysioNet cuenta con acceso abierto a usarios para la extración de registros de estudios de señales fisilógicas. |<img width="200" height="150" src="">|
</div>

</p>
<a id = "metodo" style></a>
<h2 style = "text-align: center;">Metodología</h2>

#### Filtrado <br />
Para las señales en EEG, al igual que en ECG, elegimos para los filtros IIR el Butterworth de cuarto orden, ya que este es comúnmente utilizado para el procesamiento de señales de EEG con el fin de filtrar y eliminar componentes no deseados . En las gráficas podemos observar que las señales se atenúan sin tener un delay, sin embargo hay un cambio en su amplitud [M. K. Hasan, R. Z. Rusho, T. M. Hossain, T. K. Ghosh, y M. Ahmad, «Design and simulation of cost effective wireless EEG acquisition system for patient monitoring», en 2014 International Conference on Informatics, Electronics & Vision (ICIEV), IEEE, 2014, pp. 1-5.]. <br />

#### Preprocesamiento <br />
El proceso de normalización de la señal EEG después del filtrado incluye detectar la entropía de muestra para identificar señales anormales, usando un umbral definido \( k \). Luego, se calcula la energía media de cada segmento de la señal, utilizando la norma L1, y se clasifica como anormal si supera un umbral \( e \). El valor máximo absoluto de los segmentos normales se usa como coeficiente de normalización \( m \), dividiendo toda la señal por \( m \) para normalizar. Finalmente, la señal normalizada se introduce en una red generativa adversaria (GAN) para entrenar el modelo y obtener datos EEG limpiados, asegurando un rango controlado y estable. [Y. An, H. K. Lam, and S. H. Ling, “Auto-Denoising for EEG Signals Using Generative Adversarial Network,” Sensors, vol. 22, no. 5, p. 1750, Feb. 2022, doi: 10.3390/s22051750]. Con esto aseguramos la homogeneidad de los datos y la mejoría de la precisión de nuestro análisis. <br />

#### Wavelet
Para aplicar la transformada wavelet a una señal EEG después de la normalización, primero se selecciona una función wavelet adecuada, como Daubechies, que se ajusta bien a las características de la señal EEG. Luego, se descompone la señal normalizada en coeficientes de detalle y aproximación a varios niveles de frecuencia utilizando la transformada wavelet discreta (DWT). Posteriormente, se aplica un umbral a los coeficientes wavelet para eliminar el ruido presente en la señal, usando técnicas como la umbralización suave o dura. Finalmente, se reconstruye la señal limpia a partir de los coeficientes umbralizados mediante la transformada wavelet inversa (IDWT), asegurando que las características esenciales de la señal se conservan mientras se elimina el ruido. Esta metodología permite una mejora significativa en la calidad de la señal EEG para análisis posteriore [I. H. Elshekhidris, M. B. MohamedAmien, and A. Fragoon, “WAVELET TRANSFORMS FOR EEG SIGNAL DENOISING AND DECOMPOSITION,” Int. J. Adv. SIGNAL IMAGE Sci., vol. 9, no. 2, Art. no. 2, Dec. 2023, doi: 10.29284/ijasis.9.2.2023.11-28.] [M. Jas et al., “MEG/EEG group study with MNE: recommendations, quality assessments and best practices.” Dec. 28, 2017. doi: 10.1101/240044.]




</p>


<a id = "archivosenal"></a>
<h2 style = "text-align: center;">Archivos de los datos de la señal ploteada</h2>
</h5>

#### ECG
1. [Registro 1 - Base de datos Physionet](https://physionet.org/content/brain-wearable-monitoring/1.0.0/)</p>


### Archivos python 

1. [Código principal]()</p>


<a id = "python"></a>
<h2 style = "text-align: center;">Ploteo de la señal en Python</h2>
</p>

intro de lo que maso se ehace

</p>


## Para las señales de ECG 

## Señal cruda :

Primero evaluamos la señal original, para eso le sacamos su Transformada de Fourier<p>
</p>
<p align="center">
<img width="800" height="600" src="">
</p>
<h5 align="center">
  Figura 1: Señal obtenida en python: Actividad 1.[Elaboración propia]
</h5>

Procemos a la aplicación de los filtros mencionados, primero el filtro pasabanda, seguido por el filtrado IIR.</p>
#### Pasabanda y filtro IIR:
</p>
<p align="center">
<img width="800" height="600" src="">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python previamente filtrada.[Elaboración propia]
</h5>

#### Normalización:
</p>
<p align="center">
<img width="800" height="600" src="">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Normalización.[Elaboración propia]
</h5>

#### Wavelet:
</p>
<p align="center">
<img width="800" height="600" src="">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: filtrado wavelet[Elaboración propia]
</h5>

blbiblbie
</p>

#### Extraccion de características:
</p>
<p align="center">
<img width="800" height="600" src="">
</p>
<h5 align="center">
  Figura 9: Señal obtenida en python: Extracción de características.[Elaboración propia]
</h5>


#### Parámetros importantes:
1. RMSSD: 0.0373 s
2. SDNN: 0.0373 s
3. PNN50: 4.347 %


#### Interpretación:
-bliblibli


NO SE PARA CUANTOS CASOS VAMOS A HACER PERO DE SER ASI COPIAR Y PEGAR PLANTILLA DE ARRIBA


<a id = "explic"></a>
<h2 style = "text-align: center;">Resumen y Discusión</h2>

### Discusión

BLIBLIBLI

### Resumen

BLIBLIBIL


<a id = "Bibliografía"></a>
<h2 style = "text-align: center;">Bibliografía</h2>

[1]	BLIBL </p>




