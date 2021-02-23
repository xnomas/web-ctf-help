import argparse
import requests

from bs4 import BeautifulSoup, Comment

from webctf import __version__
from .modules.comment_find import Comms
from .modules.script_source_find import Scripts
from .modules.img_source_find import Images
from .modules.headers_view import Headers
from .modules.cookie_send import Cookies
from .modules.flag_find import Flag


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="webctf",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + __version__,
    )
    # required arguments
    parser.add_argument(
        "url",
        help="URL of the target website",
        type=str,
    )
    # optional arguments
    parser.add_argument(
        "--comments",
        help="only display HTML comments",
        action="store_true",
    )
    parser.add_argument(
        "--scripts",
        help="only display script sources",
        action="store_true",
    )
    parser.add_argument(
        "--images",
        help="only display image sources",
        action="store_true",
    )
    parser.add_argument(
        "--headers",
        help="only display interesting response headers (combine with -f to display all)",
        action="store_true",
    )
    parser.add_argument(
        "--cookies",
        help='''add cookies to your request in the following format "name=value;name2=value2"''',
        type=str,
    )
    parser.add_argument(
        "--flags",
        help='''search for a flag hidden on the website in the following format "pattern", and will be searched as "pattern\{*\}"''',
        type=str,
    )
    parser.add_argument(
        "-f",
        "--full",
        help="enable full output for all options",
        action="store_true",
    )

    # get arguments
    args = parser.parse_args()
    settings = {
        "comments": args.comments,
        "headers": args.headers,
        "images": args.images,
        "scripts": args.scripts,
        "cookies": args.cookies,
        "flags": args.flags,
    }
    non_default = {
        "cookies": args.cookies,
        "flags": args.flags,
    }

    # If no argument is entered we assume we want to display all information available.
    for value in settings.values():
        if value and value not in non_default.values():
            break
        else:
            # No argument is True, enable everything
            for key in settings.keys():
                if key in non_default.keys() and settings[key] == None:
                    continue
                settings[key] = True

    # get webpage
    if settings["cookies"]:
        cookies = Cookies(args.cookies)
        cookies.print()
        re = requests.get(args.url, cookies=cookies.get_dict())
    else:
        re = requests.get(args.url)

    # print results
    if settings["comments"]:
        comments = Comms(re.text)
        comments.print()

    if settings["scripts"]:
        scripts = Scripts(re.text)
        scripts.print()

    if settings["images"]:
        images = Images(re.text)
        images.print()

    if settings["flags"]:
        flags = Flag(re.text, args.flags)
        flags.print()

    if settings["headers"]:
        if args.full:
            headers = Headers(re.headers, important_only=False)
        else:
            headers = Headers(re.headers, important_only=True)
        headers.print()

    print()  # end with a new line
