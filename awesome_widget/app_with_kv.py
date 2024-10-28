import kivy
kivy.require('2.3.0')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget

class WaitBar(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (10, 10)
        animation = Animation(pos=(656, 10), t='in_out_cubic') + Animation(pos=(10, 10), t='in_out_cubic')
        animation.repeat = True
        animation.start(self)

class RootWidget(AnchorLayout):
    pass

class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()
