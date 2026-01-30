from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import threading
import socket

# تم استبدال OSC بالمقابس المحلية لضمان السيادة والاستقرار
OSC_AVAILABLE = False 

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # حالة النظام (الواجهة السيادية)
        self.status_label = Label(
            text='[b]SYSTEM STATUS: INITIALIZING...[/b]',
            markup=True, color=(1, 1, 0, 1), font_size='22sp', size_hint_y=0.1
        )
        self.add_widget(self.status_label)

        # رادار السجلات (اللوحة الحية)
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.log_label = Label(
            text="[System Booting...]\n>> Sockets Interface Loaded.\n",
            markup=True, align='left', valign='top',
            size_hint_y=None, font_size='14sp'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)

        # زر فحص العتاد
        self.stats_label = Label(
            text='HARDWARE TOKEN: READY',
            color=(0, 0.7, 1, 1), size_hint_y=0.1
        )
        self.add_widget(self.stats_label)

    def send_command(self, command):
        """إرسال الأوامر عبر الأعصاب الرقمية (Sockets)"""
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(2) # مهلة زمنية لعدم تجميد الواجهة
            client.connect(('127.0.0.1', 9999))
            client.send(command.encode('utf-8'))
            client.close()
            return True
        except Exception as e:
            self.update_ui(f"CONNECTION ERROR: {e}")
            return False

    def activate_node(self, password):
        """تفعيل العقدة السابعة عند إدخال كلمة السر"""
        if password == "freedom":
            if self.send_command("ACTIVATE_STEALTH"):
                self.update_ui("[✔] COMMAND SENT: Stealth Mode Initialized.")
                self.status_label.text = "[b]SYSTEM STATUS: PROTECTED[/b]"
                self.status_label.color = (0, 1, 0, 1)
            else:
                self.update_ui("[!] Service Unreachable. Core might be offline.")

    def update_ui(self, text):
        Clock.schedule_once(lambda dt: self._append_log(text))

    def _append_log(self, text):
        self.log_label.text += f">> {text}\n"
        self.scroll_view.scroll_y = 0

class TheGuardApp(App):
    def build(self):
        return GuardInterface()

if __name__ == '__main__':
    TheGuardApp().run()
