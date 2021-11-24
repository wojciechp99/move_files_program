import datetime
import os
import shutil


def create_folder(name, date):
    try:
        folder_name = f"{name} {date}"
        path = os.path.join(destination, folder_name)
        os.mkdir(path)
    except FileExistsError:
        pass


def move(file, date):
    for folder in os.listdir(destination):
        if date in folder:
            path = os.path.join(destination, folder)
            shutil.copy(file, path)
            break
        else:
            continue


def files_in_folder(name_for_folder, source):
    for file in os.listdir(source):
        path = os.path.join(source, file)
        created = os.path.getmtime(path)
        date = datetime.datetime.fromtimestamp(created).strftime('%d.%m.%Y')
        create_folder(name_for_folder, date)
        move(path, date)


# rotates date in name to make it easy to sort
def change_name_of_folders(name):
    for folder in os.listdir(destination):
        path = os.path.join(destination, folder)
        day = folder[-10:-8]
        month = folder[-8:-4]
        year = folder[-4:]
        new_path = os.path.join(destination, f"{name} {year}{month}{day}")
        os.rename(path, new_path)


if __name__ == "__main__":
    from_source = "C:/Users/wojtek/Videos/"
    destination = "D:/destination_folder_for_video/"
    files_in_folder('Video_from', from_source)
    change_name_of_folders('Folder')

