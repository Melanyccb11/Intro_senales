<a id = "Informe edge impulse" style></a>
<h2 style = "text-align: center;">Objetivos</h2>
- Subir mediante un codigo en python las señales adquieridas a impulse edge <br />

<h2 style = "text-align: center;">Objetivos</h2>
'import requests
import os

api_key = 'ei_bbee1514cc1ac4c96a9a578cbcc014cc2cd536dd8321d0b213550afe0b3993be'
# Add the files you want to upload to Edge Impulse
files = [
    '/content/ECG_hiperventilación.csv',
]
# # Replace the label with your own.
label = 'ecg_hiperventilacion'
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
          res.status_code, res.content)'
