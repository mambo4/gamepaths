import project as project
from importlib import reload
reload(project)

import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(module)s.%(funcName)s():%(message)s")

JSON="project_client.json"

def test_IdProjectData():
    instance=project.IdProjectData()
    instance.print_data()
    instance.load(file=JSON)
    instance.print_data()

def test_IdProjectClient():
    client=project.IdProjectClient()
    # client.print_data()

if __name__=="__main__":
    # test_IdProjectData()
    test_IdProjectClient()

