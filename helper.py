import subprocess
import os
import json
import requests
import base64

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

    def create_hash_id(self):
        data = {'password':'angrymonkey'}
        headers = {'Accept':'application/json'}
        response = requests.post(self.base_url() + "/hash", json=data, headers=headers)
        return response.text

    def isBase64(self, s):
        try:
            return base64.b64encode(base64.b64decode(s)) == s
        except Exception:
            return False