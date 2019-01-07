from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label



class PlayScreen(Screen):
    cards = ['Coco', 'Un 1A', 'des crepes', 'J\'aime', 'Hoho', 'Hello', 'Un bout de chat qui est long comme la phrase pour voir la longueur des phrases voila']
    sentence = "Ce matin j'irais bien %s"

    def play_card(self, btn):
        pass

    def on_enter(self):
        for c in self.cards:
            b = Button(text=c, on_press=self.play_card, halign='center', valign='center')
            b.text_size = b.size
            self.w_cards.add_widget(b)

        l = Label(text=self.manager.gm.username+" (0)", halign='left', valign='center')
        l.text_size = l.size
        self.w_players.add_widget(l)

        self.w_title.text = self.manager.gm.partie
