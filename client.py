# -*- coding: utf-8 -*-
"""
Copyright (c) 2023 Miguel Massot Campos
All rights reserved.
Licensed under the BSD 3-Clause License.
See LICENSE.md file in the project root for full license information.
"""

import socket
from threading import Thread
import json


class Listener:
    def __init__(self):
        # -- UDP
        self.client = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
        )

        # -- Enable port reusage
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # -- Enable broadcasting mode
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # self.client.settimeout(params["timeout"])
        self.client.bind(("", 50000))
        self.th = Thread(target=self.loop, daemon=True)
        self.th.start()

        # -- data recieved
        self.data = None

    def loop(self):
        while True:
            print("waiting for data...")
            try:
                broadcast_data, _ = self.client.recvfrom(4096)
                print("received message:", json.loads(broadcast_data))

            except Exception as e:
                print("Got exception trying to recv %s" % e)

    def __del__(self):
        self.client.close()


if __name__ == "__main__":
    listener = Listener()
    while True:
        pass
