<h1 style="text-align: center;">Home Study Environments: Assessment of Posture and Muscle Fatigue Using Surface Electromyography in the Context of Virtual Education After the Pandemic</h1>
<h1 style="text-align: center;">Entornos de Estudio en Casa: Evaluación de la Postura y Fatiga Muscular Mediante Electromiografía Superficial en el Contexto de la Educación Virtual Después de la Pandemia</h1>

Bienvenidos al repositorio del **Grupo 2** del curso *Introducción a Señales Biomédicas*. Somos un equipo de estudiantes de Ingeniería Biomédica de las universidades UPCH y PUCP del semestre 2024-1. 


<h2 style="text-align: center;">Tabla de Contenidos</h2>

1. [Resúmen](#intro)
2. [Motivación](#problem)
3. [Principales hallazgos](#Tema)
4. [Links importantes](#sol)
5. [Referencia](#biblio)


<a id = "intro"></a>  
<h2 style = "text-align: center;">Resúmen</h2>
La pandemia de COVID-19 generó un cambio rápido hacia la educación virtual, aumentando las preocupaciones sobre la ergonomía y la postura de los estudiantes universitarios en casa. Este proyecto busca optimizar los entornos de estudio en el hogar evaluando la postura y la fatiga muscular usando electromiografía superficial (EMG). Se identifican y cuantifican problemas musculoesqueléticos causados por configuraciones no ergonómicas en el hogar, analizando la relación entre el tiempo prolongado frente a la pantalla, la mala postura y la fatiga muscular. Utilizando el kit EMG de BITalino (r)evolution y el software Kinovea, se evaluaron estudiantes universitarios que estudiaron virtualmente durante la pandemia. Los datos se procesaron para proponer recomendaciones ergonómicas que mejoren la postura, reduzcan la fatiga muscular y promuevan un entorno de estudio más saludable para un mejor rendimiento académico.

<a id = "problem"></a>
<h2 style = "text-align: center;">Motivación</h2>

La motivación principal de este proyecto radica en la necesidad urgente de optimizar los entornos de estudio en casa para garantizar que los estudiantes puedan aprender de manera efectiva y saludable. Al proporcionar datos cuantitativos y análisis detallados sobre la relación entre la postura y la fatiga muscular, este proyecto no solo contribuirá a mejorar la salud física de los estudiantes, sino que también fomentará una mayor concientización sobre la importancia de ambientes de estudio ergonómicamente adecuados. En última instancia, se espera que estas mejoras conduzcan a un mejor rendimiento académico y una mayor calidad de vida para los estudiantes universitarios en el Perú.

<a id = "sol"></a>
<h2 style = "text-align: center;">Principales hallazgos</h2>

La pandemia de COVID-19 obligó a las instituciones educativas a adoptar métodos de enseñanza virtuales, generando preocupaciones sobre la ergonomía y la postura de los estudiantes universitarios. La falta de ambientes ergonómicos en el hogar puede llevar a posturas deficientes y aumentar el riesgo de síntomas musculoesqueléticos [1]. 

Durante la pandemia, muchos estudiantes que recibieron clases en línea desde casa estuvieron expuestos a un riesgo postural medio debido a entornos domésticos no ergonómicos, como sofás y camas [2]. El uso prolongado de dispositivos móviles y computadoras en posiciones inadecuadas ha incrementado problemas como dolor de cuello, espalda baja y hombros [3], [4], [5]. Estas condiciones afectan tanto el bienestar físico de los estudiantes como su rendimiento académico y calidad de vida [4].

En Perú, un estudio en una universidad de Lima encontró que el 60.3% de los estudiantes experimentaron molestias musculoesqueléticas durante sus clases virtuales, reportando dolor en el cuello, espalda baja y hombros [6]. Otro estudio nacional reveló que el 20% de los estudiantes interrumpieron sus estudios durante el primer semestre de 2020 debido a la falta de acceso a servicios básicos y tecnología adecuada. 

A pesar de las políticas implementadas para mejorar la infraestructura tecnológica y la capacitación docente, persisten desafíos relacionados con la equidad y el acceso a recursos adecuados [7]. La continuidad de la educación virtual subraya la necesidad de entornos de estudio óptimos en casa para garantizar un aprendizaje efectivo y saludable [8], [9].

En los resultados, por medio de fotogametría, los datos indican que la postura en el sofá durante las clases virtuales no es adecuada debido a los valores obtenidos en el ángulo cráneo-vertebral. En la posición en sofá, la mediana del ángulo cráneo-vertebral es 57.75°, con una desviación estándar de 17.15°, significativamente mayor que en la silla (media de 51.9° y desviación estándar de 6.23°). En este caso la media no ha sido tomada en cuenta como relevante debido a la alta varianza. Estos resultados sugieren una mayor variabilidad y una alineación inadecuada de la columna cervical en el sofá. La cual muestra una peor alineación postural, con valores fuera del rango recomendado para todos los sujetos.

Por parte de EMG, el análisis estadístico, los valores obtenidos para los sujetos 1 y 2 indican una actividad muscular sostenida, lo que puede sugerir fatiga muscular. Estos hallazgos coinciden con estudios que muestran cómo las posturas no ergonómicas aumentan la actividad muscular y la fatiga. En contraste, los sujetos 2 y 4 muestran menor actividad muscular y menos fatiga, lo que podría reflejar una postura más eficiente [10]. En general, los parámetros extraídos de las señales EMG proporcionan una visión detallada de cómo las posturas adoptadas durante el estudio en casa pueden afectar la actividad muscular y la fatiga.

<p align="center">
 <img width="500" height="300" src="Software/Imagenes finales/Estadistica/TABLA_ESTADISTICA.png ">
<h5 align="center">
  <i>Tabla 1. Estadística con parámetros de cada señal. </i></div>

 
Se generaron diagramas de caja y bigotes como se puede visualizar en la Figura 1 con el fin de ver la distribución de los valores RMS y se calcularon estadísticas descriptivas, incluyendo media, desviación estándar, valores mínimos y máximos, percentiles y coeficiente de variación. Además, se realizó la prueba de Shapiro-Wilk para verificar la normalidad de los valores RMS.

<p align="center">
 <img width="500" height="300" src="Software/Imagenes finales/Estadistica/DIAGRAMA_CAJA_BIGOTES.png">
<h5 align="center">
  <i> Figura 1. Diagrama de caja y bigotes de valores RMS de cada persona analizada. </i></div>


Según los resultados de la Tabla 2, el valor F de 191.628421 es muy alto, indicando una variabilidad significativa entre los grupos. El valor-p de 3.488760e-22, mucho menor que 0.05, muestra que las diferencias entre grupos son estadísticamente significativas, permitiendo rechazar la hipótesis nula. El tamaño del efecto (η² parcial) es 0.941069, sugiriendo que la mayor parte de la variabilidad en los valores RMS se debe a diferencias entre los sujetos, indicando una fuerte influencia del factor "Sujeto".

<p align="center">
 <img width="700" height="200" src="Software/Imagenes finales/Estadistica/ANOVA.png">
<h5 align="center">
  <i>Tabla 2. Estadística con parámetros de cada señal.</i></div>


En la Tabla 3, no hubo diferencias significativas entre los sujetos 1 y 2 (p-tukey = 0.101). Hubo diferencias significativas entre los sujetos 1 y 3 (p-tukey = 0.000), con el sujeto 3 mostrando mayores valores RMS, y entre los sujetos 1 y 4 (p-tukey = 0.000), con el sujeto 4 mostrando valores RMS más altos. Entre los sujetos 2 y 3 (p-tukey = 0.000) y los sujetos 2 y 4 (p-tukey = 0.000), también se observaron diferencias significativas, con el sujeto 4 mostrando los mayores valores RMS.

<p align="center">
 <img width="800" height="300" src="Software/Imagenes finales/Estadistica/Grupos.png">
<h5 align="center">
  <i>Tabla 3. Estadística con parámetros de cada señal.</i></div>

<h2 style = "text-align: center;">Links importantes</h2>

- Paper: https://paperswithcode.com/paper/home-study-environments-assessment-of-posture
- Sobre nosotros: https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/1.%20Sobre%20Nosotros/1.%20Sobre%20nosotros.md
- Codigo: https://github.com/Melanyccb11/Intro_senales/tree/main/Software/Codigo%20py


<a id = "biblio"></a>
<h2 style = "text-align: center;">Bibliográfia</h2>


[1]	B. E. Vallespin y Y. Tri Prasetyo, «Posture Analysis of Students doing Online Class at Home during COVID-19 Pandemic», en 2020 IEEE 7th International Conference on Engineering Technologies and Applied Sciences (ICETAS), Kuala Lumpur, Malaysia: IEEE, dic. 2020, pp. 1-6. doi: 10.1109/ICETAS51660.2020.9484281.

[2]	I. Akulwar-Tajane, M. Darvesh, M. Ghule, S. Deokule, y B. Deora, «Medical & Clinical Research», 2020.

[3]	C. Symanzik et al., «Back and neck problems as well as disadvantageous ergonomic behavior patterns in university students: Concomitants of the pandemic?», Sports Orthop. Traumatol., vol. 39, n.o 1, pp. 50-57, mar. 2023, doi: 10.1016/j.orthtr.2022.11.011.

[4]	I. H. Susilowati, L. M. Kurniawidjaja, S. Nugraha, S. M. Nasri, I. Pujiriani, y B. P. Hasiholan, «The prevalence of bad posture and musculoskeletal symptoms originating from the use of gadgets as an impact of the work from home program of the university community», Heliyon, vol. 8, n.o 10, p. e11059, oct. 2022, doi: 10.1016/j.heliyon.2022.e11059.

[5]	P. Gorce y J. Jacquier-Bret, «Postural prevalence, time of day and spent time activities during smartphone weekday use among students: A survey to prevent musculoskeletal disorders», Heliyon, vol. 9, n.o 12, p. e22796, dic. 2023, doi: 10.1016/j.heliyon.2023.e22796.


[6]	Y. F. Alamo Honorio et al., «Cambios en la ergonomía en tiempos de COVID-19 en estudiantes de una universidad Peruana», J Health Med Sci Print, pp. 67-74, 2021.

[7]	M. F. Prada, G. Elacqua, C. Méndez, R. Novella, K. L. Vargas, y D. Vásquez, «El impacto de la crisis del COVID-19 en estudiantes vulnerables de educación superior: el caso de Perú», IDB Publ., mar. 2022, doi: 10.18235/0004149.

[8]	S. LR, «COVID-19 y educación: ¿cómo afectó la pandemia en el aprendizaje de los alumnos? | clases virtuales | clases presenciales | cuarta ola | Minedu | Sociedad | La República». Accedido: 17 de mayo de 2024. [En línea]. Disponible en: https://larepublica.pe/sociedad/2022/07/22/covid-19-y-educacion-como-afecto-la-pandemia-en-el-aprendizaje-de-los-alumnos-clases-virtuales-clases-presenciales-cuarta-ola-minedu

[9]	E. Maza-Córdova, «Una mirada a la educación virtual en el Perú en tiempos de la COVID-19», Rev. Científica Episteme Tekne, vol. 2, n.o 1, Art. n.o 1, ene. 2023, doi: 10.51252/rceyt.v2i1.459.

[10] P. Intolo, B. Shalokhon, G. Wongwech, P. Wisiasut, S. Nanthavanij, and D. G. Baxter, “Analysis of neck and shoulder postures, and muscle activities relative to perceived pain during laptop computer use at a low-height table, sofa and bed,” Work, vol. 63, no. 3, pp. 361–367, 2019


