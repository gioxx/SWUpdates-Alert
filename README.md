# SWUpdates-Alert

[![Software Checks](https://github.com/gioxx/SWUpdates-Alert/actions/workflows/software.yml/badge.svg)](https://github.com/gioxx/SWUpdates-Alert/actions/workflows/software.yml)

**[Vai alla versione in italiano](#versione-italiana)**

## English version

SWUpdates-Alert automates version checks for various software and sends a Telegram notification whenever a new release is published. Each script in the repository monitors a specific application and keeps the related file inside the `updates/` folder up to date.

**Follow the Telegram channel**: <https://t.me/SWUpdate>

For more details about the project, see the dedicated article on Gioxx's Wall: <https://gioxx.org/2022/09/19/swupdates-alert-rimani-aggiornato-sul-rilascio-delle-applicazioni/>

## Monitored software
- 7-Zip
- FileZilla
- Firefox (stable and ESR)
- Firma4NG
- ImageMagick
- NAPS2
- Notepad++
- PuTTY
- Win32 Content Prep Tool
- XmlNotepad

Daily checks run via [GitHub Actions](.github/workflows/software.yml) which launches each script independently.

## Requirements
- Python 3.10 or later
- Dependencies listed in [`requirements.txt`](requirements.txt)

Install the dependencies with:
```bash
pip install -r requirements.txt
```

### Environment variables
The scripts send notifications using a Telegram bot. Before running them define:

- `TGRAMTOKEN` – Telegram bot token
- `TGRAMCHATID` – ID of the chat or channel that receives the messages

Some update sources use outdated HTTPS certificates, so SSL verification is temporarily disabled when downloading the data (for example this happens with FileZilla). When a software version cannot be determined, the script is skipped and the file under `updates/` is left unchanged.

## Manual execution
Each script can be run individually, for example:
```bash
python sw_firefox.py
```
If a new version is found the file in the `updates/` folder is updated and a message is sent on Telegram.

## Tests
Unit tests based on `unittest` are available. Run them with:
```bash
python -m unittest
```

## Contributing
1. Open an *issue* using the **New Software Check** template if you want to request the monitoring of new software.
2. Fork the project and open a *pull request* with your changes.
3. Make sure all tests pass before submitting the PR.

## License
This project is released under the [MIT](LICENSE) license.

## Versione italiana

SWUpdates-Alert automatizza il controllo delle versioni di diversi software e invia una notifica su Telegram quando viene pubblicato un nuovo rilascio. Ogni script della repository monitora un'applicazione specifica e mantiene aggiornato il file corrispondente all'interno della cartella `updates/`.

**Segui il canale Telegram**: <https://t.me/SWUpdate>

Per maggiori dettagli sul progetto puoi leggere l'articolo dedicato su Gioxx's Wall: <https://gioxx.org/2022/09/19/swupdates-alert-rimani-aggiornato-sul-rilascio-delle-applicazioni/>

## Software monitorato
- 7-Zip
- FileZilla
- Firefox (stable ed ESR)
- Firma4NG
- ImageMagick
- NAPS2
- Notepad++
- PuTTY
- Win32 Content Prep Tool
- XmlNotepad

L'esecuzione quotidiana avviene tramite [GitHub Actions](.github/workflows/software.yml) che lancia ogni script in modo indipendente.

## Requisiti
- Python 3.10 o superiore
- Dipendenze elencate in [`requirements.txt`](requirements.txt)

Installa le dipendenze con:
```bash
pip install -r requirements.txt
```

### Variabili d'ambiente
Gli script inviano notifiche tramite un bot Telegram. Prima dell'esecuzione definisci:

- `TGRAMTOKEN` – token del bot Telegram
- `TGRAMCHATID` – ID della chat o del canale destinatario

Alcune fonti di aggiornamento utilizzano certificati HTTPS obsoleti: in questi casi la verifica SSL viene disattivata temporaneamente per consentire il download dei dati (ad esempio accade con FileZilla).
Quando non è possibile determinare la versione di un software, lo script viene ignorato e il file in `updates/` rimane invariato.

## Esecuzione manuale
Ogni script può essere lanciato singolarmente, ad esempio:
```bash
python sw_firefox.py
```
Se viene rilevata una nuova versione il file nella cartella `updates/` viene aggiornato e un messaggio viene inviato su Telegram.

## Test
Sono presenti test unitari basati su `unittest`. Per eseguirli:
```bash
python -m unittest
```

## Come contribuire
1. Apri una *issue* utilizzando il template **New Software Check** se desideri proporre il monitoraggio di un nuovo software.
2. Effettua una *fork* del progetto e apri una *pull request* con le tue modifiche.
3. Assicurati che i test passino prima di inviare la PR.

## Licenza
Questo progetto è distribuito sotto licenza [MIT](LICENSE).
