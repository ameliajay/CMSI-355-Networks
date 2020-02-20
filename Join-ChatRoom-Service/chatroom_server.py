import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True  # not sure what this means

class UserHandler(socketserver.StreamRequestHandler):
    room = []
    # this can become a chatroom class
    def handle(self):
        client = f'{self.client_address} on {threading.currentThread().getName()}'
        print(f'Connected: {client}')
        self.send('Welcome to The Chat Room\n')
        self.send('Please submit your name\n')
        while True:
            name = self.rfile.readline().decode('utf-8').rstrip('\n')
            if not name:
                self.send('You must submit a name to continue\n')
                return
            else:
                self.room.append(name)
                self.send('Someone new has entered The Chat Room')
                self.send(self.room)
                break
                
def send(self, message):
    self.wfile.write(f'{message}\n'.encode('utf-8'))
    
with ThreadedTCPServer(('', 59898), UserHandler) as server:
    print(f'The Chat Room is live...')
    server.serve_forever()
