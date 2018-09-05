<<<<<<< HEAD
import project as project
from importlib import reload
reload(project)

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(module)s.%(funcName)s():%(message)s")

JSON="project_client.json"

def test_IdProjectData():
    instance=project.IdProjectData()
=======
import id_project as id_project
from importlib import reload

reload(id_project)

JSON="id_project_client.json"

def test_IdProjectData():
    instance=id_project.IdProjectData()
>>>>>>> fd773fb7323cda17b727de293665b86209cb4b5c
    instance.print_data()
    instance.load(file=JSON)
    instance.print_data()

<<<<<<< HEAD
def test_IdProjectClient():
    client=project.IdProjectClient()
    # client.print_data()

if __name__=="__main__":
    # test_IdProjectData()
    test_IdProjectClient()
=======
if __name__=="__main__":
    test_IdProjectData()
>>>>>>> fd773fb7323cda17b727de293665b86209cb4b5c

