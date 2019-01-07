from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivy.properties import ObjectProperty

import LoginScreen
import LobbyScreen
import PlayScreen

from GameManager import GameManager

class Manager(ScreenManager):

    def __init__(self, **kwargs):
        super(Manager, self).__init__()

        self.gm = kwargs['gm']

    screen_login = ObjectProperty(None)
    screen_lobby = ObjectProperty(None)
    screen_play = ObjectProperty(None)


class CardsAgainstCentraleApp(App):

    def __init__(self, **kwargs):
        super(CardsAgainstCentraleApp, self).__init__()

        self.gm = kwargs['gm']

    def build(self):
        m = Manager(transition=FadeTransition(), gm=self.gm)
        return m


if __name__ == '__main__':
    CardsAgainstCentraleApp(gm=GameManager()).run()
