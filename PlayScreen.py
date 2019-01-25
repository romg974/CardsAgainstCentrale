from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

class PlayScreen(Screen):
    cards = ['Coco', 'Un 1A', 'des crepes', 'J\'aime', 'Hoho', 'Hello', 'Un bout de chat qui est long comme la phrase pour voir la longueur des phrases voila']
    sentence = "Ce matin j'irais bien %s"

    def __init__(self, **kwargs):
        super(PlayScreen, self).__init__(**kwargs)

        layout = FloatLayout()
        self.box_cards = BoxLayout(size_hint=(1,.4))
        self.box_players = BoxLayout(size_hint=(.2,.6),
                                     pos_hint={'x': 0, 'y': .4})
        btn_pass = Button(size_hint=(.8,.1),
                          pos_hint={'x':.2,'y':.4},
                          text="Passer le tour")
        self.lbl_title = Label(size_hint=(.8,.1),
                               pos_hint={'x': .2, 'y': .9})

        layout.add_widget(self.box_players)
        layout.add_widget(self.box_cards)
        layout.add_widget(btn_pass)
        layout.add_widget(self.lbl_title)

        self.add_widget(layout)


    def play_card(self, btn):
        pass

    def on_enter(self):
        for c in self.cards:
            b = Button(text=c, on_press=self.play_card, halign='center', valign='center')
            b.text_size = b.size
            self.box_cards.add_widget(b)

        l = Label(text=self.manager.gm.username+" (0)", halign='left', valign='center')
        l.text_size = l.size
        self.box_players.add_widget(l)

        self.lbl_title.text = self.manager.gm.partie
