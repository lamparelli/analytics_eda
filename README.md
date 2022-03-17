# Config python

Installare le seguenti librerie

```
pip install numpy 1.22.3
pip install pandas 1.4.1
pip install matplotlib 3.5.1
pip install seaborn 0.11.2
pip install google-cloud 0.34.0
pip install google-cloud-bigquery 2.34.2
pip install google-cloud-bigquery-storage 2.13.0
pip install pyarrow 7.0.0
pip install ipykernel 6.9.2
```

# Config BigQuery

- Creare account

- Nel progetto di default, creare un dataset

- Nel dataset creato, creare una tabella, impostando la fonte di dati (es. un csv)

- Andare dal menu laterale in API and Services -> Credentials

- Premere Create credentials -> Service account

- Impostare un nome a scelta (es. "mio_nome_service_account"), e premere continua

- Nella schermata successiva, come ruolo, impostare BigQuery Admin

- Premere continua e salva

- Dalla schermata risultante, in basso, clickare su mio_nome_service_account

- Nella pagina di mio_nome_service_account, andare su Keys nel menu

- Premere Add key -> Premere Create new key -> Lasciare default JSON -> Confermare