#!/usr/bin/python3

from zocp import ZOCP
import time
import math

class Annoyatron(ZOCP):
    # Constructor
    def __init__(self, nodename=""):
        super(Annoyatron, self).__init__()
        self.set_name(nodename)

        self.interval = 0.1
        self.loop_time = 0

        self.register_string('','', '')
        self.start()

        while True:
            try:
                self.run_once(0)
                if time.time() > self.loop_time:
                    self.loop_time = time.time() + self.interval
                    self.on_timer()
            except (KeyboardInterrupt, SystemExit):
                break

        self.stop()
  
    def on_timer(self):
        position = [
            math.sin(time.time()) * 100,
            math.cos(time.time()) * 100
        ]
        # This is a BAD idea!
        self._on_modified({'_zne_position': position})

        
if __name__ == '__main__':
    z = Annoyatron("ANNOYATRON!")
    del z 
