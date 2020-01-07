import logging
import logging.handlers
from pathlib import Path

import os
 
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)

Path(dirpath + "/Log").mkdir(parents=True, exist_ok=True)

logging.basicConfig(level=logging.DEBUG, format='%(message)s')
mylog = logging.getLogger('my_logger')

boom = logging.handlers.RotatingFileHandler("wow", mode='a', maxBytes=0, backupCount=10, encoding=None, delay=False)
boom.setLevel(20)
mylog.addHandler(boom)
mylog.setLevel(20)
print(mylog.getEffectiveLevel())
print(mylog.isEnabledFor(20))
print(mylog.hasHandlers())

#logging.basicConfig(filename='Log/example.log',format='%(asctime)s[%(levelname)s]:%(message)s',level=logging.DEBUG)
mylog.debug('This message should go to the log file')
boom.doRollover()
mylog.info('So should this')
mylog.warning('And this, too')