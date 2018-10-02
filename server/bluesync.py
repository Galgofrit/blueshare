import struct
from twisted.internet.protocol import Protocol

BLUESYNC_MAGIC = 0xb5b5
BLUESYNC_STRUCT_FORMAT = 'Hc'
BLUESYNC_MESSAGE_LENGTH = 3 # magic 2 + type 1


class BS_REQUEST_TYPES:
    SUCCESSFUL_BT_CONNECTION = 0
    REQUEST_BT_CONNECTION = 1
    BT_CONNECTION_FAILED = 2
    BT_CONNECTION_SUCCESSFUL = 3
    CHECK_CURRENT_OWNER = 4


class BadBluesyncMessage(Exception):
    pass

class BluesyncMessage(object):
    def __init__(self, raw):
        if len(raw) != BLUESYNC_MESSAGE_LENGTH:
            raise BadBluesyncMessage("Bad message: Bad length.")

        parsed = struct.unpack(BLUESYNC_STRUCT_FORMAT, raw)
        self.magic = parsed[0]
        self.request_type = ord(parsed[1])
         

class Bluesync(Protocol):
    def __init__(self, addr, connected_device):
        self.ip = addr
        self.connected_device = connected_device

    def connectionMade(self):
        print 'Received connection'
        self.connected_device.add_user(self)

    def connectonLost(self):
        # if connection was owner of bluetooth, invalidate server
        print 'Lost connection'
        self.connected_device.remove_user(self)
        
    def dataReceived(self, data):
        # switch data type
        # check current connection state
        # register name etc
        try:
            message = BluesyncMessage(data)
        except BadBluesyncMessage:
            print 'Can\'t parse message. Not handling...'
            return

        if message.magic != BLUESYNC_MAGIC:
            print 'Bad message. Not handling...'
            return

        import ipdb; ipdb.set_trace()
        if (message.request_type == BS_REQUEST_TYPES.REQUEST_BT_CONNECTION):
            self.connected_device.request_connection(self)
            print 'lool'
            

