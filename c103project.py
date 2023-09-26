import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

source="C:/Users/User/Downloads"


# Event Handler Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
       print(f"Hey, {event.src_path} has been created!")

    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}")     

# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()

try: 
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('stopped!')
    observer.stop()