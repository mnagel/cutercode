#!/usr/bin/python
# vim:set encoding=utf-8 ft=python ts=8 sw=4 sts=4 et cindent:

# Copyright © 2010  Michael Nagel <nailor@devzero.de>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.

from __future__ import with_statement

import sys
import qrencode
import StringIO

import cgi
form = cgi.FieldStorage()
text = form.getfirst('t','DEMO-QR-CODE')
if len(text) < 1 or len(text) > 1000:
    #print "Content-type: image/png"
    #print "Location: http://www.debian-administration.org/images/logo.png"
    #print
    text = "INVALID INPUT (to cutercode)..."

print "Content-type: image/png"
print

def pil_to_qpixmap(pil_image):
    buf = StringIO.StringIO()
    pil_image.save(buf, format='PNG')
    contents = buf.getvalue()
    print contents
    return ""

size=300
_, _, pil_img = qrencode.encode_scaled(text, level=3, size=size)
qpix = pil_to_qpixmap(pil_img)
