
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.carousel import Carousel
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.resources import resource_add_path
import os

try:
    Window.size = (1080, 1920)
except Exception:
    pass

resource_add_path(os.path.join(os.path.dirname(__file__), "assets"))

KV = """
<MenuScreen>:
    name: "menu"
    FloatLayout:
        Image:
            source: "fundoumm.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            pos_hint: {"x": 0, "y": 0}
        Button:
            background_normal: ""
            background_color: 0,0,0,0
            size_hint: 0.36, 0.20
            pos_hint: {"x": 0.08, "y": 0.38}
            on_release: root.go_loading()

<LoadingScreen>:
    name: "loading"
    FloatLayout:
        canvas.before:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                size: self.size
                pos: self.pos
        Image:
            source: "fundoumm.jpg"
            allow_stretch: True
            keep_ratio: False
            opacity: 0.15
            size_hint: 1, 1
        Label:
            text: "Carregando..."
            font_size: "36sp"
            size_hint: None, None
            pos_hint: {"center_x": 0.5, "center_y": 0.5}

<GalleryScreen>:
    name: "gallery"
    FloatLayout:
        Image:
            source: "fundodois.jpg"
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
            pos_hint: {"x": 0, "y": 0}
        FloatLayout:
            id: card
            size_hint: 0.86, 0.52
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [28,]
            Carousel:
                id: car
                size_hint: 0.92, 0.82
                pos_hint: {"center_x": 0.5, "center_y": 0.58}
                direction: "right"
                loop: True
            BoxLayout:
                id: dots
                size_hint: 0.5, None
                height: "26dp"
                pos_hint: {"center_x": 0.5, "y": 0.04}
                spacing: "6dp"
                padding: 0,0,0,0
                orientation: "horizontal"
"""
Builder.load_string(KV)

class MenuScreen(Screen):
    def go_loading(self):
        self.manager.current = "loading"
        Clock.schedule_once(lambda dt: setattr(self.manager, 'current', 'gallery'), 2)

class LoadingScreen(Screen):
    pass

class GalleryScreen(Screen):
    def on_pre_enter(self):
        car = self.ids.car
        if len(car.slides) == 0:
            images = ["fotoprimeira.jpg", "img4_3.png", "img4_2.png", "img4.png"]
            for path in images:
                local = os.path.join("assets", path)
                src = path if os.path.exists(path) else local
                img = Image(source=src, allow_stretch=True, keep_ratio=True)
                car.add_widget(img)
            self.build_dots(len(images))
            car.bind(index=self.on_carousel_index)
        self.update_dots(self.ids.car.index)

    def build_dots(self, n):
        dots = self.ids.dots
        dots.clear_widgets()
        for _ in range(n):
            lbl = Label(text="•", font_size="28sp", opacity=0.4)
            dots.add_widget(lbl)

    def on_carousel_index(self, car, idx):
        self.update_dots(idx)

    def update_dots(self, idx):
        dots = self.ids.dots.children[::-1]
        if not dots:
            return
        for i, w in enumerate(dots):
            w.opacity = 1.0 if i == (idx % len(dots)) else 0.35

class Root(ScreenManager):
    pass

class HabilitacaoApp(App):
    def build(self):
        sm = Root(transition=FadeTransition(duration=0.2))
        sm.add_widget(MenuScreen())
        sm.add_widget(LoadingScreen())
        sm.add_widget(GalleryScreen())
        return sm

if __name__ == "__main__":
    HabilitacaoApp().run()
