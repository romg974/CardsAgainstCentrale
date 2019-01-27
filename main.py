from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.properties import ObjectProperty

from LoginScreen import *
from LobbyScreen import *
from PlayScreen import *

from GameManager import GameManager

from kivy.config import Config
Config.set('graphics', 'resizable', False)

# Screen manager, used to manage screen switchs
class Manager(ScreenManager):

    def __init__(self, **kwargs):
        super(Manager, self).__init__()

        self.gm = kwargs['gm']

        self.add_widget(LoginScreen(name='login'))
        self.add_widget(LobbyScreen(name='lobby'))
        self.add_widget(PlayScreen(name='play'))

    screen_login = ObjectProperty(None)
    screen_lobby = ObjectProperty(None)
    screen_play = ObjectProperty(None)


class CardsAgainstCentraleApp(App):

    def __init__(self, **kwargs):
        super(CardsAgainstCentraleApp, self).__init__()

        # Game manager handling game logic
        self.gm = kwargs['gm']

    def build(self):
        m = Manager(transition=FadeTransition(), gm=self.gm)
        return m


if __name__ == '__main__':
    gm = GameManager()
    gm.start()
    CardsAgainstCentraleApp(gm=gm).run()
