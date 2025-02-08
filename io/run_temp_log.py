import time
import subprocess

SCRIPT_NAME = "temp_log.py"

while True:
    try:
        subprocess.run(["python", SCRIPT_NAME])
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(1)
