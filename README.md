# Fang das Wollknäuel
 * **Spiele programmieren mit Python und Pygame**,
c't 14/2018, S. 136, apoi@ct.de 
 * **Spiele programmieren mit Python und Pygame, Teil 2**, 
c't 17/2018, S. 128, apoi@ct.de

Fragen zum Repository an pmk@ct.de

## Projektstruktur

| Datei                                                                          | Beschreibung             |
| -------------------------------------------------------------------------------|--------------------------|
| [knaeuljagd.py](https://github.com/pinae/Knaeuljagd/blob/master/knaeuljagd.py) | Modul mit Spielelementen |
| [main.py](https://github.com/pinae/Knaeuljagd/blob/master/main.py)             | Spiel-Skript             |
| [katze.png](https://github.com/pinae/Knaeuljagd/blob/master/katze.png)         | Katzen-Spielfigur        |
| [falter.png](https://github.com/pinae/Knaeuljagd/blob/master/falter.png)       | ZufallsObjekt (top)      | 
| [maus.png](https://github.com/pinae/Knaeuljagd/blob/master/maus.png)           | ZufallsObjekt (top)      | 
| [knaeul.png](https://github.com/pinae/Knaeuljagd/blob/master/knaeul.png)       | ZufallsObjekt (top)      | 
| [hund.png](https://github.com/pinae/Knaeuljagd/blob/master/hund.png)           | ZufallsObjekt (flop)     | 
| [laerm.png](https://github.com/pinae/Knaeuljagd/blob/master/laerm.png)         | ZufallsObjekt (flop)     | 
| [wasser.png](https://github.com/pinae/Knaeuljagd/blob/master/wasser.png)       | ZufallsObjekt (flop)     | 

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