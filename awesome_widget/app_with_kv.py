import kivy
kivy.require('2.3.0')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

class WaitBar(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pos = (10, 10)
        self.animation = Animation(pos=((Winwow.width * 0.9) - 64, 10), t='in_out_cubic') + Animation(pos=(10, 10), t='in_out_cubic')
        self.animation.repeat = True
        self.animation.start(self)
        Window.bind(on_resize=self.on_window_resize)

    def on_window_resize(self, window, width, height):
        self.animation.cancel(self)
        self.animation = Animation(pos=((width * 0.9) - 64 , 10), t='in_out_cubic') + Animation(pos=(10, 10), t='in_out_cubic')
        self.animation.repeat = True
        self.animation.start(self)

class RootWidget(AnchorLayout):
    pass

class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()
