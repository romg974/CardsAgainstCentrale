import threading
import time
import requests

class GameManager(threading.Thread):
    api = 'http://localhost/CAC/'

    username = ''
    userkey = ''
    partie = ''
    cards = []
    running = True
    action = None
    callback = None

    ACTION_PING = 0
    ACTION_LOGIN = 1
    ACTION_LOBBY = 2
    ACTION_JOIN = 3
    ACTION_CREATE = 4
    ACTION_GAME = 5
    ACTION_PLAY = 6
    ACTION_VOTE = 7

    def run(self):
        print("GM running")
        while self.running:
            self.perform_calls()
            time.sleep(0.1)

    def request(self, uri='', payload=None):
        try:
            if payload != None:
                r = requests.post(self.api + '?' + uri, data=payload, headers={'X-UK': self.userkey})
            else:
                r = requests.get(self.api+'?'+uri, headers={'X-UK': self.userkey})
            if r.status_code != 200:
                return False
            else:
                print(r.text)
                return r.json()
        except:
            return False

    def perform_calls(self):
        if self.action == self.ACTION_PING:
            self.callback(self.request())
        elif self.action == self.ACTION_LOGIN:
            result = self.request('login', {'username': self.username})
            if result != False:
                if result['ok']:
                    self.userkey = result['userkey']
                    self.callback(True)
                else:
                    self.callback(False, result['message'])
            else:
                self.callback(False, 'Echec de la communication avec le serveur.')
        elif self.action == self.ACTION_LOBBY:
            result = self.request('lobby')
            if result != False:
                self.callback(True, result['games'])
            else:
                self.callback(False)

        self.action = None

    def ping(self, callback):
        self.callback = callback
        self.action = self.ACTION_PING

    def login(self, callback, username):
        self.username = username
        self.callback = callback
        self.action = self.ACTION_LOGIN

    def lobby(self, callback):
        self.callback = callback
        self.action = self.ACTION_LOBBY

    def createGame(self, callback, name):
        self.callback = callback
        self.action = self.ACTION_CREATE
