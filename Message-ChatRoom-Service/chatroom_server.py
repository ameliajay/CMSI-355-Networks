import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True  # not sure what this means

class UserHandler(socketserver.StreamRequestHandler):
    room = []
    users = {}
    # need to add a chatroom class
    def handle(self):
        client = f'{self.client_address} on {threading.currentThread().getName()}'
        print(f'Connected: {client}')
        self.send('Welcome to The Chat Room\n')
        self.send('Please submit a username - letters and numbers only please\n')
        while True:
            name = self.rfile.readline().decode('utf-8').rstrip('\n')
            # do some other checks here to make sure name isn't just a bunch of spaces
            if not name:
                self.send('You must submit a username to continue\n')
            elif name in self.room:
                self.send('That username is already taken - please submit another\n')
            else:
                self.room.append(name)
                self.users[client] = name
                # I want this to be sent to all the users, not just printed
                print('The Chat Room Members are:')
                for user in self.room:
                    print(user)
                break
        while True:
            message = self.rfile.readline().decode('utf-8')
            if not message:
                break
            self.send(message)
        print(f'Closed: {client}')
        self.room.remove(self.users[client])
        print(f'{name} has left The Chat Room\n')
        print(f'Users still in The Chat Room: {self.room}\n')

    def send(self, message):
        self.wfile.write(f'\n{message}\n'.encode('utf-8'))
        
with ThreadedTCPServer(('', 59898), UserHandler) as server:
    print(f'The Chat Room is live...')
    server.serve_forever()
