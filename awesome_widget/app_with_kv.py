import kivy
kivy.require('2.3.0')
from kivy.animation import Animation
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window

class WaitBar(Widget):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.pos = (10, 10)
        self.set_animation(Window.width)
        Window.bind(on_resize=self.on_window_resize)

    def set_animation(self, width: int) -> None:
        """The end abscissa is defined by the current window width by 0.9, the
        popup abscissa size_hint, substract by 64, the size of the rectangle
        (30) plus the popup border (24) plus the end offset we want (10).
        """
        self.animation = Animation(pos=((width * 0.9) - 64, 10), t='in_out_cubic')
        self.animation += Animation(pos=(10, 10), t='in_out_cubic')
        self.animation.repeat = True

    def start_animation(self):
        self.animation.start(self)

    def on_window_resize(self, window: Window, width: int, height: int) -> None:
        self.animation.cancel(self)
        self.set_animation(width)
        self.animation.start(self)

class RootWidget(AnchorLayout):
    pass

class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()
