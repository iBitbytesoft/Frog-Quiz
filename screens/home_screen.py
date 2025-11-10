"""Home screen with frog selection grid"""
from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from screens.frog_data import FROGS


class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout
        main = FloatLayout()
        
        # Background color
        with main.canvas.before:
            Color(0.18, 0.54, 0.34, 1)
            self.rect = Rectangle(size=main.size, pos=main.pos)
        main.bind(size=self._update_rect, pos=self._update_rect)
        
        # Content container
        content = BoxLayout(orientation='vertical', padding=[20, 20], spacing=20,
                           size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Title
        title = Label(
            text='Select a frog to see and hear its call',
            size_hint=(1, 0.1),
            font_size='36sp',
            color=(1, 1, 1, 1),
            halign='center',
            valign='middle'
        )
        title.bind(size=title.setter('text_size'))
        content.add_widget(title)
        
        # Grid of buttons (5 columns: instructions + 8 frogs + mystery)
        grid = GridLayout(cols=5, spacing=25, size_hint=(1, 0.8), padding=[50, 0])
        
        # Instructions button - Fixed to maintain square aspect ratio
        inst_box = BoxLayout(orientation='vertical', spacing=5)
        
        # Container to maintain square aspect ratio
        inst_btn_container = BoxLayout(size_hint=(1, 0.85))
        inst_btn = Button(background_normal='assets/App_overview.png', 
                         background_down='assets/App_overview.png',
                         size_hint=(None, None))
        inst_btn.bind(on_press=lambda x: self.manager.go_to('instructions'))
        
        # Bind size to maintain square shape
        def update_inst_btn_size(instance, value):
            size = min(instance.width, instance.height)
            for child in instance.children:
                if isinstance(child, Button):
                    child.size = (size, size)
        inst_btn_container.bind(size=update_inst_btn_size)
        
        inst_btn_container.add_widget(Widget())  # Left spacer
        inst_btn_container.add_widget(inst_btn)
        inst_btn_container.add_widget(Widget())  # Right spacer
        inst_box.add_widget(inst_btn_container)
        
        inst_label = Label(text="How spectrograms\nshow sound", font_size='20sp', 
                          color=(1, 1, 1, 1), size_hint=(1, 0.15), halign='center')
        inst_label.bind(size=inst_label.setter('text_size'))
        inst_box.add_widget(inst_label)
        grid.add_widget(inst_box)
        
        # Frog buttons - Fixed to maintain square aspect ratio
        for frog in FROGS:
            frog_box = BoxLayout(orientation='vertical', spacing=5)
            
            # Container to maintain square aspect ratio
            btn_container = BoxLayout(size_hint=(1, 0.85))
            btn = Button(background_normal=frog['photo'], 
                        background_down=frog['photo'],
                        size_hint=(None, None))
            btn.bind(on_press=lambda x, f=frog: self.manager.show_frog(f))
            
            # Bind size to maintain square shape
            def update_btn_size(instance, value):
                size = min(instance.width, instance.height)
                for child in instance.children:
                    if isinstance(child, Button):
                        child.size = (size, size)
            btn_container.bind(size=update_btn_size)
            
            btn_container.add_widget(Widget())  # Left spacer
            btn_container.add_widget(btn)
            btn_container.add_widget(Widget())  # Right spacer
            frog_box.add_widget(btn_container)
            
            lbl = Label(text=frog['name'], font_size='20sp', 
                       color=(1, 1, 1, 1), size_hint=(1, 0.15), halign='center')
            lbl.bind(size=lbl.setter('text_size'))
            frog_box.add_widget(lbl)
            grid.add_widget(frog_box)
        
        # Mystery frog button - Fixed to maintain square aspect ratio
        mystery_box = BoxLayout(orientation='vertical', spacing=5)
        
        # Container to maintain square aspect ratio
        mystery_btn_container = BoxLayout(size_hint=(1, 0.85))
        mystery_btn = Button(background_normal='assets/UnknownFrog.png',
                            background_down='assets/UnknownFrog.png',
                            size_hint=(None, None))
        mystery_btn.bind(on_press=lambda x: self.manager.go_to('mystery'))
        
        # Bind size to maintain square shape
        def update_mystery_btn_size(instance, value):
            size = min(instance.width, instance.height)
            for child in instance.children:
                if isinstance(child, Button):
                    child.size = (size, size)
        mystery_btn_container.bind(size=update_mystery_btn_size)
        
        mystery_btn_container.add_widget(Widget())  # Left spacer
        mystery_btn_container.add_widget(mystery_btn)
        mystery_btn_container.add_widget(Widget())  # Right spacer
        mystery_box.add_widget(mystery_btn_container)
        
        mystery_label = Label(text="Mystery Frog", font_size='20sp', 
                             color=(1, 0.65, 0, 1), size_hint=(1, 0.15), halign='center')  # Orange color to match Windows
        mystery_label.bind(size=mystery_label.setter('text_size'))
        mystery_box.add_widget(mystery_label)
        grid.add_widget(mystery_box)
        
        content.add_widget(grid)
        
        # App Info button
        info_btn = Button(
            text='App Info',
            size_hint=(0.2, 0.08),
            pos_hint={'center_x': 0.5},
            background_color=(0.3, 0.69, 0.31, 1),
            font_size='20sp'
        )
        info_btn.bind(on_press=lambda x: self.manager.go_to('app_info'))
        content.add_widget(info_btn)
        
        main.add_widget(content)
        self.add_widget(main)
        
        # Add triple-tap exit functionality
        self.tap_count = 0
        self.tap_timer = None
        main.bind(on_touch_down=self.on_triple_tap)
    
    def on_triple_tap(self, instance, touch):
        """Handle triple-tap in top-left corner to exit"""
        # Check if tap is in top-left corner (100x100 pixel area)
        if touch.x < 100 and touch.y > (instance.height - 100):
            from kivy.clock import Clock
            import time
            
            current_time = time.time()
            
            # Reset counter if more than 2 seconds since last tap
            if self.tap_timer and (current_time - self.tap_timer) > 2:
                self.tap_count = 0
            
            self.tap_count += 1
            self.tap_timer = current_time
            
            if self.tap_count >= 3:
                # Exit the app
                from kivy.app import App
                App.get_running_app().stop()
                self.tap_count = 0
    
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
