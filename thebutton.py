# Based on https://github.com/hjfreyer/thebutton/
# This is free and unencumbered software released into the public domain.
# 
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
# 
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import re
import urllib2
import json
from websocket import create_connection

class TheButton:
    ws_re = re.compile('(wss://wss.redditmedia.com/thebutton\?h=[0-9a-f]*&e=[0-9a-f]*)')

    def __init__(self):
        self.ws_url = self.get_websocket_url()

    def get_websocket_url(self):
        req = urllib2.urlopen("https://www.reddit.com/r/thebutton")
        contents = req.read()

        matches = TheButton.ws_re.findall(contents)
        if any(matches):
            return matches[0]
        else:
            raise Exception("Failed to find websocket url")

    def get_current_time(self):
        ws = create_connection(self.ws_url)
        result = ws.recv()
        json_result = json.loads(result)
        ws.close()
        return json_result["payload"]["seconds_left"]
