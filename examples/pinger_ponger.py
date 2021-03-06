import add_import_path # only for examples
__author__ = 'ceremcem'

from aktos_dcs import *


class Ponger(Actor):
    def handle_PongMessage(self, msg):
        msg = get_msg_body(msg)
        print "Pong got pong message:", msg['text']
        sleep(2)
        self.send({'PingMessage': {'text': "Hello pinger!"}})


class Pinger(Actor):
    def handle_PingMessage(self, msg):
        msg = get_msg_body(msg)
        print "Ping got ping message: ", msg['text']
        sleep(2)
        self.send({'PongMessage': {'text': "Hello ponger!"}})


if __name__ == "__main__":
    pinger = Pinger()
    ponger = Ponger()

    pinger.send({'PongMessage': {'text': "Hello ponger!"}})

    wait_all()