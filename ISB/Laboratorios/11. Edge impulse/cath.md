<h1 style="text-align: center;">Laboratorio 11: Edge impulse (EI)</h1>
Integrante: 

- Catherine Boggio
<a id = "Informe edge impulse" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- Crear un proyecto en EI por cada señal trabaja en clases. Es decir, deben tener 3 proyectos en EI para EMG, ECG, EEG. Las señales deben estar etiquetadas, ejemplo para ECG<br />

<h2 style = "text-align: center;">Código en python</h2>

```python
import requests
import os

api_key = 'ei_bbee1514cc1ac4c96a9a578cbcc014cc2cd536dd8321d0b213550afe0b3993be'
# Add the files you want to upload to Edge Impulse
files = [
    '/content/asistolia.csv',
]
# # Replace the label with your own.
label = 'ecg_asistolia'
# Upload the file to Edge Impulse using the API, and print the response.
res = requests.post(url='https://ingestion.edgeimpulse.com/api/training/files',
                    headers={
                        'x-label': label,
                        'x-api-key': api_key,
                    },
                    # Creating the data payload for the request.
                    files=(('data', (os.path.basename(i), open(
                        i, 'rb'), 'application/csv')) for i in files)
                    )

if (res.status_code == 200):
    print('Uploaded file(s) to Edge Impulse\n', res.status_code, res.content)
else:
    print('Failed to upload file(s) to Edge Impulse\n',
          res.status_code, res.content)
```
<h2 style = "text-align: center;">Links de proyecto</h2>

1. ECG (https://studio.edgeimpulse.com/public/431087/live)
2. EEG (https://studio.edgeimpulse.com/public/431125/live)  
3. EMG (https://studio.edgeimpulse.com/public/431137/live)

<h2 style = "text-align: center;">Imagenes</h2>

### ECG
 </p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/ecg_asistolia.png">
<h5 align="center">
  <i>Figura 1. Señal de ECG de un paciente con asistolia </i></div>
<br /> </p>
</h5>

 </p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/ecg_RSN.png">
<h5 align="center">
  <i>Figura 2.Señal RSN en un ECG </i></div>
<br /> </p>
</h5>

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/ecg_hiperventilacion.png">
<h5 align="center">
  <i>Figura 3. Señal hiperventilación en un ECG </i></div>
<br /> </p>
</h5>

### EEG
</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/eeg_ejerciomate.png">
<h5 align="center">
  <i>Figura 4. Señal de EEG tras realizar un ejercicio matemático </i></div>
<br /> </p>
</h5>

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/eeg_primeroojoscerrados.png">
<h5 align="center">
  <i>Figura 5. Señal EEG abriendo y cerrando los ojos </i></div>
<br /> </p>
</h5>
    
### EMG

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/EMG_Oposici%C3%B3n.png">
<h5 align="center">
  <i>Figura 6. Señal EMG en haciendo un poco de fuerza </i></div>
<br /> </p>
</h5>

</p>
<p align="center">
 <img width="250" height="150" src="https://github.com/Melanyccb11/Intro_senales/blob/main/ISB/Laboratorios/11.%20Edge%20impulse/imagenes%20cath/EMG_resposo.png">
<h5 align="center">
  <i>Figura 7. Señal ENG en reposo </i></div>
<br /> </p>
</h5>
