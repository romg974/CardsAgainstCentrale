from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image

class LobbyScreen(Screen):
    games = []

    def __init__(self, **kwargs):
        super(LobbyScreen, self).__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(source='img/bg.jpg')
        self.grid = BoxLayout(orientation='vertical',
                                size_hint=(1, 0.9))
        label = Label(size_hint= (.6,.1),
                      pos_hint= {'x': 0, 'y': .9},
                      text="[b]Liste des parties[/b]\n[i]Cliquez sur une partie pour la rejoindre[/i]",
                      markup=1)
        btn_refresh = Button(size_hint=(.2,.1),
                             pos_hint={'x':.8,'y':.9},
                             text='Rafraichir',
                             on_press=self.fetch_games)
        btn_add = Button(size_hint=(.2,.1),
                         pos_hint={'x':.6,'y':.9},
                         text='Ajouter une partie',
                         on_press=self.add_game)

        layout.add_widget(bg)
        layout.add_widget(self.grid)
        layout.add_widget(label)
        layout.add_widget(btn_refresh)
        layout.add_widget(btn_add)

        self.add_widget(layout)
        self.popup = None

    def join_game_callback(self, ok, message=''):
        if ok:
            self.manager.current = 'play'
        else:
            Popup(title='Erreur !',
                  content=Label(text=message),
                  size_hint=(None, None), size=(400, 400)).open()

    def join_game(self, btn):
        name = btn.text
        self.manager.gm.joinGame(self.join_game_callback, name)

    def add_game_action(self, e=None):
        name = self.add_game_input.text
        self.manager.gm.createGame(self.join_game_callback, name)

    def add_game(self, e=None):
        def add_game(e):
            popup.dismiss()
            self.add_game_action()
        playout = BoxLayout(orientation='vertical', padding=10)
        playout.add_widget(Label(text='Nom de la partie : '))
        self.add_game_input = TextInput()
        playout.add_widget(self.add_game_input)
        playout.add_widget(Button(text='Créer la partie', on_press=add_game))

        popup = Popup(title='Créer une nouvelle partie',
                      content=playout,
                      size_hint=(None, None), size=(400, 400))
        playout.add_widget(Button(text='Annuler', on_press=popup.dismiss))
        popup.open()

    def callback(self, ok, data=[]):
        if ok:
            def add_game(e):
                popup.dismiss()
                self.add_game()
            def refresh(e):
                popup.dismiss()
                self.fetch_games()
            self.games = data
            if len(data) < 1:

                playout = BoxLayout(orientation='vertical')
                playout.add_widget(Label(text='Il n\'y a pas encore de partie, voulez vous en créer une ?'))
                playout.add_widget(Button(text='Créer une partie...', on_press=add_game))
                playout.add_widget(Button(text='Rafraichir', on_press=refresh))
                popup = Popup(title='Information',
                              content=playout,
                              size_hint=(None, None), size=(400, 400))
                popup.open()
            else:
                self.grid.clear_widgets()
                for g in self.games:
                    self.grid.add_widget(Button(text=g['name'], on_press=self.join_game))
        else:
            popup = Popup(title='Erreur !',
                          content=Label(text='Echec de la récuperation des données.'),
                          size_hint=(None, None), size=(400, 400))
            popup.open()

    def fetch_games(self, e=None):
        self.manager.gm.lobby(self.callback)

    def on_enter(self):
        self.fetch_games()
