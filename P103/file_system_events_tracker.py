import sys
import time
import shutil
import os
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = '/Users/satya/Downloads'

class FileEventHandler (FileSystemEventHandler) :
    def on_created(self, event) :
        print('A file has been created at' + event.src_path)
        time.sleep(0.5)
    
    def on_modified(self, event) :
        print('A file has been modified at' + event.src_path)
        time.sleep(0.5)

    def on_moved(self, event) : 
        print('A file has been moved from' + event.src_path)
        time.sleep(0.5) 

    def on_deleted(self, event) :
        print('Oops! A file has een deleted at' + event.src_path)
        time.sleep(0.5)

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive = True)

observer.start()

try:
    while True :
        print('Running...')
        time.sleep(1.5)
except KeyboardInterrupt:
    observer.stop()
    print('Stopped!')