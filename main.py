from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.animation import Animation

# الأساس البصري المعتمد
Window.clearcolor = (0, 0, 0, 1)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text='[color=#00FF00]NODE 7[/color]', markup=True, font_size='48sp', size_hint_y=0.4))
        
        self.password_input = TextInput(hint_text='Key to Freedom', password=True, multiline=False, size_hint_y=0.1, background_color=(0.1, 0.1, 0.1, 1), foreground_color=(0, 1, 0, 1), halign='center')
        layout.add_widget(self.password_input)
        
        btn = Button(text='ENTER', size_hint_y=0.1, background_color=(0, 0.5, 0, 1))
        btn.bind(on_press=self.check_password)
        layout.add_widget(btn)
        self.add_widget(layout)

    def check_password(self, instance):
        if self.password_input.text == 'freedom':
            self.manager.current = 'main_app'

# --- الغرف الجديدة (الحقن البصري) ---

class AppVaultScreen(Screen): # غرفة مراقبة التطبيقات
    def __init__(self, **kwargs):
        super(AppVaultScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='[color=#00FF00]APP VAULT - RADAR[/color]', markup=True, font_size='24sp', size_hint_y=0.1))
        
        scroll = ScrollView()
        list_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        list_layout.bind(minimum_height=list_layout.setter('height'))
        
        # محاكاة الرادار الصامت
        apps = [("System Kernel", "SAFE"), ("Network Driver", "SAFE"), ("Unknown Process", "SUSPICIOUS")]
        for app, status in apps:
            color = "00FF00" if status == "SAFE" else "FF0000"
            lbl = Label(text=f"{app} [color=#{color}][ {status} ][/color]", markup=True, size_hint_y=None, height=50)
            list_layout.add_widget(lbl)
            
        scroll.add_widget(list_layout)
        layout.add_widget(scroll)
        
        btn_back = Button(text='BACK TO COMMAND', size_hint_y=0.1, background_color=(0.2, 0.2, 0.2, 1))
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_app'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class GhostRoomScreen(Screen): # غرفة الشبكات
    def __init__(self, **kwargs):
        super(GhostRoomScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='[color=#00FF00]GHOST ROOM - NETWORK[/color]', markup=True, font_size='24sp', size_hint_y=0.1))
        
        info = Label(text="SSID: Node7_Secure\nGateway: 192.168.1.1\nDNS: 8.8.8.8", halign='center')
        layout.add_widget(info)
        
        btn_mirage = Button(text='ACTIVATE MIRAGE PROTOCOL', size_hint_y=0.2, background_color=(0, 0.3, 0.5, 1))
        layout.add_widget(btn_mirage)
        
        btn_back = Button(text='BACK', size_hint_y=0.1, background_color=(0.2, 0.2, 0.2, 1))
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_app'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class SentinelRoomScreen(Screen): # غرفة الاختراق
    def __init__(self, **kwargs):
        super(SentinelRoomScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='[color=#00FF00]SENTINEL - INTRUSION LOG[/color]', markup=True, font_size='24sp', size_hint_y=0.1))
        
        layout.add_widget(Label(text="[Crystal Firewall: ACTIVE]", color=(0, 1, 1, 1)))
        layout.add_widget(Label(text="No intrusion attempts detected.", font_size='14sp'))
        
        btn_back = Button(text='BACK', size_hint_y=0.1, background_color=(0.2, 0.2, 0.2, 1))
        btn_back.bind(on_press=lambda x: setattr(self.manager, 'current', 'main_app'))
        layout.add_widget(btn_back)
        self.add_widget(layout)

class MainAppScreen(Screen):
    def __init__(self, **kwargs):
        super(MainAppScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        layout.add_widget(Label(text='[color=#00FF00]COMMAND CENTER[/color]', markup=True, font_size='36sp', size_hint_y=0.2))
        
        btn1 = Button(text='APP MONITORING', background_color=(0.1, 0.1, 0.1, 1), color=(0, 1, 0, 1))
        btn1.bind(on_press=lambda x: setattr(self.manager, 'current', 'app_vault'))
        
        btn2 = Button(text='NETWORK & JAMMING', background_color=(0.1, 0.1, 0.1, 1), color=(0, 1, 0, 1))
        btn2.bind(on_press=lambda x: setattr(self.manager, 'current', 'ghost_room'))
        
        btn3 = Button(text='INTRUSION DETECTOR', background_color=(0.1, 0.1, 0.1, 1), color=(0, 1, 0, 1))
        btn3.bind(on_press=lambda x: setattr(self.manager, 'current', 'sentinel_room'))
        
        layout.add_widget(btn1); layout.add_widget(btn2); layout.add_widget(btn3)
        self.add_widget(layout)

class SovereignShieldApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainAppScreen(name='main_app'))
        sm.add_widget(AppVaultScreen(name='app_vault'))
        sm.add_widget(GhostRoomScreen(name='ghost_room'))
        sm.add_widget(SentinelRoomScreen(name='sentinel_room'))
        return sm

if __name__ == '__main__':
    SovereignShieldApp().run()
