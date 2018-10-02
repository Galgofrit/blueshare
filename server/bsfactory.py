from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

import config
import bluesync
import bluetooth_connection

class BSFactory(Factory):
    def __init__(self):
        print 'Reactor started.'
        self.connected_device = bluetooth_connection.BluetoothConnection()
        self.clients = []

    def buildProtocol(self, addr):
        return bluesync.Bluesync(addr, self.connected_device)


endpoint = TCP4ServerEndpoint(reactor, config.PORT)
endpoint.listen(BSFactory())
print 'Starting reactor on port {port}.'.format(port=config.PORT)
try:
    reactor.run()
except KeyboardInterrupt:
    reactor.stop()
    print 'Stopping reactor.'
