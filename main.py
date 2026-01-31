from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# إعدادات الواجهة (الأسود والذهبي للسيادة)
Window.clearcolor = (0, 0, 0, 1)

class BridgeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        layout.add_widget(Label(text="[ THE GUARD - NODE 7 ]", font_size='28sp', color=(1, 0.8, 0, 1)))
        
        self.password = TextInput(hint_text="Enter Access Code", password=True, multiline=False,
                                  size_hint=(1, 0.1), background_color=(0.1, 0.1, 0.1, 1),
                                  foreground_color=(1, 1, 1, 1), halign='center')
        
        btn = Button(text="ACTIVATE BRIDGE", size_hint=(1, 0.15), background_color=(0.7, 0, 0, 1))
        btn.bind(on_press=self.verify_access)
        
        layout.add_widget(self.password)
        layout.add_widget(btn)
        self.add_widget(layout)

    def verify_access(self, instance):
        if self.password.text in ["freedom", "499712"]:
            self.manager.current = 'hub'
        else:
            self.password.text = ""
            self.password.hint_text = "INVALID CODE"

class HubScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        layout.add_widget(Label(text="SECURITY CONTROL CENTER", font_size='22sp', size_hint_y=0.1, color=(1, 0.8, 0, 1)))
        
        # الغرف الثلاث المحددة
        layout.add_widget(Button(text="APP WATCHER (PENDING NERVE)", background_color=(0.1, 0.1, 0.3, 1)))
        layout.add_widget(Button(text="LAN GHOST (PENDING NERVE)", background_color=(0.1, 0.1, 0.3, 1)))
        layout.add_widget(Button(text="DATA SENTINEL (PENDING NERVE)", background_color=(0.1, 0.1, 0.3, 1)))
        
        self.add_widget(layout)

class GuardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BridgeScreen(name='bridge'))
        sm.add_widget(HubScreen(name='hub'))
        return sm

if __name__ == '__main__':
    GuardApp().run()
