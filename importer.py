import requests
import json
import logging
import psycopg2

class Importer:
  """Imports Data from WienerLinien API

  For this version, only one single monitor is observed.
  """

  logging.basicConfig(level=logging.DEBUG)

  endpoint = 'http://www.wienerlinien.at/ogd_realtime/monitor'
  sender = ''
  rblList = []
  accept = 'application/json'

  tablename = 'stops'
  database = 'angtft'

  def __init__(self):
    json_data=open('config.json')
    data = json.load(json_data)

    logging.info('Initializing Importer with WL-Sender config')
    self.sender = data['WL-sender']
    pass

  def loadRBLList(self):
    try:
      conn = psycopg2.connect("dbname='angtft' user='philipp' host='localhost' password=''")
    except:
      logging.fatal('Unable to connect to the database')
      # TODO throw exception?
      return

    cur = conn.cursor()

    cur.execute("""select distinct rbl from platforms where rbl IS NOT NULL;""")

    self.rblList = [str(i[0]) for i in cur.fetchall()]

    # logging.info("Fetched List %s from DB", self.rblList)

  def request(self):
    """Issue the request to WienerLinien"""
    
    # Request need splitting, because rblList parameter is too long
    result = list()

    # TODO be more smart about splitting (find magic spot)
    chunksize = 200
    request = 1
    for i in xrange(0, len(self.rblList), chunksize):
      logging.debug("Request-chunk nr %s", request)
      rblShortList =  ','.join(self.rblList[i:i+chunksize])

      payload = {'sender': self.sender, 'rbl': rblShortList}
      logging.debug('Request payload: %s', payload)
      headers = {'content-type': self.accept, 'accept': self.accept}
      logging.debug('Request headers: %s', headers)

      r = requests.get(self.endpoint, params=payload, headers=headers)
      if r.status_code == requests.codes.ok:
        logging.info('WienerLinien real-time data request successful')
        # TODO returning here makes no sense, as we have multiple requests
        result.extend(r.json()['data']['monitors'])
      else:
        logging.error('Error issuing WienerLinien real-time data request!')
        # TODO: map status codes with error description from data.gv.at
        logging.error('Status code: %d', r.status_code)
        raise Exception('Server returned %s', r.status_code)

      request += 1
      # break;
    
    return result
