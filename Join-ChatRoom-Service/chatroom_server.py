import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True  # not sure what this means

class UserHandler(socketserver.StreamRequestHandler):
    room = []
    users = {}
    name = None
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
                self.name = name
                self.initialize()
                self.display_members()
                self.send('\nType your message below and press Enter to send\n')
                break
        while True:
            message = self.rfile.readline().decode('utf-8')
            if not message:
                break
            self.send(message)
        print(f'Closed: {client}')
        self.room.remove(self.users[client])
        self.leave()
        self.display_members()
        print(f'{name} has left The Chat Room\n')
        print(f'Users still in The Chat Room:')
        for user in self.room:
            print(user)

    def send(self, message):
        self.wfile.write(f'\n{message}\n'.encode('utf-8'))

    def initialize(self):
        ChatRoom.join(self)
        
    def display_members(self):
        ChatRoom.display_members(self)

    def leave(self):
        ChatRoom.leave(self)
        
class ChatRoom:
    members = []

    def __init__(self):
        self.lock = threading.Lock()

    @classmethod
    def join(cls, user):
        cls.members.append(user)
        for member in cls.members:
            member.send(user.name + ' has entered The Chat Room.')
            
    @classmethod
    def leave(cls, user):
        cls.members.remove(user)
        
    @classmethod
    def display_members(cls, user):
        for member in cls.members:
            member.send('The Chat Room Members:')
            for m in cls.members:
                member.send(m.name)
            member.send('_______________________________________________')
    
with ThreadedTCPServer(('', 59898), UserHandler) as server:
    print(f'The Chat Room is live...')
    server.serve_forever()
