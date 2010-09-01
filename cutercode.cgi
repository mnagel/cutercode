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
makepic = form.getfirst('i','0')
if len(text) < 1 or len(text) > 1000:
    #print "Content-type: image/png"
    #print "Location: http://www.debian-administration.org/images/logo.png"
    #print
    text = "INVALID INPUT (to cutercode)..."



if makepic != '1':
    print "Content-type: text/html"
    print
    print """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>

        <!--
    TODO look better
    -->

        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
        <title>oneshot - upload</title>

        <style type="text/css">
            body { background-color: #4F7E9E; }
            * { font-family: sans-serif; }

            pre { font-family: monospace; }
            ul { margin-left: 1.0em; margin-bottom: 0.1em; }

            h1 { color: #000000; margin-left: 0.1em; margin-top: 0.2em; }
            h2 { color: #000000; }

            hr { color: #E6DACF; background-color: #E6DACF; height: 0.1em; border: 0; }

            a { color: black; text-decoration: none; font-weight: bold; }
            a:hover { color: #E6DACF; }

            .pre { font-family: monospace; }
            .nodeco { text-decoration: none; border: 0 }
            .hanging { margin-left: 0.5em; margin-top: 0px; }
            .invisible { color: #4F7E9E; }
        </style>

        <script type="text/javascript">
            //<![CDATA[

            function show(what) {
                if (document.getElementById(what).style.display=='none')
                    document.getElementById(what).style.display='block';
                else
                    document.getElementById(what).style.display='none';
            }

            //]]>
        </script>
    </head>

    <body>

        <table border="0">
            <tr>
                <td>
                    <a class="nodeco" href="http://validator.w3.org/check?uri=referer">

                        <img class="nodeco" src="http://www.w3.org/Icons/valid-xhtml11-blue" alt="Valid XHTML 1.1" height="31" width="88" />
                    </a>
                </td>
                <td><h1>oneshot - upload - untitled</h1></td>

            </tr>
        </table>
        
            <div>
        <table border="0">
    <tr>
      <td rowspan="2">
          <img class="nodeco" src="./cutercode.cgi?i=1&t=%(qr)s" alt="QR CODE" width="500" height="500"/>
      </td>
    </tr>
    <tr>
      <td>
        <h2>%(qr)s</h2>
        <a class="hanging" href="javascript:show('xx3ky.html')">&rarr; details</a>

      </td>
    </tr>
  </table>

    <ul id="xx3ky.html" style="display:none;">
    <li style="display:none;">
                                  </li>
    <li>uploaded: 2010-09-01 08:16:58                                        </li>
    <li>expires:  2010-10-01 08:16:58                                          </li>

    <li>size      0.009 MB</li>
    <li>sha1:     8e8e3acba5faef98e031d3f1cf68168f7fdcd0e6                                  </li>
    </ul>

    </div>


        <form name='qrinput' enctype="multipart/form-data"
              action='./cutercode.cgi' method='get'>

                
            <input type='text' name='t' value="%(qr)s" size="40" /> &nbsp;
            <input type='submit' value="Generate QR Code"/>
        </form>

    </body>
</html>

    """ % {'qr': text}
    sys.exit()

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
