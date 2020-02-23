import socketserver
import threading

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

class UserHandler(socketserver.StreamRequestHandler):
    room = []
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
                # add the name to the list of names in the room
                self.room.append(name)
                self.name = name
                # then join the chat room
                self.initialize()
                self.display_members()
                self.send('\nType your message below and press Enter to send\n')
                break

        # keep sending messages until the client leaves
        while True:
            message = self.rfile.readline().decode('utf-8')
            if not message:
                break
            self.send_all(message)

        print(f'Closed: {client}')
        # remove the name from the list of names and leave the chat room
        self.room.remove(self.name)
        self.leave()
        self.send_all('Bye!! I am leaving The Chat Room\n')
        self.display_members()

    def send(self, message):
        self.wfile.write(f'\n{message}\n'.encode('utf-8'))

    def send_all(self, message):
        ChatRoom.send(self, message)

    def initialize(self):
        ChatRoom.join(self)

    def display_members(self):
        ChatRoom.display_members(self)

    def leave(self):
        ChatRoom.leave(self)

class ChatRoom:
    members = []

    def __init__(self):
        # would locking be used if I wanted lots of chatrooms open at the same time?
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
    def send(cls, sender, message):
        name = sender.name
        for member in cls.members:
            if member.name is not name:
                member.send(name + ' > ' + message)
            else:
                member.send('me > ' + message)

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
