# cutercode

easily create QR codes

## SCREENSHOT

![screenshot](https://raw.github.com/mnagel/cutercode/master/cutercode.png)

## INSTALLATION

* install dependencies with `sudo apt-get install python-qrencode python-qt4`

## USAGE

basic usage:

* just run `./cutercode`
* enter some text/link into the text field, it is automatically converted

command line parameters:

* command line paramters can be used to set the initial QR code
* `./cutercode this is an example` creates a code reading "this is an example"

## TODO

QT-GUI bugs:
* scale image on window resize
* allow to reduce window size
* process CTRL-Q, CTRL-W (ESC works)
* make it possible to type in the middle of the text without moving the cursor

CGI-GUI bugs:
* add input validation
* fix XHTML errors
