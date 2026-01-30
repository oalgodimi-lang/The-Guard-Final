from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import socket
import threading
import time

# استدعاء آمن للمكتبات لتجنب DexPathList error
try:
    from jnius import autoclass
    ANDROID_READY = True
except Exception as e:
    ANDROID_READY = False
    ANDROID_ERROR = str(e)

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=20, **kwargs)
        
        self.add_widget(Label(
            text='[b]NODE 7: SOVEREIGN SHIELD v1.1.7[/b]', 
            markup=True, font_size='22sp', size_hint_y=0.1, color=(0, 0.7, 1, 1)
        ))
        
        self.code_input = TextInput(
            hint_text='Enter Freedom Cipher...',
            password=True, multiline=False, size_hint_y=0.1,
            halign='center', background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.code_input)

        self.btn = Button(
            text='ACTIVATE SHIELD', 
            size_hint_y=0.15, background_color=(0, 0.5, 0.8, 1),
            font_size='18sp', bold=True
        )
        self.btn.bind(on_press=lambda x: self.activate_node(self.code_input.text))
        self.add_widget(self.btn)

        self.scroll_view = ScrollView(size_hint_y=0.6)
        self.log_label = Label(
            text="[System Ready]\n>> Checking Android Bridge...\n",
            markup=True, halign='left', valign='top',
            size_hint_y=None, font_size='14sp'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)
        
        if not ANDROID_READY:
            self.update_log(f"[X] Bridge Error: {ANDROID_ERROR}")

    def update_log(self, msg):
        Clock.schedule_once(lambda dt: self._append_msg(msg))

    def _append_msg(self, msg):
        self.log_label.text += f">> {msg}\n"
        self.scroll_view.scroll_y = 0

    def activate_node(self, password):
        if password == "freedom":
            self.update_log("[!] Cipher Accepted. Initializing...")
            threading.Thread(target=self.run_bridge).start()
        else:
            self.update_log("[X] Invalid Cipher.")

    def run_bridge(self):
        if ANDROID_READY:
            try:
                self.update_log("[🛡️] Sending Native Wake-up Signal...")
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                context = PythonActivity.mActivity
                service_name = context.getPackageName() + '.ServiceMonitor'
                service_class = autoclass(service_name)
                intent = autoclass('android.content.Intent')(context, service_class)
                context.startForegroundService(intent)
                self.update_log("[✔] Signal Sent Successfully.")
            except Exception as e:
                self.update_log(f"[!] Bridge Call Failed: {str(e)}")
        
        # محاولة الربط عبر السوكت
        for i in range(3):
            self.update_log(f"Connecting to Node Core (Attempt {i+1})...")
            try:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(2)
                client.connect(('127.0.0.1', 9999))
                client.send(b"ACTIVATE")
                client.close()
                self.update_log("[💎] CORE LINKED: SHIELD ACTIVE.")
                return
            except:
                time.sleep(2)
        self.update_log("[X] Connection Timeout. Service might be sleeping.")

class TheGuardApp(App):
    def build(self):
        return GuardInterface()

if __name__ == '__main__':
    TheGuardApp().run()
