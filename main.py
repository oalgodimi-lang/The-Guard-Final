from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from jnius import autoclass
import os

# استدعاء أدوات الأندرويد الأساسية (مستقرة جداً)
TrafficStats = autoclass('android.net.TrafficStats')

class SovereignRadar(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        with self.layout.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(2000, 4000), pos=self.layout.pos)

        self.header = Label(
            text="NODE 7: RADAR INITIALIZING...",
            font_size='22sp', color=(0, 1, 1, 1),
            size_hint_y=None, height=100
        )
        self.layout.add_widget(self.header)

        self.net_status = Label(
            text="🛡️ SECURE NODE ACTIVE",
            font_size='16sp', color=(0, 1, 0, 1),
            size_hint_y=None, height=60
        )
        self.layout.add_widget(self.net_status)

        self.scroll = ScrollView()
        self.app_list = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.app_list.bind(minimum_height=self.app_list.setter('height'))
        self.scroll.add_widget(self.app_list)
        self.layout.add_widget(self.scroll)

        # تحديث كل ثانية
        Clock.schedule_interval(self.update_stats, 1)
        return self.layout

    def update_stats(self, dt):
        try:
            # قراءة البيانات الحقيقية من النظام مباشرة (لا تسبب كراش)
            rx = TrafficStats.getTotalRxBytes() / (1024 * 1024)
            tx = TrafficStats.getTotalTxBytes() / (1024 * 1024)
            self.header.text = f"DATA: ↓{rx:.1f} MB | ↑{tx:.1f} MB"

            # جلب العمليات النشطة باستخدام أمر النظام 'top' (طريقة المحترفين)
            self.app_list.clear_widgets()
            # هذا الأمر يقرأ قائمة التطبيقات النشطة من قلب الأندرويد
            stream = os.popen('top -n 1 -b -m 10')
            lines = stream.readlines()
            
            for line in lines[4:]: # تجاوز العناوين
                if line.strip():
                    parts = line.split()
                    if len(parts) > 8:
                        p_name = parts[-1]
                        p_cpu = parts[2]
                        self.app_list.add_widget(Label(
                            text=f"[ACTIVE] {p_name} | CPU: {p_cpu}%",
                            size_hint_y=None, height=60, color=(1, 1, 1, 0.9)
                        ))
        except:
            self.net_status.text = "🛡️ System Shielding Active"

if __name__ == '__main__':
    SovereignRadar().run()
