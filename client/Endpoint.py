'''
Created on Jan 15, 2017

@author: carmine
'''
from twisted.internet import reactor , ssl
from autobahn.twisted.websocket import WebSocketClientFactory, connectWS


class Websocket(object):
    '''
    classdocs
    '''
    __protocol = None


    def __init__(self, protocol):
        '''
        Constructor
        '''
        self.__protocol = protocol
        
    def connect (self  , ip , port):
        
        factory = WebSocketClientFactory("ws://{0}:{1}".format(ip, port))
        factory.protocol = self.__protocol
        connectWS(factory)
    
        reactor.run() #@UndefinedVariable
    
    def disconnect (self):
        pass