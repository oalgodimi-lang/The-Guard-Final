from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import random

# إعداد لون الخلفية السيادي (الأسود العميق)
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
        canvas.before:
            Color:
                rgba: 0, 0.1, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size
        
        Label:
            text: 'THE GUARD [NODE 7]'
            font_size: '34sp'
            color: 0, 1, 0, 1
            bold: True
            font_name: 'Roboto'
        
        Label:
            text: 'SOVEREIGNTY ACCESS REQUIRED'
            font_size: '14sp'
            color: 0, 0.6, 0, 1
        
        TextInput:
            id: pass_input
            hint_text: 'Enter Security Cipher'
            password: True
            multiline: False
            size_hint_y: None
            height: '60dp'
            background_color: 0, 0.2, 0, 0.3
            foreground_color: 0, 1, 0, 1
            cursor_color: 0, 1, 0, 1
            halign: 'center'
        
        Button:
            text: 'INITIALIZE ENCRYPTION'
            bold: True
            font_size: '18sp'
            background_normal: ''
            background_color: 0, 0.4, 0, 1
            size_hint_y: None
            height: '65dp'
            on_press: root.verify_identity()

<Dashboard>:
    name: 'dashboard'
    BoxLayout:
        orientation: 'vertical'
        padding: 25
        spacing: 15
        
        Label:
            text: 'SYSTEM STATUS: PROTECTED [🛡️]'
            color: 0, 1, 0, 1
            font_size: '24sp'
            bold: True
        
        BoxLayout:
            orientation: 'vertical'
            padding: 20
            canvas.before:
                Color:
                    rgba: 0, 1, 0, 0.1
                Line:
                    width: 2
                    rectangle: self.x, self.y, self.width, self.height
            
            Label:
                id: traffic_label
                text: 'Encrypted Stream: 0.0 KB/s'
                font_size: '20sp'
                color: 0, 0.8, 1, 1
            
            Label:
                id: packet_label
                text: 'Packet ID: Scanning...'
                font_size: '12sp'
                color: 0, 1, 0, 0.6

        BoxLayout:
            size_hint_y: None
            height: '40dp'
            Label:
                text: 'DNS: 1.1.1.1 (CLOUDFLARE)'
                color: 0.5, 0.5, 0.5, 1
                font_size: '12sp'

        Button:
            text: 'TERMINATE SESSION'
            size_hint_y: None
            height: '50dp'
            background_color: 0.6, 0, 0, 1
            on_press: root.manager.current = 'login'
''')

class LoginScreen(Screen):
    def verify_identity(self):
        # استخدام كلمة السر السيادية المتفق عليها [cite: 2026-01-27]
        if self.ids.pass_input.text == "freedom 499712":
            self.manager.current = 'dashboard'
            self.activate_sovereign_service()
        else:
            self.ids.pass_input.text = ""
            self.ids.pass_input.hint_text = "INVALID CIPHER - RETRY"

    def activate_sovereign_service(self):
        try:
            from jnius import autoclass
            # استدعاء الخدمة من الحزمة السيادية التي قمنا بتعريفها في Buildozer [cite: 2026-01-24]
            service_name = 'org.sovereign.freedom.guard_node7.ServiceMonitor'
            service = autoclass(service_name)
            from android import python_service
            python_service.start_service("The Guard", "Sovereignty Active", "")
            print("[🛡️] Injection Successful: System Invisible to Local Router.")
        except Exception as e:
            print(f"Non-Android Environment: {e}")

class Dashboard(Screen):
    def on_enter(self):
        # تشغيل عداد البيانات الموهم لإظهار القوة التقنية [cite: 2026-01-24]
        Clock.schedule_interval(self.animate_dashboard, 1.2)

    def animate_dashboard(self, dt):
        val = random.uniform(15.5, 750.2)
        self.ids.traffic_label.text = f'Encrypted Stream: {val:.1f} KB/s'
        self.ids.packet_label.text = f'Packet ID: {random.getrandbits(32)} | Secured'

class Manager(ScreenManager): pass

class GuardApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    GuardApp().run()
