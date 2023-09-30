import argparse
import logging
from irssi_general import send_pvr

logging.basicConfig(filename='irssi.log',level=logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("--title", required=True)
parser.add_argument("--downloadUrl", required=True)
parser.add_argument("--tracker")
parser.add_argument("--torrentSize")

args = parser.parse_args()

logging.debug(args.torrentSize)

send_pvr('sonarr', args.title, args.downloadUrl, tracker=args.tracker, fileSize=args.torrentSize)
send_pvr('radarr', args.title, args.downloadUrl, tracker=args.tracker, fileSize=args.torrentSize)