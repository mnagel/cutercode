INSTALLATION

erfordert die folgende Lib:
* python-qrencode

unter debian unstable:
sudo apt-get install python-qrencode

unter altem debian / ubuntu:
Download von:
http://packages.debian.org/sid/python-qrencode
oder im "depend"-Verzeichnis



BEDIENUNG

Aufruf im Ordner:
./cutercode

Dann den gewünschten Text/Link/... im Textfeld eingeben und auf den Knopf klicken.

Kommandozeilen-Parameter werden zur Darstellung des ersten QR-Codes genutzt.
Beispiel:
./cutercode So kann ein QR-Code aussehen
Sorgt dafür, dass der ein QR-Code mit dem Inhalt "So kann ein QR-Code aussehen" erzeugt wird.



SONSTIGES

python-qrencode manuell bauen:

sudo apt-get install devscripts 
wget http://ftp.de.debian.org/debian/pool/main/p/python-qrencode/python-qrencode_1.01-1.dsc
wget http://ftp.de.debian.org/debian/pool/main/p/python-qrencode/python-qrencode_1.01.orig.tar.gz
wget http://ftp.de.debian.org/debian/pool/main/p/python-qrencode/python-qrencode_1.01-1.debian.tar.gz
dpkg-source -x python-qrencode_1.01-1.dsc
cd python-qrencode-1.01
sudo apt-get install debhelper python-all-dev libqrencode-dev
debuild -us -uc
cd ..
sudo dpkg -i python-qrencode_1.01-1_amd64.deb
sudo apt-get install python-imaging

TODO

* Bugs im Debian-Paket zu python-qrencode
	* dependency auf python-imaging fehlt -- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=598029
	* String der Länge > 1024 (circa) gehen kaputt -- http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=598031
	* String der Länge 0 geht kaputt -- kann ich so nicht reproduzieren

QT-GUI
* Bild bei Fenstergrößen-Änderung skalieren
* nachträgliches Verkleinern des Fensters ermöglichen
* GUI verhübschen
	* Reaktion auf CTRL-Q, CTRL-W (ESC funktioniert derzeit)
* man kann nicht mittendrin tippen, weil jeder Keystroke den Cursor nach hinten versetzt

CGI-GUI
* Input validieren/escapen
* XHTML-Fehler beheben
