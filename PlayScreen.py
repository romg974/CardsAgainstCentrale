from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.image import Image

class PlayScreen(Screen):
    cards = []
    sentence = ""

    def __init__(self, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)

        layout = FloatLayout()
        bg = Image(source='img/bg.jpg')
        hud = Image(source='img/hud1.png')
        self.box_cards = BoxLayout(size_hint=(1, .4))
        self.box_players = BoxLayout(size_hint=(.2, .6),
                                     orientation='vertical',
                                     pos_hint={'x': 0, 'y': .4})
        self.red_card = Button(size_hint=(.2, .4),
                                pos_hint={'x': .2, 'y': .5},
                                background_color=(1, 0, 0, 1),
                                 color=(1, 1, 1, 1),
                               valign='center',
                               halign='center')
        self.red_card.text_size = self.red_card.size

        self.box_vote = BoxLayout(size_hint=(.6,.4),
                                  pos_hint={'x': .4, 'y': .5},
                                  orientation='vertical')

        btn_pass = Button(size_hint=(.8, .1),
                          pos_hint={'x': .2, 'y': .4},
                          text="Passer le tour")
        self.lbl_title = Label(size_hint=(.8, .1),
                               pos_hint={'x': .2, 'y': .9})

        layout.add_widget(bg)
        layout.add_widget(hud)
        layout.add_widget(self.box_players)
        layout.add_widget(self.box_cards)
        layout.add_widget(self.red_card)
        layout.add_widget(self.box_vote)
        layout.add_widget(btn_pass)
        layout.add_widget(self.lbl_title)

        self.add_widget(layout)

    def callback(self, ok, data={}):
        if ok:
            self.cards = data['cards']
            self.players = data['players']
            self.sentence = data['sentence']

            if self.sentence != "":
                self.red_card.text = self.sentence % '____'
            else:
                self.red_card.text = "En attente de joueurs..."
            self.box_cards.clear_widgets()
            for id, c in self.cards.items():
                b = Button(text=c,
                           on_press=self.play_card,
                           halign='center',
                           valign='center',
                           background_color=[0, 0, 1, 1],
                           color=[1, 1, 1, 1])
                b.text_size = b.size
                b._idc = id
                self.box_cards.add_widget(b)

            self.box_players.clear_widgets()
            for p in self.players.values():
                color = [0, 1, 0, 1]
                if not p['played']:
                    color = [1, 0, 0, 1]
                l = Label(text="%s (%s)" % (p['name'], p['score']), halign='left', valign='center', color=color)
                l.text_size = l.size
                self.box_players.add_widget(l)

            self.box_vote.clear_widgets()
            if data['state'] == 'voting' or data['state'] == 'score':
                for id, c in data['cards_played'].items():
                    color = [0,0,1,1]
                    if id == data['voted']:
                        color = [0,1,0,1]
                    b = Button(text=c,
                               on_press=self.play_card,
                               halign='center',
                               valign='center',
                               background_color=color,
                               color=[1, 1, 1, 1])
                    b.text_size = b.size
                    b._idc = id
                    self.box_vote.add_widget(b)
        else:
            Popup(title='Erreur !',
                  content=Label(text='Les données de jeu n\'ont pas pu être récupérées.'),
                  size_hint=(None, None), size=(400, 400)).open()

    def play_card(self, btn):
        self.manager.gm.play(self.callback, btn._idc)

    def on_enter(self):
        self.lbl_title.text = self.manager.gm.partie
        self.manager.gm.game(self.callback)

