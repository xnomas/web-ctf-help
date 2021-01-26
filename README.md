# Web-CTF-Help

## Description

A simple set of scripts (mainly scrapers for now) intended for aid in web CTFs. Find image sources (and alts), javascript sources and comments. 

## Usage

```bash
usage: webctf [-h] [-v] [--comments] [--scripts] [--images] [--headers] [--cookies COOKIES] [--flags FLAGS] [-f] url

positional arguments:
  url            URL of the target website

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
  --comments     only display HTML comments (default: False)
  --scripts      only display script sources (default: False)
  --images       only display image sources (default: False)
  --headers      only display interesting response headers (combine with -f to display all) (default: False)
  --cookies COOKIES  add cookies to your request in the following format "name=value;name2=value2" (default: None)
  --flags FLAGS      search for a flag hidden on the website in the following format "pattern", and will be searched as "pattern\{*\}" (default: None)
  -f, --full     enable full output for all options (default: False)
```

```bash
webctf https://example.com
```

Only display HTML comments and script sources:

```bash
webctf --comments --scripts https://example.com
```
```
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
```

Only display interesting headers:

```bash
webctf --headers https://example.com
```
```
===================
INTERESTING HEADERS
===================

Server : Google Frontend
```

Display all headers:

```bash
webctf --headers -f https://example.com
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
Send a request with a cookie and only get comments

```bash
webctf --cookies "name1=value1;name2=value2" --comments https://example.com 
```
```
==============
Using cookies:
==============

[+] name1 = value1
[+] name2 = value2

=============
COMMENTS
=============

[+] 1 :   Internal game scripts/styles, mostly boring stuff
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

## Thank you!

Thank you to [sinus-x](https://github.com/sinus-x) for helping!
