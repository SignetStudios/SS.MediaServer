import argparse
import configparser
import logging
import os
from irssi_general import gen_payload, send_pvr

filePath = os.path.dirname(__file__)
logging.basicConfig(filename='{0}/irssi.log'.format(filePath),level=logging.DEBUG)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--downloadUrl", required=True)
    parser.add_argument("--tracker")
    parser.add_argument("--torrentSize")

    args = parser.parse_args()

    send_pvr('sonarr', args.title, args.downloadUrl, tracker=args.tracker, fileSize=args.torrentSize)
