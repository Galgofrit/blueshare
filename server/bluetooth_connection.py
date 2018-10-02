from twisted.internet import reactor, defer

class IDENTITIES:
    UNKNOWN = '_unknown'

class BluetoothConnection(object):
    def __init__(self):
        self.users = []
        self.lastOwner = None
        self.isFree = True
        self.defer = None

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.pop(user)

    def request_connection(self, identity):
        if self.isFree:
            self.lastOwner = identity
            self.isFree = False
            return True
        else:
            self.defer = defer.Deferred()
            #  self.defer.addCallback()
            return False


    def release_connection(self, identity):
        if (self.lastOwner == identity):
            self.isFree = True
        elif (self.lastOwner == IDENTITIES.UNKNOWN):
            self.isFree = True # allow anyone to release on unknown


    def get_release_from_client(self, identity):
        # send identity packet asking it to release
        # wait for it to respond with packet "i released"
        pass


    def request_release(self, identity):
        if (self.lastOwner == IDENTITIES.UNKNOWN):
            self.isFree = True # allow anyone to release on unknown
        # send identity request to disconnect via self.defer.addCallback(get_release_from_client)
        self.isFree = True
        self.release_connection(identity)

