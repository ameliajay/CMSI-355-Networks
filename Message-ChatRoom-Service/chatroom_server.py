class UserHandler(socketserver.StreamRequestHandler):
    room = []
    users = {}
    name = None
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
                self.name = name
                self.initialize()
                break
        while True:
            message = self.rfile.readline().decode('utf-8')
            if not message:
                break
            self.send_all(message)
        print(f'Closed: {client}')
        self.room.remove(self.users[client])
        print(f'{name} has left The Chat Room\n')
        print(f'Users still in The Chat Room:')
        for user in self.room:
            print(user)

    def send(self, message):
        self.wfile.write(f'\n{message}\n'.encode('utf-8'))

    def send_all(self, message):
        ChatRoom.send(self, message)

    def initialize(self):
        ChatRoom.join(self)

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
    def send(cls, sender, message):
        name = sender.name
        for member in cls.members:
            if member.name is not name:
                member.send(name + '> ' + message)

with ThreadedTCPServer(('', 59898), UserHandler) as server:
    print(f'The Chat Room is live...')
    server.serve_forever()
