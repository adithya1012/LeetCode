import sys
from pathlib import Path
import configparser
import signal
import os
import json
import time

folder = "./test_folder"
file = "process.json"

class forever:
    def __init__(self):
        global folder, file
        folder = Path(folder)
        folder.mkdir(exist_ok=True)
        self.file = folder/file
        # self.file.mkdir(exist_ok=True)
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)

    def cleanup(self, sig, frame):
        # process = self.read_file()
        # if str(os.getpid()) in process:
        #     del process[str(os.getpid())]
        # with open(self.file, "w") as f:
        #     json.dump(process, f, indent=2)
        pass

    def write_file(self, process, arg):
        process[str(os.getpid())] = {
            "pid": str(os.getpid()),
            "arg": arg,
            "cmd": [sys.executable, sys.argv[0], arg]
        }
        with open(self.file, "w") as f:
            json.dump(process, f, indent=2)

    def read_file(self):
        if not self.file.exists():
            return {}
        process = {}
        with open(self.file, "r") as f:
            process = json.load(f)
        return process

    def main(self):
        arg1 = sys.argv[1]
        process = self.read_file()
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
        os.setsid()
        self.write_file(process, arg1)
        while True:
            time.sleep(1)

if __name__ == "__main__":
    obj = forever()
    obj.main()