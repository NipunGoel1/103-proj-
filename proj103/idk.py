import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/iTechBuddy/Downloads"
to_dir = "C:/Users/iTechBuddy/Desktop/Down_Files"


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey,{event.src_path}has been created!")
    def on_deleted(self,event):
        print(f"Oops,someone deleted{event.src_path}!")
    def on_modified(self, event):
        print(f"Ooooh,{event.src_path}has been modified!")
    def on_moved(self,event):
        print(f"Oi,someone moved your file{event.src_path}!")
       # name,ext = os.path.splitext(event.src_path)
        # for key,value in dir_tree.items():
        #     if (ext in value):
        #         file_name = os.path.basename(event.src_path)
        #         path1 = from_dir + '/'+ file_name
        #         path2 = to_dir + '/'+ key
        #         path3 = to_dir +'/'+ key +'/'+ file_name
        #         time.sleep(3)
        #         if(os.path.exists(to_dir+'/'+key)):
        #             shutil.move(path1,path3)
        #         else:
        #             os.makdir(path2)
        #             shutil.move(path1,path3)    
   #print(event)
       # print(event.src_path)


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
 while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("STOP!Put your hands in the air,no funny business")
    observer.stop()
    