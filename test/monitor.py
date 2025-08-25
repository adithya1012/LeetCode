#!/usr/bin/env python3
import sys
import os
import time
import json
import subprocess
import signal
from pathlib import Path


class ProcessMonitor:
    def __init__(self, program_name):
        self.program_name = program_name
        self.state_dir = Path('./forever_monitor')
        self.state_file = self.state_dir / 'processes.json'
        self.running = True

        # Ensure state directory exists
        self.state_dir.mkdir(exist_ok=True)

        # Set up signal handlers - only for monitor itself
        signal.signal(signal.SIGTERM, self.stop_monitoring)
        signal.signal(signal.SIGINT, self.stop_monitoring)

    def stop_monitoring(self, signum, frame):
        """Stop the monitoring loop"""
        print(f"\nMonitor {os.getpid()} stopping...")
        self.running = False
        sys.exit(0)

    def load_processes(self):
        """Load process information from state file"""
        if not self.state_file.exists():
            return {}

        try:
            with open(self.state_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}

    def save_processes(self, processes):
        """Save process information to state file"""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(processes, f, indent=2)
        except IOError as e:
            print(f"Error saving processes: {e}")

    def is_process_running(self, pid):
        """Check if a process is still running"""
        try:
            # Send signal 0 to check if process exists
            os.kill(int(pid), 0)
            return True
        except (OSError, ProcessLookupError):
            return False

    def restart_process(self, process_info):
        """Restart a dead process"""
        argument = process_info['argument']
        print(f"Attempting to restart: {self.program_name} {argument}")

        try:
            # Start the process
            cmd = [sys.executable, f"{self.program_name}.py", argument]
            result = subprocess.Popen(cmd)
            print(f"Successfully started {self.program_name} {argument} with PID {result.pid}")
            return True
        except Exception as e:
            print(f"Failed to restart {self.program_name} {argument}: {e}")
            return False

    def monitor(self):
        """Main monitoring loop"""
        print(f"Monitor {os.getpid()} started, watching {self.program_name} processes...")

        while self.running:
            processes = self.load_processes()
            dead_processes = []
            alive_processes = {}

            # Check each tracked process
            for pid, info in processes.items():
                if self.is_process_running(pid):
                    # Process is still alive, keep it
                    alive_processes[pid] = info
                else:
                    # Process is dead, mark for restart
                    print(f"Process {pid} ({self.program_name} {info['argument']}) is dead")
                    dead_processes.append(info)

            # Restart dead processes
            for info in dead_processes:
                print("Removing : ", str(info["pid"]))
                processes.pop(str(info["pid"]))
                print(f"Restarting: {self.program_name} {info['argument']}")
                self.restart_process(info)
                self.save_processes(processes)
                # Give time for new process to start and register itself
                time.sleep(0.5)

            # If there were changes, reload the processes to get new PIDs
            if dead_processes:
                # Small delay to let new processes register
                time.sleep(1.5)

            # Wait before next check
            time.sleep(2)


def main():
    if len(sys.argv) != 2:
        print("Usage: python monitor.py <program_name>")
        print("Example: python monitor.py forever")
        sys.exit(1)

    program_name = sys.argv[1]

    # Fork to run in background
    try:
        pid = os.fork()
        if pid > 0:
            # Parent process - print info and exit
            print(f"Started monitor process with PID {pid} for program '{program_name}'")
            sys.exit(0)
    except OSError:
        print("Fork failed")
        sys.exit(1)

    # Child process continues here
    # Detach from terminal
    os.setsid()

    # Start monitoring
    monitor = ProcessMonitor(program_name)
    monitor.monitor()


if __name__ == "__main__":
    main()