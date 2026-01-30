from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from jnius import autoclass
import socket
import time
import threading

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=20, **kwargs)
        
        # شعار العقدة السابعة
        self.add_widget(Label(
            text='[b]NODE 7: SOVEREIGN SHIELD[/b]', 
            markup=True, font_size='24sp', size_hint_y=0.1, color=(0, 0.7, 1, 1)
        ))
        
        self.code_input = TextInput(
            hint_text='Enter Freedom Cipher...',
            password=True, multiline=False, size_hint_y=0.1,
            padding_y=(10, 10), halign='center', background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.code_input)

        self.btn = Button(
            text='ACTIVATE STEALTH MODE', 
            size_hint_y=0.15, background_color=(0, 0.6, 0, 1),
            font_size='18sp', bold=True
        )
        self.btn.bind(on_press=lambda x: self.activate_node(self.code_input.text))
        self.add_widget(self.btn)

        self.scroll_view = ScrollView(size_hint_y=0.6)
        self.log_label = Label(
            text="[System Ready]\n>> Waiting for Freedom Cipher...\n",
            markup=True, halign='left', valign='top',
            size_hint_y=None, font_size='14sp', color=(0.8, 0.8, 0.8, 1)
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)

    def activate_node(self, password):
        if password == "freedom":
            self.update_log("[!] Cipher Accepted. Initializing Core Protocols...")
            # إطلاق خيط الاتصال والتشغيل الإجباري
            threading.Thread(target=self.connection_retry_logic).start()
        else:
            self.update_log("[X] Access Denied: Invalid Cipher.")

    def connection_retry_logic(self):
        # --- حقنة الاستيقاظ الإجباري (Android Native Call) ---
        try:
            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            context = PythonActivity.mActivity
            service_name = context.getPackageName() + '.ServiceMonitor'
            service_class = autoclass(service_name)
            intent = autoclass('android.content.Intent')(context, service_class)
            # إرغام النظام على تشغيل الخدمة فوراً
            context.startForegroundService(intent) 
            self.update_log("[🛡️] High-Priority Wake-up Signal Sent.")
        except Exception as e:
            self.update_log(f"[!] System Call Warning: {str(e)}")

        # --- حلقة المصافحة الرقمية ---
        for i in range(5):
            self.update_log(f">> Attempting to link with Core (Trial {i+1}/5)...")
            if self.send_socket_command("ACTIVATE_STEALTH"):
                self.update_log("[✔] GHOST MODE ACTIVE: Shield Engaged.")
                Clock.schedule_once(lambda dt: self.set_button_success())
                return
            time.sleep(2) # مهلة ثانية بين المحاولات لضمان الاستقرار
        
        self.update_log("[X] Final Error: Core is unresponsive. Please check app permissions.")

    def set_button_success(self):
        self.btn.text = "SHIELD ACTIVE"
        self.btn.background_color = (0, 0.4, 0.9, 1)

    def send_socket_command(self, cmd):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1.5)
            client.connect(('127.0.0.1', 9999))
            client.send(cmd.encode('utf-8'))
            client.close()
            return True
        except:
            return False

    def update_log(self, msg):
        Clock.schedule_once(lambda dt: self._append_msg(msg))

    def _append_msg(self, msg):
        self.log_label.text += f">> {msg}\n"
        self.scroll_view.scroll_y = 0

class TheGuardApp(App):
    def build(self):
        return GuardInterface()

if __name__ == '__main__':
    TheGuardApp().run()
