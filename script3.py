
import watchdog.events
import watchdog.observers
import time
import os 

## this is only a test to commit 
file1= "just a test"
data_file ="file_r.txt"

# get current directory
parent_path = os.getcwd()
print("Current Directory", parent_path)

  

def Imprimer():
    print("---------imprimer")
    with open(data_file, "rb") as file:
        try:
            file.seek(-2, os.SEEK_END)
            while file.read(1) != b'\n':
                file.seek(-2, os.SEEK_CUR)
        except OSError:
            file.seek(0)
        last_line = file.readline().decode()
        last_line = last_line.strip()
        

    print(last_line.split(";"))


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=[data_file],
                                                             ignore_directories=True, case_sensitive=False)
    
    def on_modified(self, event):
        # Event is modified, you can process it now    
        Imprimer()



# main function
if __name__ == "__main__":
    src_path = (parent_path)
    print(parent_path)
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()