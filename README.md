# SWUpdates-Alert

[![Software Checks](https://github.com/gioxx/SWUpdates-Alert/actions/workflows/software.yml/badge.svg)](https://github.com/gioxx/SWUpdates-Alert/actions/workflows/software.yml)

**[Vai alla versione in italiano](#versione-italiana)**

## English version

SWUpdates-Alert automates version checks for various software and sends a Telegram notification whenever a new release is published. Each script in the repository monitors a specific application and keeps the related file inside the `updates/` folder up to date.

**Follow the Telegram channel**: <https://t.me/SWUpdate>

For more details about the project, see the dedicated article on Gioxx's Wall: <https://gioxx.org/2022/09/19/swupdates-alert-rimani-aggiornato-sul-rilascio-delle-applicazioni/>

## Monitored software

| Software Name            | Description                                                      | Website |
|------------------------|------------------------------------------------------------------|--------------|
| 7-Zip  | 7-Zip is a free and open-source file archiver. | [7-zip.org](https://www.7-zip.org/) |
| FileZilla  | FileZilla is a free and open-source, cross-platform FTP application. | [filezilla-project.org](https://filezilla-project.org/) |
| Firefox (stable and ESR)  | Mozilla Firefox, or simply Firefox, is a free and open-source web browser developed by the Mozilla Foundation and its subsidiary, the Mozilla Corporation. | [mozilla.org/firefox](https://www.mozilla.org/firefox/) |
| Firma4NG  | firma4ng is a professional digital signature application, compatible with Windows, Linux and Mac OS X operating systems. | [infocamere.it](https://id.infocamere.it/download_software.html) |
| ImageMagick  | ImageMagick is a free and open-source cross-platform software suite for displaying, creating, converting, modifying, and editing raster images. | [imagemagick.org](https://imagemagick.org/) |
| IrfanView  | IrfanView is a fast and compact image viewer for Windows. | [irfanview.com](https://www.irfanview.com/) |
| NAPS2  | NAPS2 is free and open source scanning software for Windows, Mac and Linux. | [naps2.com](https://www.naps2.com/) |
| Notepad++  | Notepad++ is a text and source code editor for use with Microsoft Windows. It supports tabbed editing, which allows working with multiple open files in one window. | [notepad-plus-plus.org](http://notepad-plus-plus.org/) |
| PuTTY  | PuTTY is a free and open-source terminal emulator, serial console and network file transfer application. | [chiark.greenend.org.uk/~sgtatham](https://www.chiark.greenend.org.uk/~sgtatham/putty/) |
| Win32 Content Prep Tool  | Microsoft Win32 Content Prep Tool converts application installation files into the .intunewin format. | [github.com/microsoft](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool) |
| XML Notepad  | XML Notepad is an open-source XML editor written by Chris Lovett and published by Microsoft. | [microsoft.github.io/XmlNotepad](http://microsoft.github.io/XmlNotepad/) |

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
| Nome dell'applicazione            | Descrizione                                                      | Sito web |
|------------------------|------------------------------------------------------------------|--------------|
| 7-Zip  | 7-Zip è un archiviatore di file gratuito e open-source. | [7-zip.org](https://www.7-zip.org/) |
| FileZilla  | FileZilla è un'applicazione FTP multipiattaforma, gratuita e open-source. | [filezilla-project.org](https://filezilla-project.org/) |
| Firefox (stable and ESR)  | Mozilla Firefox, o semplicemente Firefox, è un browser web gratuito e open-source sviluppato dalla Mozilla Foundation e dalla sua filiale, la Mozilla Corporation. | [mozilla.org/firefox](https://www.mozilla.org/firefox/) |
| Firma4NG  | firma4ng è un’applicazione professionale di firma digitale, compatibile con i sistemi operativi Windows, Linux e Mac OS X. | [infocamere.it](https://id.infocamere.it/download_software.html) |
| ImageMagick  | ImageMagick è una suite software multipiattaforma gratuita e open-source per la visualizzazione, la creazione, la conversione, la modifica e l'editing di immagini raster. | [imagemagick.org](https://imagemagick.org/) |
| IrfanView  | IrfanView è un visualizzatore di immagini veloce e compatto per Windows. | [irfanview.com](https://www.irfanview.com/) |
| NAPS2  | NAPS2 è un software di scansione gratuito e open source per Windows, Mac e Linux. | [naps2.com](https://www.naps2.com/) |
| Notepad++  | Notepad++ è un editor di testo e codice sorgente da utilizzare con Microsoft Windows. Supporta l'editing a schede, che consente di lavorare con più file aperti in un'unica finestra. | [notepad-plus-plus.org](http://notepad-plus-plus.org/) |
| PuTTY  | PuTTY è un emulatore di terminale, una console seriale e un'applicazione per il trasferimento di file in rete gratuita e open-source. | [chiark.greenend.org.uk/~sgtatham](https://www.chiark.greenend.org.uk/~sgtatham/putty/) |
| Win32 Content Prep Tool  | Microsoft Win32 Content Prep Tool converte i file di installazione delle applicazioni nel formato .intunewin. | [github.com/microsoft](https://github.com/microsoft/Microsoft-Win32-Content-Prep-Tool) |
| XML Notepad  | XML Notepad è un editor XML open-source scritto da Chris Lovett e pubblicato da Microsoft. | [microsoft.github.io/XmlNotepad](http://microsoft.github.io/XmlNotepad/) |

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
