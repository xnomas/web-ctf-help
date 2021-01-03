import argparse
import requests
import sys

sys.path.append('src/')

from bs4 import BeautifulSoup, Comment

from __version__ import version  

from modules.comment_find import Comms
from modules.script_source_find import Scripts
from modules.img_source_find import Images
from modules.headers_view import Headers


def main():
    parser = argparse.ArgumentParser(
        prog="webctf",
        allow_abbrev=False,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + version,
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
    }

    # If no argument is entered we assume we want to display all information available.
    for value in settings.values():
        if value:
            break
    else:
        # No argument is True, enable everything
        for key in settings.keys():
            settings[key] = True

    # get webpage
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
    if settings["headers"]:
        if args.full:
            headers = Headers(re.headers, important_only=False)
        else:
            headers = Headers(re.headers, important_only=True)
        headers.print()


if __name__ == "__main__":
    main()
