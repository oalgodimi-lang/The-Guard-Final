from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import random

Window.clearcolor = (0, 0, 0, 1)

Builder.load_string('''
<Manager>:
    ShowcaseLogin:
    Dashboard:
    MonitorRoom:
    ObfuscatorRoom:
    AnalystRoom:

<ShowcaseLogin>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: 'THE GUARD - NODE 7'
            font_size: '28sp'
            color: 0, 1, 0, 1
            bold: True
        Label:
            text: 'SOVEREIGNTY PROTOCOL ACTIVE'
            font_size: '14sp'
            color: 0, 0.5, 0, 1
        TextInput:
            id: code_input
            hint_text: 'Enter Sovereignty Code...'
            password: True
            multiline: False
            size_hint_y: None
            height: '50dp'
            background_color: 0.1, 0.1, 0.1, 1
            foreground_color: 0, 1, 0, 1
        Button:
            text: 'INITIALIZE SYSTEM'
            bold: True
            background_color: 0, 0.4, 0, 1
            on_press: root.verify()

<Dashboard>:
    name: 'dashboard'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        Label:
            text: 'CONTROL CENTER / DASHBOARD'
            color: 0, 1, 0, 1
            font_size: '20sp'
            bold: True
        Button:
            text: '[📊] DATA MONITORING'
            background_color: 0.1, 0.1, 0.1, 1
            on_press: root.manager.current = 'monitor'
        Button:
            text: '[📡] NETWORK OBFUSCATOR'
            background_color: 0.1, 0.1, 0.1, 1
            on_press: root.manager.current = 'obfuscator'
        Button:
            text: '[🧠] SECURITY ANALYST'
            background_color: 0.1, 0.1, 0.1, 1
            on_press: root.manager.current = 'analyst'
        Button:
            text: 'LOGOUT SYSTEM'
            size_hint_y: None
            height: '45dp'
            background_color: 0.5, 0, 0, 1
            on_press: root.manager.current = 'login'

<MonitorRoom>:
    name: 'monitor'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            id: traffic_label
            text: 'SCANNING NETWORK...'
            font_size: '22sp'
            color: 0, 1, 0, 1
        Label:
            id: app_status
            text: 'APPS SECURE'
            color: 0, 0.7, 1, 1
        Label:
            id: alert_label
            text: 'STATUS: SHIELD ACTIVE'
        Label:
            id: countdown_label
            text: ''
            font_size: '70sp'
            bold: True
            color: 1, 0, 0, 1
        Button:
            text: 'BACK TO COMMAND'
            size_hint_y: None
            height: '50dp'
            on_press: root.back_to_dash()

<ObfuscatorRoom>:
    name: 'obfuscator'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: 'NETWORK OBFUSCATION ACTIVE'
            color: 0, 0.6, 1, 1
            font_size: '18sp'
            bold: True
        Label:
            id: app_shield
            text: 'PROTECTING: SYSTEM'
            color: 1, 1, 0, 1
        Label:
            id: packet_label
            text: 'Injecting Dummy Stream...'
            font_size: '11sp'
            color: 0.5, 0.5, 0.5, 1
        Button:
            text: 'STOP BRIDGE'
            size_hint_y: None
            height: '50dp'
            on_press: root.manager.current = 'dashboard'

<AnalystRoom>:
    name: 'analyst'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        Label:
            id: analyst_text
            text: 'Expert waiting for security logs...'
            halign: 'center'
            font_size: '16sp'
        Button:
            text: 'ANALYZE SECURITY EVENTS'
            size_hint_y: None
            height: '60dp'
            background_color: 0, 0.3, 0.6, 1
            on_press: root.explain()
        Button:
            text: 'BACK'
            on_press: root.manager.current = 'dashboard'
''')

class ShowcaseLogin(Screen):
    def verify(self):
        if self.ids.code_input.text == "freedom 499712":
            self.manager.current = 'dashboard'

class Dashboard(Screen): pass

class MonitorRoom(Screen):
    def on_enter(self):
        self.destruction_counter = 10
        self.is_critical = False
        self.event = Clock.schedule_interval(self.update_traffic, 1)
    
    def update_traffic(self, dt):
        apps = ["Telegram", "Facebook", "X (Twitter)", "WhatsApp", "System"]
        selected_app = random.choice(apps)
        out_val = random.randint(5, 150)
        
        self.ids.traffic_label.text = f"APP: {selected_app}"
        self.ids.app_status.text = f"TRAFFIC: {out_val} kb/s"
        
        if out_val > 120 and not self.is_critical:
            self.is_critical = True
            self.ids.alert_label.text = f"🚨 DATA LEAK DETECTED IN {selected_app.upper()}!"
            self.ids.alert_label.color = (1, 0, 0, 1)
            Clock.schedule_interval(self.start_self_destruct, 1)
        
        if not self.is_critical:
            self.ids.alert_label.text = "STATUS: SHIELD ACTIVE"
            self.ids.alert_label.color = (0, 1, 0, 1)

    def start_self_destruct(self, dt):
        if self.destruction_counter > 0:
            Window.clearcolor = (0.4, 0, 0, 1) if self.destruction_counter % 2 == 0 else (0, 0, 0, 1)
            self.ids.countdown_label.text = str(self.destruction_counter)
            self.destruction_counter -= 1
        else:
            Window.clearcolor = (0, 0, 0, 1)
            self.ids.traffic_label.text = "MEMORY PURGED"
            self.ids.app_status.text = "ALL DATA WIPED"
            self.ids.alert_label.text = "SAFE FROM INTRUDERS"
            self.ids.countdown_label.text = "OFFLINE"
            return False

    def back_to_dash(self):
        Clock.unschedule(self.event)
        Window.clearcolor = (0, 0, 0, 1)
        self.manager.current = 'dashboard'

class ObfuscatorRoom(Screen):
    def on_enter(self):
        self.ob_event = Clock.schedule_interval(self.send_dummy, 0.2)
    def send_dummy(self, dt):
        apps = ["Telegram", "Facebook", "X", "Meta"]
        hex_data = "".join(random.choice("0123456789ABCDEF") for _ in range(24))
        self.ids.app_shield.text = f"PROTECTING: {random.choice(apps)}"
        self.ids.packet_label.text = f"OBFUSCATING: 0x{hex_data}"
    def on_leave(self):
        Clock.unschedule(self.ob_event)

class AnalystRoom(Screen):
    def explain(self):
        explanations = [
            "Unauthorized access to local network blocked.",
            "Obfuscation bridge preventing packet sniffing.",
            "All outgoing Telegram metadata converted to HEX.",
            "Security shield active on Node 7 Bridge."
        ]
        self.ids.analyst_text.text = random.choice(explanations)

class Manager(ScreenManager): pass

class GuardApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    GuardApp().run()
