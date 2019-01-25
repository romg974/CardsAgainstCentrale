from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

import time


# Declare both screens
class LoginScreen(Screen):
    message = StringProperty()

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # Draw widgets
        layout = FloatLayout()
        glayout = GridLayout(size_hint=(0.5,0.25),
                             pos_hint={'x': .25, 'y': .25},
                             rows=2,
                             cols=2,
                             padding=10,
                             spacing=10)
        label1 = Label(text="Nom : ")
        self.f_username = TextInput()
        self.label = Label(text=self.message)
        btn = Button(text="Connexion", on_press=self.submit)

        glayout.add_widget(label1)
        glayout.add_widget(self.f_username)
        glayout.add_widget(self.label)
        glayout.add_widget(btn)
        layout.add_widget(glayout)
        self.add_widget(layout)

    def callback_ping(self, success):
        self.label.text = 'Ping successful'

    def callback_login(self, success, msg=''):
        if success:
            self.manager.current = 'lobby'
        else:
            print('Fail')
            self.label.text = msg

    def on_enter(self):
        pass

    def submit(self, e):
        self.manager.gm.login(self.callback_login, self.f_username.text)
