<<<<<<< HEAD
import os
import json
import logging
import getpass

USER=getpass.getuser()
HOME=os.environ["HOME"]
=======
import json
import logging

>>>>>>> fd773fb7323cda17b727de293665b86209cb4b5c

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

<<<<<<< HEAD

=======
>>>>>>> fd773fb7323cda17b727de293665b86209cb4b5c
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
<<<<<<< HEAD
            except FileNotFoundError as e:
                logger.info("failed to locate {}:\n{}".format(self.file,e))
                pass
            except IOError as e:
                logger.info("failed to load {}:\n{}".format(self.file,e))  
                pass   
=======
            except IOError as e:
                logger.error("failed to load {}:\n{}".format(self.file,e))
>>>>>>> fd773fb7323cda17b727de293665b86209cb4b5c
        else:
            logger.warning("no file specified.")

    def print_data(self):
        if self.data:
            for k,v in self.data.items():
                print("{} : {}".format(k,v))
        else:
            print ("no data")

class IdProjectClient(IdProjectData):
<<<<<<< HEAD
    
    def __init__(self,file=None):
        self.default_file=os.path.join(HOME,"id_project_data.json")
        self.file =None
        self.data =None
        self.project_name = None
        self.user = None
        self.server = None
        self.source_client = None
        self.source_root = None
        self.game_client = None
        self.game_root = None

        self.load_default()

    def load_default(self):
        try:
            self.load(self.default_file)
        except FileNotFoundError:
            logger.info( "default file '{}' could not be found.".format(self.default_file))
            pass
        
=======
    pass
>>>>>>> fd773fb7323cda17b727de293665b86209cb4b5c
