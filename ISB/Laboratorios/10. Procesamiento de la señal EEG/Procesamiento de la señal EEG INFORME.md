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

Este informe se centra en el análisis de señales EEG, a partir de las señales que obtuvimos en una base de datos fisiológico se hará realizará un filtrado, preprocesamiento,  extracción de características y su clasificación. </p>

<p align="center">
 <img width="500" height="300" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/10.%20Procesamiento%20de%20la%20se%C3%B1al%20EEG/Im%C3%A1genes/EEG%20waves.png">
<h5 align="center">
  <i>Figura 1. Ondas EEG [3]. </i></div>
<br /> </p>
</h5>
   
- Ondas cerebrales beta (β) (13-30 Hz):
Estas ondas tienen la frecuencia más alta entre todas las ondas cerebrales. Se generan en los lóbulos frontales del cerebro y son ondas irregulares. Normalmente dominan los estados de conciencia durante la vigilia y ocurren cuando la atención se dirige hacia tareas cognitivas y otras actividades. Se producen cuando una persona está alerta, concentrada, atenta, enfocada y comprometida en la toma de decisiones o resolución de problemas. La ansiedad y la depresión también se han relacionado con las ondas beta, ya que pueden conducir a patrones de pensamiento repetitivos. Cuando alguien está participando en una conversación, hay un aumento en las ondas beta.

- Ondas cerebrales alfa (α) (8-10 Hz):
Las ondas alfa son muy regulares y sincronizadas. Se generan en los lóbulos parietales u occipitales. Se producen cuando los ojos están cerrados y durante actividades como el yoga y la meditación, cuando la mente está alerta y la memoria está potenciada. Cuando un pintor o músico está realizando una obra creativa, se emiten estas ondas. Se generan en un estado de relajación y ayudan a mejorar la memoria. Hans Berger solo pudo registrar las ondas alfa, por lo que también se conocen como ondas de Berger.

- Ondas cerebrales theta (θ) (4-7 Hz):
Estas ondas se producen en el hipocampo del cerebro. Se generan cuando la mente está decepcionada. Durante el sueño REM, se producen las ondas theta. Justo antes de quedarnos dormidos y justo después de despertar, cuando la mente no está tan consciente como en el estado de vigilia normal, se generan las ondas theta. También se producen durante la meditación profunda y cuando estamos recordando recuerdos olvidados hace mucho tiempo.

- Ondas cerebrales delta (δ) (2-4 Hz):
Estas ondas se crean durante el estado de sueño profundo y tienen varios efectos terapéuticos. Ayudan a sanar perturbaciones. Cuando nuestro estado de ánimo es bajo o nos sentimos tristes, y después de un sueño profundo nos despertamos sintiéndonos energéticos, es porque el cerebro ha producido ondas delta [3].

 

<a id = "materiales"></a>  
<h2 style = "text-align: center;">Materiales y equipos</h2>

<div align="center">

|   **Dispositivo**   | **Descripción** |  **Imagen**  |
|:-------------------:|:---------------:|:------------:|
|      Laptop      | Una laptop equipada con Python, un lenguaje de programación versátil y poderoso, es ideal para realizar tareas de programación y análisis de datos en entornos de laboratorio. |<img width="200" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/6.%20Filtros%20IIR%20y%20FIR/Im%C3%A1genes/68af906e-92c2-4096-ab4c-06e60cba53f1.jpg">|
|      Database     | La Base de base datos de PhysioNet cuenta con acceso abierto a usarios para la extración de registros de estudios de señales fisilógicas. |<img width="200" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/10.%20Procesamiento%20de%20la%20se%C3%B1al%20EEG/Im%C3%A1genes/physionet.png">|
</div>

</p>
<a id = "metodo" style></a>
<h2 style = "text-align: center;">Metodología</h2>

#### Filtrado <br />
   Utilizamos un filtro Butterworth pasabanda con frecuencias de corte de 3 Hz a 30 Hz y un orden de 2. Este tipo de filtro es efectivo para eliminar el ruido de baja y alta frecuencia que puede contaminar las señales EEG, mejorando así la calidad de las señales para análisis posteriores. El filtro Butterworth se selecciona por su respuesta de fase lineal y su capacidad para mantener la forma de la señal dentro del rango de frecuencias de interés[4][5]. <br />

#### Normalización de Señales <br />
Después del filtrado, las señales EEG se normalizan utilizando el software MNE (MNE-Python). Este proceso implica crear una estructura de información con las características de las señales y aplicar un filtro adicional para asegurar que la señal esté en un rango controlado. La normalización ayuda a reducir la variabilidad entre diferentes señales y facilita la comparación y el análisis posterior [4]. <br />

#### Wavelet
La transformada wavelet discreta (DWT) se utiliza para descomponer las señales EEG en diferentes niveles de detalle utilizando la wavelet 'db4' de Daubechies. Este método es útil para analizar características en diferentes escalas de tiempo y frecuencia, permitiendo una extracción de características más detallada y precisa [4][5].
Los coeficientes obtenidos de la transformada wavelet se normalizan calculando la media y la desviación estándar de cada conjunto de coeficientes. Este paso es crucial para asegurar que los coeficientes estén en un rango comparable y evitar que valores extremos afecten el análisis [5]. <br />

#### Cálculo SNR (Signal to Noise Ratio)

El SNR se calcula para evaluar la calidad de las señales preprocesadas. Se define como la relación entre la potencia de la señal útil y la potencia del ruido presente en la señal. Este cálculo es esencial para cuantificar la mejora en la calidad de las señales después del preprocesamiento [4][5].

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

#### Señal adquirida :

</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/10.%20Procesamiento%20de%20la%20se%C3%B1al%20EEG/Im%C3%A1genes/RAW%20SIGNALS.png">
</p>
<h5 align="center">
  Figura 2: Señal obtenida en python: Actividad 1 [Elaboración propia].
</h5>
El primer conjunto de gráficos muestra las señales EEG originales de la base de datos , en este, se observan varios canales (TP9, AF7, AF8, TP10, Right AUX). Donde podemos observar que las señales contienen una cantidad significativa de ruido y hay picos notables con variaciones en la amplitud. Estas variaciones podrían deberse a movimientos musculares, parpadeos o interferencias electromagnéticas.

Procemos a la aplicación de los filtros mencionados, primero el filtro pasabanda, seguido por el filtrado IIR.</p>

#### Normalización (Pasabanda y filtro IIR):
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/10.%20Procesamiento%20de%20la%20se%C3%B1al%20EEG/Im%C3%A1genes/NORMALIZED%20AND%20FILTERED%20SIGNALS.png"">
</p>
<h5 align="center">
  Figura 3: Señal normalizada y filtrada en python previamente filtrada [Elaboración propia].
</h5>
Conjunto de gráficos muestra las señales EEG filtradas y normalizadas utilizando un filtro iir pasa banda (0.5-25 Hz) para centrarse en las bandas de frecuencia típicas del EEG (delta, theta, alfa, beta) [6].
Podemos ver que el filtrado reduce significativamente el ruido y que las variaciones de amplitud son más suaves. Para la normalización se utilizó la biblioteca MNE, esto implica aplicar un filtro pasa banda adicional y ajustar las señales para que tengan una amplitud comparable.

#### Wavelet:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/10.%20Procesamiento%20de%20la%20se%C3%B1al%20EEG/Im%C3%A1genes/Wavelet%20and%20coeff.png">
</p>
<h5 align="center">
  Figura 4: Señal obtenida en python: filtrado wavelet[Elaboración propia]
</h5>
Conjunto de gráficos se aplica una transformada wavelet discreta (DWT) a las señales normalizadas para extraer características tiempo-frecuencia. Esto es útil para capturar eventos transitorios en los datos EEG [5].
</p>

#### FFT DE LA SEÑAL NORMALIZADA:
</p>
<p align="center">
<img width="800" height="600" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/10.%20Procesamiento%20de%20la%20se%C3%B1al%20EEG/Im%C3%A1genes/FFT%20OF%20SIGNALS.png">
</p>
<h5 align="center">
  Figura 5: FFT de la señal normalizada obtenida en python: Extracción de características.[Elaboración propia]
</h5>
En la figura 5 se aprecia el conjunto de gráficos de la magnitud de la FFT de las señales EEG filtradas y normalizadas en decibelios (dB). </p>

<a id = "explic"></a>
<h2 style = "text-align: center;">Resumen y Discusión</h2>

### Resumen

Este laboratorio se centra en el procesamiento de señales EEG utilizando bases de datos de PhysioNet. El objetivo es mejorar la calidad de las señales mediante filtrado, preprocesamiento, y extracción de características relevantes. Se aplicó un filtro Butterworth de cuarto orden para eliminar el ruido de las señales originales y se normalizaron los datos utilizando la biblioteca MNE y una red generativa adversaria (GAN) para asegurar la homogeneidad de los datos. Posteriormente, se utilizó la transformada wavelet discreta (DWT) para descomponer y limpiar las señales, facilitando la captura de eventos transitorios.

El análisis incluyó la identificación de ondas cerebrales, evaluando su presencia y características en las señales filtradas y normalizadas. Los resultados demostraron una significativa reducción del ruido y una mayor claridad en los patrones de las ondas cerebrales. 

### Discusión

En la figura de la señal obtenida del data base, se observa una notable cantidad de ruido, con una amplitud que varía entre -1000 y 1000 en el eje Y, que representa la frecuencia en Hz. El eje X muestra el tiempo en milisegundos. Después de aplicar el filtrado pasa banda e IIR, se nota una significativa reducción de las frecuencias altas (mayores a 25 Hz) y bajas (menores a 0.5 Hz), lo que disminuye el ruido. Este proceso se continúa con la normalización utilizando la biblioteca MNE, destacándose así los eventos transitorios de mayor frecuencia.

Finalmente, al realizar la FFT de la señal normalizada, los valores de amplitud obtenidos oscilan entre -100 y 0 dB. Sin embargo, sería esperable observar pequeñas amplitudes positivas comparables con las ondas beta, alfa, theta y delta, alineándose con las características típicas de las frecuencias cerebrales. Este proceso integral asegura una señal más limpia y precisa para el análisis, facilitando la identificación de las distintas ondas cerebrales[6],[7],[8],[9].




<a id = "Bibliografía"></a>
<h2 style = "text-align: center;">Bibliografía</h2>

[1] A. Chaddad, Y. Wu, R. Kateb, and A. Bouridane, “Electroencephalography signal processing: A comprehensive review and analysis of methods and techniques,” Sensors, vol. 23, no. 14, p. 6434, 2023.</p>
[2] Y. Zhao, F. He, and Y. Guo, “EEG Signal Processing Techniques and Applications,” Sensors, vol. 23, no. 22. MDPI, p. 9056, 2023.</p>
[3] K. N. Singh, S. S. Patra, S. Samantaray, S. Jena, J. K. Mantri, and C. Misra, “Automatic Sleep EEG Classification with Ensemble Learning Using Graph Modularity,” in *Biomedical Signal Processing for Healthcare Applications*, 1st ed., CRC Press, 2021, pp. 1-24. DOI: 10.1201/9781003147817-1.</p>
[4] A. Keil et al., “Committee report: publication guidelines and recommendations for studies using electroencephalography and magnetoencephalography,” Psychophysiology, vol. 51, no. 1, pp. 1–21, 2014</p>
[5] N. Ahmadi, Y. Pei, and M. Pechenizkiy, “Detection of alcoholism based on EEG signals and functional brain network features extraction,” in 2017 IEEE 30th International Symposium on Computer-Based Medical Systems (CBMS), IEEE, 2017, pp. 179–184.</p>
[6]Y. An, H. K. Lam, and S. H. Ling, “Auto-Denoising for EEG Signals Using Generative Adversarial Network,” Sensors, vol. 22, no. 5, p. 1750, Feb. 2022, doi: 10.3390/s22051750.</p>
[7]	I. H. Elshekhidris, M. B. MohamedAmien, and A. Fragoon, “WAVELET TRANSFORMS FOR EEG SIGNAL DENOISING AND DECOMPOSITION,” Int. J. Adv. SIGNAL IMAGE Sci., vol. 9, no. 2, Art. no. 2, Dec. 2023, doi: 10.29284/ijasis.9.2.2023.11-28.</p>
[8]	M. Jas et al., “MEG/EEG group study with MNE: recommendations, quality assessments and best practices.” Dec. 28, 2017. doi: 10.1101/240044.</p>

[9] «BITalino (r)evolution Lab Guide»</p>


