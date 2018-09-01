import json
import logging


logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class IdProjectData(object):
    """base class for reading and writing json data"""

    def __init__(self):
        self.file =None
        self.data =None

    def load(self,file=None):
        if file:
            self.file=file
        if self.file:
            try:
                with open(self.file, 'r') as f:
                    self.data =json.load(f)
                logger.info("loaded {}".format(self.file))
            except IOError as e:
                logger.error("failed to load {}:\n{}".format(self.file,e))
        else:
            logger.warning("no file specified.")

    def print_data(self):
        if self.data:
            for k,v in self.data.items():
                print("{} : {}".format(k,v))
        else:
            print ("no data")

class IdProjectClient(IdProjectData):
    pass