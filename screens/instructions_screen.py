"""Instructions screen showing spectrogram explanation"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line


class InstructionsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main = FloatLayout()
        with main.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size=main.size, pos=main.pos)
        main.bind(size=self._update_rect, pos=self._update_rect)
        
        content = BoxLayout(orientation='vertical', padding=15, spacing=8)
        
        # Title (smaller)
        title = Label(
            text='Spectrograms display the frequency and amplitude of sound',
            size_hint=(1, 0.06),
            font_size='24sp',
            color=(0, 0.5, 0, 1),
            bold=True,
            halign='center'
        )
        title.bind(size=title.setter('text_size'))
        content.add_widget(title)
        
        # Main spectrogram image (larger - this is the key element)
        img = Image(source='assets/example.png', size_hint=(1, 0.7))
        content.add_widget(img)
        
        # Bottom section: Back button and explanation boxes
        bottom_section = BoxLayout(size_hint=(1, 0.24), spacing=15)
        
        # Back button - maintain square aspect
        back_container = BoxLayout(size_hint=(0.15, 1))
        back_btn = Button(
            background_normal='assets/Arrow.png',
            background_down='assets/Arrow.png',
            size_hint=(None, None)
        )
        back_btn.bind(on_press=lambda x: self.manager.go_to('home'))
        back_container.bind(size=lambda i, v: self._update_button_size(back_btn, i))
        back_container.add_widget(back_btn)
        bottom_section.add_widget(back_container)
        
        # Green box explanation
        green_box = FloatLayout(size_hint=(0.425, 1))
        green_label = Label(
            text='The call in the [b]green box[/b] has a higher [b]frequency[/b].',
            size_hint=(1, 1),
            font_size='16sp',
            color=(0, 0, 0, 1),
            halign='center',
            valign='middle',
            markup=True,
            padding=(10, 10)
        )
        green_label.bind(size=lambda l, s: setattr(l, 'text_size', (s[0] - 20, s[1] - 20)))
        
        # Draw green border
        with green_box.canvas.after:
            Color(0.3, 0.69, 0.31, 1)  # Green color
            self.green_line = Line(width=3)
        green_box.bind(pos=self._update_green_border, size=self._update_green_border)
        
        green_box.add_widget(green_label)
        bottom_section.add_widget(green_box)
        
        # Yellow box explanation
        yellow_box = FloatLayout(size_hint=(0.425, 1))
        yellow_label = Label(
            text='The call in the [b]yellow box[/b] is higher in [b]amplitude[/b].',
            size_hint=(1, 1),
            font_size='16sp',
            color=(0, 0, 0, 1),
            halign='center',
            valign='middle',
            markup=True,
            padding=(10, 10)
        )
        yellow_label.bind(size=lambda l, s: setattr(l, 'text_size', (s[0] - 20, s[1] - 20)))
        
        # Draw yellow border
        with yellow_box.canvas.after:
            Color(1, 0.84, 0, 1)  # Yellow color
            self.yellow_line = Line(width=3)
        yellow_box.bind(pos=self._update_yellow_border, size=self._update_yellow_border)
        
        yellow_box.add_widget(yellow_label)
        bottom_section.add_widget(yellow_box)
        
        content.add_widget(bottom_section)
        
        main.add_widget(content)
        self.add_widget(main)
        self.green_box = green_box
        self.yellow_box = yellow_box
    
    def _update_button_size(self, button, container):
        """Maintain square aspect ratio for buttons"""
        if container.width > 0 and container.height > 0:
            size = min(container.width, container.height)
            button.size = (size, size)
    
    def _update_green_border(self, instance, value):
        """Update green border rectangle"""
        self.green_line.rectangle = (instance.x, instance.y, instance.width, instance.height)
    
    def _update_yellow_border(self, instance, value):
        """Update yellow border rectangle"""
        self.yellow_line.rectangle = (instance.x, instance.y, instance.width, instance.height)
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
