# Web-CTF-Help

## Description

A simple set of scripts (mainly scrapers for now) intended for aid in web CTFs. Find image sources (and alts), javascript sources and comments. 

## Usage

```bash
usage: webctf [-h] [-c] [-sc] [-si] [-he [a]] [-a [a]] url

positional arguments:
  url                   URL to fetch info from

optional arguments:
  -h, --help      show this help message and exit
  -c, --comments  Scrape for HTML comments on given website
  -sc, --scripts  Scrape for script sources on given website
  -si, --img      Scrape for all image sources on given website
  -he [ a ], --headers [ a ]
                  Displays response headers deemed important.
                  To show all use '-he | --headers a'
  -a [ a ], --all [ a ]
                  Use all options on given url. Runs with important headers.
                  Use '-a | --all a' to show all headers
```

### Getting response headers

Get headers deemed important using only `-he`, all using `-he a`

```bash
python3 webctf.py http://example.com -he [ a ] or --headers [ a ]
```

#### Default Output

```bash
python3 webctf.py https://xss-game.appspot.com/level2/frame -he
```
```

===================
INTERESTING HEADERS
===================

Server : Google Frontend
```

#### All Headers Output

```bash
python3 webctf.py https://xss-game.appspot.com/level2/frame -he a
```
```

=============
ALL HEADERS
=============

Content-Type : text/html; charset=utf-8
Cache-Control : no-cache
X-Cloud-Trace-Context : df6d1758c776f4fbc4b3bab158818b64;o=1
Date : Fri, 01 Jan 2021 20:19:57 GMT
Server : Google Frontend
Content-Length : 2689
Alt-Svc : h3-29=":443"; ma=2592000,h3-T051=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"
```


### Getting JS scripts

```bash
python3 webctf.py http://www.example.com -sc or --scripts
```

#### Output

```bash
python3 webctf.py https://xss-game.appspot.com/level2/frame -sc
```
```
=============
SCRIPTS
=============

[+] 1 : /static/game-frame.js
[+] 2 : /static/post-store.js
```

### Getting IMG src and alt

```bash
python3 webctf.py http://www.example.com -si or --img
```

#### Output

```bash
python3 webctf.py https://xss-game.appspot.com/level2/frame -si
```
```

=============
IMAGES
=============

sources:
--------
[+] 1 : /static/logos/level2.png
[+] 2 : /static/level2_icon.png

alts:
-----
[+] 1 : No alt
[+] 2 : No alt
```

### Getting Comments

Why? While usually not applicable in the real world, CTF makers sometimes leave hints in the comments.

```bash
python3 webctf.py http://www.example.com -c or --comments
```

#### Output

```bash
python3 webctf.py https://xss-game.appspot.com/level2/frame -c or --comments
```
```

=============
COMMENTS
=============

[+] 1 :   Internal game scripts/styles, mostly boring stuff
[+] 2 :   This is our database of messages
```

### All at once

Using the option `-a a` or `-all a` will print all response headers. 

```bash
python3 webctf.py http://www.example.com -a [ a ] or -all [ a ]
```

#### Output

```bash
python3 webctf.py https://xss-game.appspot.com/level2/frame -a or -all
```
```

===================
INTERESTING HEADERS
===================

Server : Google Frontend

=============
COMMENTS
=============

[+] 1 :   Internal game scripts/styles, mostly boring stuff
[+] 2 :   This is our database of messages

=============
SCRIPTS
=============

[+] 1 : /static/game-frame.js
[+] 2 : /static/post-store.js

=============
IMAGES
=============

sources:
--------
[+] 1 : /static/logos/level2.png
[+] 2 : /static/level2_icon.png

alts:
-----
[+] 1 : No alt
[+] 2 : No alt
```

## Requirements

```
argparse
bs4
requests
```

## Installation

```bash
git clone https://github.com/xnomas/web-ctf-help
pip install -r requirements.txt
pip install -e .
```

## Future plans

I plan to implement a download function, to download the images, js files and so on. If you have any suggestions feel free to give them to me, 
but please keep in mind that I am still a student :) 
