from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import socket

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        self.status_label = Label(text='[b]NODE 7: READY[/b]', markup=True, size_hint_y=0.1)
        self.add_widget(self.status_label)
        
        self.scroll_view = ScrollView()
        self.log_label = Label(text=">> Waiting for Freedom Cipher...\n", size_hint_y=None, markup=True)
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)

    def activate_node(self, password):
        if password == "freedom":
            if self.send_socket_command("ACTIVATE_STEALTH"):
                self.update_log("[✔] GHOST MODE ACTIVE: DNS & SNI Obfuscated.")
                self.status_label.text = "[b]STATUS: INVISIBLE[/b]"
                self.status_label.color = (0, 1, 0, 1)

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
        Clock.schedule_once(lambda dt: setattr(self.log_label, 'text', self.log_label.text + f">> {msg}\n"))

class TheGuardApp(App):
    def build(self): return GuardInterface()

if __name__ == '__main__': TheGuardApp().run()
