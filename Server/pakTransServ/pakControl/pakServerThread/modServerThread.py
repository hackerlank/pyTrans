# -*- coding: utf-8 -*-
'''
В этом потоке сервер ожидает подключений от киентов, после чего
перебрасывает их на свои потоки.
'''

from PySide import QtCore
from .pakTcpServer.modTcpServer import clsTcpServer

class clsServerThread(QtCore.QThread):
    def __init__(self, root):
        print('      clsServerThread.__init__()')
        self.__root = root
        self.__TcpServer = clsTcpServer(root)
        self.running = False
        super(clsServerThread, self).__init__()
        
    def run(self):
        print('      clsServerThread.run()')
        self.__TcpServer.adress = 'localhost'
        self.sleep(1)
        self.__TcpServer.port = int(self.__root.Gui.winMain.entPort.text())
        print('      run 1()')    
        self.sleep(1)
        self.__TcpServer.run()
        print('      run 2()')    
        self.sleep(1)
        while self.running:
            if self.__TcpServer.listening:
                print('      clsServerThread listening')   
            else:
                print('      clsServerThread not listening')  
            self.sleep(3)
        else:
            print('      clsServerThread stopped')
            self.__TcpServer.stop()
            #self.__TcpServer.stop()
