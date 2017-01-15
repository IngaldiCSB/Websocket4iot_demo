'''
Created on Jan 11, 2017

@author: carmine
'''

from twisted.internet import reactor , ssl

from autobahn.twisted.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS

IP = "127.0.0.1"
PORT = "3000"

class DemoProtocol(WebSocketClientProtocol):
    
    __msgCount = 0
            

    def onOpen(self):
        self.sendMessage("Hello, world!".encode('utf8'))

    def onMessage(self, payload, isBinary):
        if not isBinary:
            print("[{}]received: {}".format(self.__msgCount , payload.decode('utf8')))
            
            
            self.__msgCount += 1


if __name__ == '__main__':
    pass

        # create a WS server factory with our protocol
    ##
    factory = WebSocketClientFactory("ws://{0}:{1}".format(IP, PORT))
    factory.protocol = DemoProtocol
    connectWS(factory)
    
    reactor.run() #@UndefinedVariable