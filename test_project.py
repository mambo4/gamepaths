import id_project as id_project
from importlib import reload

reload(id_project)

JSON="id_project_client.json"

def test_IdProjectData():
    instance=id_project.IdProjectData()
    instance.print_data()
    instance.load(file=JSON)
    instance.print_data()

if __name__=="__main__":
    test_IdProjectData()

