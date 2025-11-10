"""App info screen"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class AppInfoScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main = FloatLayout()
        with main.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.rect = Rectangle(size=main.size, pos=main.pos)
        main.bind(size=self._update_rect, pos=self._update_rect)
        
        content = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        title = Label(text='App Info', size_hint=(1, 0.1), font_size='36sp', color=(0, 0, 0, 1), bold=True)
        content.add_widget(title)
        
        # Info text box with border and padding (matching Windows version)
        info_container = BoxLayout(size_hint=(1, 0.7), padding=10)
        with info_container.canvas.before:
            Color(0.3, 0.54, 0, 1)  # Green border color
            info_container.border_rect = Rectangle(size=info_container.size, pos=info_container.pos)
        
        def update_info_border(instance, value):
            info_container.border_rect.pos = instance.pos
            info_container.border_rect.size = instance.size
        info_container.bind(size=update_info_border, pos=update_info_border)
        
        info = Label(
            text='This APP was designed and created by Katie Howard for the exhibition "Litoria\'s Wetland World".\n\n'
                 'Sound files were provided by the Arthur Rylah Institute for Environmental Research (DEECA) '
                 'and compiled with help from Louise Durkin.\n'
                 'The spectrograms were created using PASE (Python-Audio-Spectrogram-Explorer).\n\n'
                 'All photos were taken by Katie Howard except for those listed below, which are used with permission from:\n'
                 '- Zak Atkins: Peron\'s Tree Frog\n'
                 '- Geoff Heard: Pobblebonk Frog and Spotted Marsh Frog',
            font_size='22sp',
            color=(0, 0, 0, 1),
            halign='left',
            valign='top',
            markup=True
        )
        info.bind(size=info.setter('text_size'))
        info_container.add_widget(info)
        content.add_widget(info_container)
        
        back_box = BoxLayout(size_hint=(1, 0.2))
        back_btn = Button(
            background_normal='assets/Arrow.png',
            background_down='assets/Arrow.png',
            size_hint=(0.15, 1),
            pos_hint={'center_x': 0.5}
        )
        back_btn.bind(on_press=lambda x: self.manager.go_to('home'))
        back_box.add_widget(Widget())
        back_box.add_widget(back_btn)
        back_box.add_widget(Widget())
        content.add_widget(back_box)
        
        main.add_widget(content)
        self.add_widget(main)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
