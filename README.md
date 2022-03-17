# Descrizione progetto

Progetto di Explorative Data Analysis su dati sample di Google Analytics, provenienti da Google BigQuery

# Config

## Librerie Python utilizzate

Nel progetto è presente l'environment conda. Sono state installate le seguenti librerie, in versione latest in fase di progetto; si riportano qui le versioni per documentazione.

```
numpy 1.22.3
pandas 1.4.1
matplotlib 3.5.1
seaborn 0.11.2
google-cloud 0.34.0
google-cloud-bigquery 2.34.2
google-cloud-bigquery-storage 2.13.0
pyarrow 7.0.0
ipykernel 6.9.2
```

## Config BigQuery

Per effettuare il download dei dati di BigQuery occorre scaricare il token di accesso all'account, seguendo questi passi:
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
- Rinominare il file "bq_key.json"
- Inserire il file nella root di progetto