import logging
import logging.handlers
from pathlib import Path
import time
import json

import os
 
class MyFilter(logging.Filter):
	"""
	This is a filter which injects contextual information into the log.
	
	Rather than use actual contextual information, we just use random
	data in this demo.
	"""


	def filter(self, record):
		if 'sound' in record.__dict__:
			return True
		else:
			return False
 
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)

Path(dirpath + "/Logs/AllLogs").mkdir(parents=True, exist_ok=True)
Path(dirpath + "/Logs/NoiseLogs").mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s[%(levelname)s]:%(message)s')
mylog = logging.getLogger('my_logger')


AllLog=logging.handlers.TimedRotatingFileHandler("Logs/AllLogs/AllLog", when='H', interval=1, backupCount=5, encoding=None, delay=False, utc=False, atTime=None)
boom = logging.handlers.TimedRotatingFileHandler("Logs/NoiseLogs/NoiseLog", when='H', interval=1, backupCount=5, encoding=None, delay=False, utc=False, atTime=None)
mf = MyFilter()
boom.addFilter(mf)
boom.setLevel(10)
myformat=logging.Formatter(fmt='%(asctime)s[%(levelname)s]:%(message)s')
boom.setFormatter(myformat)
AllLog.setFormatter(myformat)
mylog.addHandler(boom)
mylog.addHandler(AllLog)
mylog.setLevel(10)
print(mylog.getEffectiveLevel())
print(mylog.isEnabledFor(20))
print(mylog.hasHandlers())
namasaya="Rizal"
#logging.basicConfig(filename='Log/example.log',format='%(asctime)s[%(levelname)s]:%(message)s',level=logging.DEBUG)
while True:
	mylog.debug('This message should go to the log file {nama}'.format(nama=namasaya),extra={'sound':"BOOM"})
	mylog.debug('silent')
	mylog.info('WOW',extra={'sound':'Cheers'})
	time.sleep(2)
