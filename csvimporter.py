import csv
import psycopg2
import logging

class CSVImporter:
  """Reads data from WienerLinien CSVs and saves them in the DB
  TODO: remove DB parts from Importer
  """

  tablename = 'stops'
  database = 'angtft'
  logging.basicConfig(level=logging.DEBUG)

  def __init__(self):
    pass

  def read_csv_data(self):
    """Retrieve Data from WienerLinien CSVs and save to DB"""

    try:
      conn = psycopg2.connect("dbname='angtft' user='philipp' host='localhost' password=''")
    except:
      logging.fatal('Unable to connect to the database')
      # TODO throw exception?
      return

    cur = conn.cursor()
    
    # TODO instead of blindly inserting, what about updating?

    # TODO replace tablename, filename and schema with datastructure (and loop)
    with open('data/wienerlinien-ogd-haltestellen.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=';', quotechar='|')
      # first row will are column-names
      next(reader)
      for row in reader:
        data = [row[0], row[2], row[3], row[6], row[7]]
        data[2] = data[2].translate(None, '"')
        logging.info("Will now save: %s into %s", data, "stops")
        cur.execute("""INSERT INTO stops (id, diva, name, latitude, longitude) VALUES (%s, %s, %s, %s, %s)""", data)

      # Make the changes to the database persistent
      conn.commit()

    with open('data/wienerlinien-ogd-linien.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=';', quotechar='|')
      # first row will are column-names
      next(reader)
      for row in reader:
        # TODO save to db
        data = [row[0], row[1], row[4]]
        for i in (1,2):
          data[i] = data[i].translate(None, '"')
        logging.info("Will now save: %s into %s", data, "lines")
        cur.execute("""INSERT INTO lines (id, name, type) VALUES (%s, %s, %s)""", data)

      # Make the changes to the database persistent
      conn.commit()

    with open('data/wienerlinien-ogd-steige.csv') as csvfile:
      reader = csv.reader(csvfile, delimiter=';', quotechar='|')
      # first row will are column-names
      next(reader)
      for row in reader:
        # TODO save to db
        data = [row[0], row[3], row[4], row[5], row[6], row[8], row[9], row[2], row[1]]
        for i in (1,3,4):
          data[i] = data[i].translate(None, '"')
        for i in (3,4):
          data[i] = None if len(data[i]) == 0 else data[i]
        logging.info("Will now save: %s into %s", data, "platforms")
        cur.execute("""INSERT INTO platforms (id, direction, "order", rbl, region, latitude, longitude, stop_id, line_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", data)

      # Make the changes to the database persistent
      conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()