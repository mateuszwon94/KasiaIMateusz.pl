from .settings import DRIVE

def get_item_from_onedrive(path:str, folder=DRIVE):
    path = [f for f in path.split("/") if f and f != "."]

    current_folder = folder
    for f in path:
        if f == "..":
            current_folder = current_folder.get_parent()
        else:
            for item in current_folder:
                if item.name == f:
                    current_folder = item
                    break
