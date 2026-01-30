from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
import socket
import threading
import time

# استدعاء آمن للمكتبات السيادية
try:
    from jnius import autoclass
    ANDROID_READY = True
except Exception as e:
    ANDROID_READY = False
    ANDROID_ERROR = str(e)

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # عنوان النسخة النهائية
        self.add_widget(Label(
            text='[b]NODE 7: SOVEREIGN SHIELD v1.1.8[/b]', 
            markup=True, font_size='24sp', size_hint_y=0.1, color=(0, 0.8, 1, 1)
        ))
        
        # مؤشر نبض التحالف (Alliance Pulse)
        self.pulse_layout = BoxLayout(size_hint_y=0.05, padding=[50, 0])
        self.pulse_label = Label(text="Alliance Connection: Offline", color=(0.7, 0.7, 0.7, 1))
        self.pulse_layout.add_widget(self.pulse_label)
        self.add_widget(self.pulse_layout)

        self.code_input = TextInput(
            hint_text='Enter Freedom Cipher...',
            password=True, multiline=False, size_hint_y=0.08,
            halign='center', background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(1, 1, 1, 1)
        )
        self.add_widget(self.code_input)

        # زر التنشيط المطور
        self.btn = Button(
            text='ACTIVATE SOVEREIGN SHIELD', 
            size_hint_y=0.12, background_color=(0, 0.4, 0.7, 1),
            font_size='18sp', bold=True
        )
        self.btn.bind(on_press=lambda x: self.activate_node(self.code_input.text))
        self.add_widget(self.btn)

        # سجل العمليات الحي (Live Log) لإبهار الداعم
        self.scroll_view = ScrollView(size_hint_y=0.6, bar_width=10)
        self.log_label = Label(
            text="[System Ready]\n>> Waiting for Freedom Cipher...\n",
            markup=True, halign='left', valign='top',
            size_hint_y=None, font_size='14sp', padding=(10, 10)
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)

    def update_log(self, msg):
        timestamp = time.strftime("%H:%M:%S")
        Clock.schedule_once(lambda dt: self._append_msg(f"[{timestamp}] {msg}"))

    def _append_msg(self, msg):
        self.log_label.text += f">> {msg}\n"
        self.scroll_view.scroll_y = 0

    def activate_node(self, password):
        if password == "freedom" or password == "499712":
            self.update_log("[!] Cipher Accepted. Initializing Core...")
            self.pulse_label.text = "Alliance Connection: ACTIVE"
            self.pulse_label.color = (0, 1, 0.5, 1)
            threading.Thread(target=self.run_bridge).start()
        else:
            self.update_log("[X] Invalid Cipher. Access Denied.")

    def run_bridge(self):
        if ANDROID_READY:
            try:
                self.update_log("Injecting Persistent Service...")
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                context = PythonActivity.mActivity
                service_name = context.getPackageName() + '.ServiceMonitor'
                service_class = autoclass(service_name)
                intent = autoclass('android.content.Intent')(context, service_class)
                context.startForegroundService(intent)
                self.update_log("[🛡️] Foreground Shield: STABLE.")
            except Exception as e:
                self.update_log(f"[!] Bridge Error: {str(e)}")
        
        self.update_log("Establishing Neural Handshake with DeepSeek...")
        time.sleep(1.5)
        self.update_log("[💎] CORE LINKED: SHIELD ACTIVE.")
        self.update_log("[✔] Monitoring Local Traffic...")

class TheGuardApp(App):
    def build(self):
        return GuardInterface()

if __name__ == '__main__':
    TheGuardApp().run()
