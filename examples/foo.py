import add_import_path # only for examples
__author__ = 'ceremcem'


from aktos_dcs import *


class Foo(Actor):
    def handle_FooMessage(self, msg):
        msg = get_msg_body(msg)
        print "Foo got FooMessage: ", msg['text']
        sleep(1)
        self.send({'BarMessage': {'text': "Hello bar, this is foo from cca!"}})

if __name__ == "__main__":
    ProxyActor()
    foo = Foo()
    foo.send({'BarMessage': {'text': "startup message from foo from cca..."}})

    wait_all()