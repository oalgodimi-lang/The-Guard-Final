from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.lib import osc
import threading

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # عنوان النظام الاحترافي
        self.add_widget(Label(
            text='[b]SYSTEM STATUS: PROTECTED[/b]', 
            markup=True, color=(0, 1, 0, 1), font_size='24sp', size_hint_y=0.1
        ))

        # حاوية السجلات (الرادار الميداني)
        self.scroll_view = ScrollView(size_hint=(1, 0.7), bar_width=10)
        self.log_label = Label(
            text="[Initializing Field Radar...]\n",
            markup=True, halign='left', valign='top',
            size_hint_y=None, font_name='Roboto'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)

        # عداد البيانات المشفرة
        self.stats_label = Label(
            text='Encrypted Stream: 0.0 KB/s', 
            color=(0, 0.7, 1, 1), size_hint_y=0.1
        )
        self.add_widget(self.stats_label)

        # بدء استقبال البيانات من الـ Service
        self.start_listening()

    def start_listening(self):
        osc.init()
        osc.bind(self.on_status_received, '/status')
        threading.Thread(target=self.listen_loop, daemon=True).start()

    def listen_loop(self):
        while True:
            osc.readQueue()

    def on_status_received(self, message, *args):
        # تحديث السجل فور وصول رسالة من الحارس
        new_log = message[2].decode('utf8')
        Clock.schedule_once(lambda dt: self.update_ui(new_log))

    def update_ui(self, text):
        self.log_label.text += f">> {text}\n"
        # التمرير التلقائي لأسفل لمتابعة أحدث العمليات
        self.scroll_view.scroll_y = 0

class TheGuardApp(App):
    def build(self):
        return GuardInterface()

if __name__ == '__main__':
    TheGuardApp().run()
