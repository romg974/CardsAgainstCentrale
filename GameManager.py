import threading
import time
import requests

class GameManager(threading.Thread):
    api = 'http://localhost/CAC/'

    username = ''
    userkey = ''
    partie = ''
    card = ''
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
                print(payload)
                r = requests.post(self.api + '?' + uri, data=payload, headers={'X-UK': self.userkey})
            else:
                r = requests.get(self.api+'?'+uri, headers={'X-UK': self.userkey})
            if r.status_code != 200:
                print(r.text)

                return False
            else:
                print(r.text)
                return r.json()
        except:
            return False

    def perform_calls(self):
        actiondebut = self.action
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
        elif self.action == self.ACTION_CREATE or self.action == self.ACTION_JOIN:
            if self.action == self.ACTION_CREATE: act = 'create'
            else: act = 'join'
            result = self.request(act, {'name': self.partie})
            if result != False:
                if result['ok']:
                    self.callback(True)
                else:
                    self.callback(False, result['message'])
            else:
                self.callback(False)
        elif self.action in [self.ACTION_GAME, self.ACTION_PLAY, self.ACTION_VOTE]:
            if self.action == self.ACTION_GAME:
                result = self.request('game')
            else:
                result = self.request('game', {'card': self.card})
            if result != False:
                self.callback(True, result)
            else:
                self.callback(False)

        if actiondebut == self.action:
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
        self.partie = name
        self.action = self.ACTION_CREATE

    def joinGame(self, callback, name):
        self.callback = callback
        self.partie = name
        self.action = self.ACTION_JOIN

    def play(self, callback, card):
        self.callback = callback
        self.card = card
        self.action = self.ACTION_PLAY

    def vote(self, callback, card):
        self.callback = callback
        self.card = card
        self.action = self.ACTION_VOTE

    def game(self, callback):
        self.callback = callback
        self.action = self.ACTION_GAME

