import subprocess
import os
import json

class Helper:
    def _init_(self):
        pass

    def open_app(self):
        return subprocess.Popen(['open', str(os.environ['BROKEN_HASH'])])
    
    def base_url(self):
        return "http://127.0.0.1:" + str(os.environ['PORT'])

    def is_json(self, jsonobject):
        try:
            json.loads(jsonobject)
        except ValueError:
            return False
        return True