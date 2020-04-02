# Fang das Wollknäuel
## Spiele programmieren mit Python und Pygame
c't 14/2018, S. 136, apoi@ct.de 

Fragen zum Repository an pmk@ct.de

## Projektstruktur

| Datei                                                                          | Beschreibung      |
| -------------------------------------------------------------------------------|-------------------|
| [katzensolo.py](https://github.com/pinae/Knaeuljagd/blob/master/katzensolo.py) | Katzen-Modul      |
| [main.py](https://github.com/pinae/Knaeuljagd/blob/master/main.py)             | Spiel-Skript      |
| [katze.png](https://github.com/pinae/Knaeuljagd/blob/master/katze.png)         | Katzen-Spielfigur | 

## Intsallation und Abhängigkeiten

Das Projekt nutzt PyGame. Auf vielen Systemen können Sie 
PyGame einfach als Paket nachinstallieren.

PyGame ist auch im Python-Package-Index (PyPI) enthalten:

```shell script
pip install pygame
```

### Virtualenv

Falls Sie das Spiel von der Python-Installation des Systems
abgrenzen möchten, richten Sie mit folgenden Befehlen unter
Linux und MacOS eine virtuelle Umgebung (Virtualenv) ein:

```shell script
python3 -m venv env
source env/bin/activate
```

Installieren Sie dort alle Abhängigkeiten:

```shell script
pip install -U pip wheel
pip install -r requirements.txt
```

### Arch Linux

Damit `pip` PyGame auf Arch Linux erfolgreich installiert, 
braucht es folgende Systempakete:

```shell script
pacman -S libmikmod portmidi sdl_image sdl_mixer sdl_ttf smpeg
```

## Ausführen und spielen

Starten Sie das Spiel mit:

```shell script
python main.py
```