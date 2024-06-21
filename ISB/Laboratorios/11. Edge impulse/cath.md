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
[nya]([https://www.ejemplo.com](https://studio.edgeimpulse.com/public/431087/live
))
