import datetime
from json import JSONEncoder

class RMSDelayEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, datetime.datetime):
      return obj.isoformat()
    else:
      return super(RMSDelayEncoder, self).default(obj)

class RMSDelay:

  # avgDelay
  # latitude
  # longitude

  def __init__(self, latitude, longitude, avgDelay, timestamp):
    self.latitude = latitude
    self.longitude = longitude
    self.avgDelay = avgDelay
    # self.timestamp = timestamp

  def __str__(self):
     return "delay {lat: " + str(self.latitude) +\
            ", long: " + str(self.longitude) +\
            ", delay in mins: " + str(self.avgDelay) +\
            ", timestamp: " + str(self.timestamp) + "}"

