from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import threading

# محاولة استيراد مكتبة OSC ومعالجة الخطأ إذا كانت ناقصة
try:
  #  from kivy.lib import osc
    OSC_AVAILABLE = True
except:
    OSC_AVAILABLE = False
    print("OSC not found, switching to offline mode")

class GuardInterface(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15, **kwargs)
        
        # حالة النظام
        self.status_label = Label(
            text='[b]SYSTEM STATUS: INITIALIZING...[/b]', 
            markup=True, color=(1, 1, 0, 1), font_size='22sp', size_hint_y=0.1
        )
        self.add_widget(self.status_label)

        # رادار السجلات (اللوحة الحية)
        self.scroll_view = ScrollView(size_hint=(1, 0.7))
        self.log_label = Label(
            text="[System Booting...]\n",
            markup=True, halign='left', valign='top',
            size_hint_y=None, font_size='14sp'
        )
        self.log_label.bind(texture_size=self.log_label.setter('size'))
        self.scroll_view.add_widget(self.log_label)
        self.add_widget(self.scroll_view)

        # زر فحص العتاد (لإبهار الداعم)
        self.stats_label = Label(
            text='HARDWARE TOKEN: SEARCHING...', 
            color=(0, 0.7, 1, 1), size_hint_y=0.1
        )
        self.add_widget(self.stats_label)

        # التحقق من توفر المكتبات وبدء الاستماع
        if OSC_AVAILABLE:
            self.start_listening()
        else:
            self.update_ui("CRITICAL ERROR: OSC Library missing in Buildozer requirements!")

    def start_listening(self):
        try:
           # osc.init()
          #  osc.bind(self.on_status_received, '/status')
            threading.Thread(target=self.listen_loop, daemon=True).start()
            self.status_label.text = '[b]SYSTEM STATUS: PROTECTED[/b]'
            self.status_label.color = (0, 1, 0, 1)
        except Exception as e:
            self.update_ui(f"OSC INIT ERROR: {str(e)}")

    def listen_loop(self):
        while True:
            try:
             #   osc.readQueue()
            except:
                pass

    def on_status_received(self, message, *args):
        try:
            new_log = message[2].decode('utf8')
            Clock.schedule_once(lambda dt: self.update_ui(new_log))
        except:
            pass

    def update_ui(self, text):
        self.log_label.text += f">> {text}\n"
        self.scroll_view.scroll_y = 0

class TheGuardApp(App):
    def build(self):
        return GuardInterface()

if __name__ == '__main__':
    try:
        TheGuardApp().run()
    except Exception as e:
        # هذا الجزء سيطبع الخطأ في الـ Logcat إذا انهار التطبيق
        print(f"FATAL APP ERROR: {str(e)}")
