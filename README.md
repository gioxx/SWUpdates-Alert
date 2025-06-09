# SWUpdates-Alert
[![Software Checks](https://github.com/gioxx/SWUpdates-Alert/actions/workflows/software.yml/badge.svg)](https://github.com/gioxx/SWUpdates-Alert/actions/workflows/software.yml)

**Segui il canale Telegram!**
https://t.me/SWUpdate

**Vuoi saperne di più sul progetto?** Leggi l'articolo dedicato su Gioxx's Wall:
https://gioxx.org/2022/09/19/swupdates-alert-rimani-aggiornato-sul-rilascio-delle-applicazioni/

Alcune fonti di aggiornamento utilizzano certificati HTTPS obsoleti. In questi
casi gli script disabilitano temporaneamente il controllo dei certificati per
consentire il download dei dati.

Quando non è possibile determinare la versione di un'applicazione, il controllo viene ignorato e il file di versione non viene aggiornato.

## Variabili d'ambiente

Gli script inviano notifiche su Telegram. Prima dell'esecuzione occorre impostare le seguenti variabili d'ambiente:

* `TGRAMTOKEN`: token del bot Telegram
* `TGRAMCHATID`: ID della chat alla quale inviare i messaggi
