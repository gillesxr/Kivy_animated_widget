import kivy
kivy.require('2.3.0')
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class RootWidget(AnchorLayout):
    pass

class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()
