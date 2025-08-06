#!/usr/bin/env python3
import sys
import os
import time
import signal
import json
from pathlib import Path


def create_state_file():
    """Create or update the state file with process info"""
    state_dir = Path.home() / '.forever_monitor'
    state_dir.mkdir(exist_ok=True)
    state_file = state_dir / 'processes.json'

    # Load existing processes
    processes = {}
    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                processes = json.load(f)
        except (json.JSONDecodeError, IOError):
            processes = {}

    # Add current process
    processes[str(os.getpid())] = {
        'argument': sys.argv[1] if len(sys.argv) > 1 else '',
        'command': ' '.join(sys.argv),
        'pid': os.getpid()
    }

    # Write back to file
    with open(state_file, 'w') as f:
        json.dump(processes, f, indent=2)


def cleanup_on_exit(signum, frame):
    """Remove this process from state file when killed"""
    state_dir = Path.home() / '.forever_monitor'
    state_file = state_dir / 'processes.json'

    if state_file.exists():
        try:
            with open(state_file, 'r') as f:
                processes = json.load(f)

            # Remove current process
            processes.pop(str(os.getpid()), None)

            with open(state_file, 'w') as f:
                json.dump(processes, f, indent=2)
        except (json.JSONDecodeError, IOError):
            pass

    sys.exit(0)


def main():
    if len(sys.argv) != 2:
        print("Usage: python forever.py <argument>")
        sys.exit(1)

    argument = sys.argv[1]

    # Set up signal handlers for cleanup
    signal.signal(signal.SIGTERM, cleanup_on_exit)
    signal.signal(signal.SIGINT, cleanup_on_exit)

    # Fork to run in background
    try:
        pid = os.fork()
        if pid > 0:
            # Parent process - print info and exit
            print(f"Started forever process with PID {pid} and argument '{argument}'")
            sys.exit(0)
    except OSError:
        print("Fork failed")
        sys.exit(1)

    # Child process continues here
    # Detach from terminal
    os.setsid()

    # Record this process in state file
    create_state_file()

    print(f"Forever process {os.getpid()} running with argument: {argument}")

    # Run forever loop
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()