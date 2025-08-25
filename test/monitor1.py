import json
import os
import time
from pathlib import Path
import signal
import subprocess

folder = "./test_folder"
file = "process.json"

class Monitor:
    def __init__(self):
        global folder, file
        self.running = True
        folder = Path(folder)
        folder.mkdir(exist_ok=True)
        self.file = folder/file
        # file.mkdir(exist_ok=True)
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)

    def cleanup(self, sig, frame):
        self.running = False
        print("Terminating Monitor ...")
        pass

    def read_json(self):
        if not self.file.exists():
            return {}
        with open(self.file, "r") as f:
            return json.load(f)

    def write_json(self, process):
        with open(self.file, "w") as f:
            return json.dump(process, f, indent=2)

    def check_alive(self, pid):
        try:
            os.kill(int(pid), 0)
            return True
        except OSError:
            return False

    def restart_process(self, info, process):
        try:
            pid = info["pid"]
            print(f"Process {str(pid)} is restarted !!!")
            if str(info["pid"]) in process:
                del process[str(info["pid"])]
            self.write_json(process)
            subprocess.run(info["cmd"])
            return True
        except:
            return False


    def main(self):
        while self.running:
            process = self.read_json()
            dead_process = []
            for pid, info in process.items():
                if not self.check_alive(pid):
                    dead_process.append(info)

            for info in dead_process:
                self.restart_process(info, process)

            time.sleep(1)

if __name__ == "__main__":
    obj = Monitor()
    obj.main()









