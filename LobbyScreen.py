from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button



class LobbyScreen(Screen):
    games = ['Lol', 'Coucou', 'Clique ici !', 'Si tu veux']

    def join_game(self, btn):
        self.manager.gm.partie = btn.text
        self.manager.current = 'play'


    def on_enter(self):
        for g in self.games:
            self.w_grid.add_widget(Button(text=g, on_press=self.join_game))
