import subprocess
import os

class Helper:
    def _init_(self):
        pass

    def open_app(self):
        return subprocess.Popen(['open', str(os.environ['BROKEN_HASH'])])
