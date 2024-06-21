<h1 style="text-align: center;">Laboratorio 11: Edge impulse (EI)</h1>
Integrante: 

- Juan Jose Sandoval
<a id = "Informe edge impulse" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- Crear un proyecto en EI por cada señal trabaja en clases. Es decir, deben tener 3 proyectos en EI para EMG, ECG, EEG. Las señales deben estar etiquetadas, ejemplo para ECG<br />

<h2 style = "text-align: center;">Código en python</h2>

```python
# Install requests via: `pip3 install requests`
import requests
import os

api_key = 'ei_bbfc3b5b7b596d3a3d2ca210cede07d0046857a3e252a359a2163bee06e505d2'
# Add the files you want to upload to Edge Impulse
files = [
    '/content/EMG/EMG_Reposo.csv'
]
# # Replace the label with your own.
label = 'car'
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

