from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
import socket

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=30, spacing=20, **kwargs)
        
        # عنوان النظام
        self.add_widget(Label(
            text='[b]NODE 7: SOVEREIGN SHIELD[/b]', 
            markup=True, font_size='24sp', size_hint_y=0.1, color=(0, 0.7, 1, 1)
        ))
        
        # حقل إدخال كلمة السر (الCipher)
        self.code_input = TextInput(
            hint_text='Enter Freedom Cipher...',
            password=True, multiline=False, size_hint_y=0.1,
            padding_y=(10, 10), halign='center'
        )
        self.add_widget(self.code_input)

        # زر التفعيل الأخضر (حقن البروتوكول)
        self.btn = Button(
            text='ACTIVATE STEALTH MODE', 
            size_hint_y=0.15, background_color=(0, 0.8, 0, 1),
            font_size='18sp', bold=True
        )
        self.btn.bind(on_press=lambda x: self.activate_node(self.code_input.text))
        self.add_widget(self.btn)

        # لوحة السجلات الحية
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
        """إرسال أمر التفعيل للنواة عبر المقابس"""
        if password == "freedom":
            self.update_log("[!] Cipher Accepted. Connecting to Core...")
            if self.send_socket_command("ACTIVATE_STEALTH"):
                self.update_log("[✔] GHOST MODE: DNS Encrypted & Identity Masked.")
                self.btn.text = "SHIELD ACTIVE"
                self.btn.background_color = (0, 0.5, 1, 1)
            else:
                self.update_log("[X] Communication Error: Core is unresponsive.")
        else:
            self.update_log("[X] Access Denied: Invalid Cipher.")

    def send_socket_command(self, cmd):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(2)
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
