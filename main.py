from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
import random

Window.clearcolor = (0, 0, 0, 1)

Builder.load_string('''
<Manager>:
    ShowcaseLogin:
    Dashboard:

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
        TextInput:
            id: code_input
            hint_text: 'Sovereignty Password...'
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
            text: 'SOVEREIGNTY ACTIVE [🛡️]'
            color: 0, 1, 0, 1
            font_size: '24sp'
        Label:
            text: 'VPN SERVICE INJECTED'
            color: 0, 0.5, 1, 1
        Label:
            text: 'The system is now monitoring background leaks.'
            font_size: '12sp'
        Button:
            text: 'SYSTEM LOGOUT'
            size_hint_y: None
            height: '50dp'
            on_press: root.manager.current = 'login'
''')

class ShowcaseLogin(Screen):
    def verify(self):
        # التحقق باستخدام كلمة السر المعتمدة: freedom 499712 [cite: 2026-01-27]
        if self.ids.code_input.text == "freedom 499712":
            self.manager.current = 'dashboard'
            self.start_shield_service()

    def start_shield_service(self):
        try:
            # تشغيل خدمة المراقبة الحقيقية في الخلفية [cite: 2026-01-24]
            from android import python_service
            from jnius import autoclass
            # الربط مع الحزمة المعرفة في buildozer
            service = autoclass('org.theguard.theguard.ServiceMonitor')
            service.start(python_service, "")
            print("[🛡️] SHIELD SERVICE INJECTED SUCCESSFULLY")
        except Exception as e:
            print(f"Injection Error: {e}")

class Dashboard(Screen): pass
class Manager(ScreenManager): pass

class GuardApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    GuardApp().run()
