import datetime
import pytz
import configparser
import logging
import os
import requests

def gen_payload(title, downloadUrl, tracker = None, fileSize = None):
    data = {
        'title': title,
        'downloadUrl': downloadUrl,
        'protocol': 'torrent',
        'publishDate': datetime.datetime.now(pytz.timezone('US/Central')).__str__()
    }

    if tracker is not None:
        data['indexer'] = tracker

    if fileSize is not None:
        data['Size'] = parseSize(fileSize)

    return data

def send_pvr(app, title, downloadUrl, tracker = None, fileSize = None):
    filePath = os.path.dirname(__file__)

    data = gen_payload(title, downloadUrl, tracker=tracker, fileSize=fileSize)

    configParser = configparser.RawConfigParser()
    configParser.read('{0}/irssi.cfg'.format(filePath))

    url = configParser.get('irssi-' + app, 'apiUrl')

    apiKey = configParser.get('irssi-' + app, 'apiKey')

    headers = {'Content-Type': 'application/json',
               'X-Api-Key': apiKey}

    try:
        logging.debug('Making request to {0}.'.format(url))
        requests.post(url,
                      json=data,
                      headers=headers)
    except RequestException:
        logging.exception('Error making web request.')
        pass

    logging.info('Report for {0} sent to {2} at {1}.'.format(title, url, app))

def parseSize(size):
    units = {
        "B": 1024**0,
        "KiB": 1024**1,
        "MiB": 1024**2,
        "GiB": 1024**3,
        "TiB": 1024**4
    }
    number, unit = [string.strip() for string in size.split()]
    return int(float(number)*units[unit])
