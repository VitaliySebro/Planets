from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.animation import Animation
from random import randint
from kivy.clock import Clock


class MenuScreen(Screen):
    def _init_(self, **kwargs):
        super().init(**kwargs)


class GameScreen(Screen):
    points = NumericProperty(0)

    def _init_(self, **kwargs):
        super().init(**kwargs)

    def on_enter(self, *args):
        self.ids.planet.new_planet()
        return super().on_enter(*args)


class Shop(Screen):
    def _init_(self, **kwargs):
        super().init(**kwargs)


class Planet(Image): 
    is_anim = False
    hp = None
    planet = None
    planet_index = 0

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.parent.parent.parent.points += 1
            self.hp -= 1
            if self.hp <= 0:
                self.new_planet()  

            x = self.x
            y = self.y
            anim = Animation(x=x - 5, y=y - 5, duration=0.05) + Animation(x=x, y=y, duration=0.05)
            anim.start(self)
            self.is_anim = True
            anim.on_complete = lambda *args: setattr(self, 'is_anim', False)
        return super().on_touch_down(touch)

    def Auto_Clicker(self, switch):
        if switch.active:
            Clock.schedule_interval(self.auto_click, 0.2)  
        else:
            Clock.unschedule(self.auto_click)

    def auto_click(self, dt):
        self.parent.parent.parent.points += 1
        self.hp -= 1
        if self.hp <= 0:
            self.new_planet()  

        x = self.x
        y = self.y
        anim = Animation(x=x - 5, y=y - 5, duration=0.05) + Animation(x=x, y=y, duration=0.05)
        anim.start(self)
        self.is_anim = True
        anim.on_complete = lambda *args: setattr(self, 'is_anim', False)

    def new_planet(self):  
        self.planet = self.LEVELS[randint(0, len(self.LEVELS) - 1)]
        self.source = self.PLANETS[self.planet]['source']
        self.hp = self.PLANETS[self.planet]['hp']


LEVELS = ['Mercury', 'Venus', 'Earth', 'Mars',
          'Jupiter', 'Saturn', 'Uranus', 'Neptune']

PLANETS = {
    'Mercury': {"source": 'assets/planets/1.png', 'hp': 10},
    'Venus': {"source": 'assets/planets/2.png', 'hp': 20},
    'Earth': {"source": 'assets/planets/3.png', 'hp': 30},
    'Mars': {"source": 'assets/planets/4.png', 'hp': 40},
    'Jupiter': {"source": 'assets/planets/5.png', 'hp': 50},
    'Saturn': {"source": 'assets/planets/6.png', 'hp': 60},
    'Uranus': {"source": 'assets/planets/7.png', 'hp': 80},
    'Neptune': {"source": 'assets/planets/8.png', 'hp': 100},
}


