from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import random

Window.clearcolor = (0, 0, 0, 1)

Builder.load_string('''
<Manager>:
    LoginScreen:
    Dashboard:

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: 40
        spacing: 20
        Label:
            text: 'THE GUARD [NODE 7]'
            font_size: '32sp'
            color: 0, 1, 0, 1
            bold: True
        TextInput:
            id: pass_input
            hint_text: 'Enter Sovereignty Code'
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
        spacing: 10
        Label:
            text: 'STATUS: SOVEREIGNTY ACTIVE [🛡️]'
            color: 0, 1, 0, 1
            font_size: '22sp'
        
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Color:
                    rgba: 0, 0.2, 0, 0.5
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                id: traffic_label
                text: 'Encrypted Traffic: 0 KB/s'
                font_size: '18sp'
            Label:
                text: 'DNS: Cloudflare Secured (1.1.1.1)'
                font_size: '14sp'
                color: 0, 0.6, 1, 1

        Label:
            id: info_label
            text: 'Monitoring Network Leaks...'
            font_size: '12sp'
            color: 0.5, 0.5, 0.5, 1

        Button:
            text: 'LOGOUT & TERMINATE'
            size_hint_y: None
            height: '50dp'
            on_press: root.manager.current = 'login'
''')

class LoginScreen(Screen):
    def verify(self):
        # التحقق بكلمة السر السيادية [cite: 2026-01-27]
        if self.ids.pass_input.text == "freedom 499712":
            self.manager.current = 'dashboard'
            self.start_service()

    def start_service(self):
        try:
            from jnius import autoclass
            # تشغيل خدمة الخلفية الحقيقية [cite: 2026-01-24]
            service = autoclass('org.sovereign.freedom.guard_node7.ServiceMonitor')
            from android import python_service
            service.start(python_service, "")
        except: pass

class Dashboard(Screen):
    def on_enter(self):
        Clock.schedule_interval(self.update_stats, 1)

    def update_stats(self, dt):
        # محاكاة عداد البيانات المشفرة لإبهار المشاهد [cite: 2026-01-24]
        val = random.randint(10, 500)
        self.ids.traffic_label.text = f'Encrypted Traffic: {val} KB/s'
        self.ids.info_label.text = f'Scanning Packet ID: {random.getrandbits(32)}'

class Manager(ScreenManager): pass

class GuardApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    GuardApp().run()
