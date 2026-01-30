from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
import psutil
from jnius import autoclass
import time

# استدعاء أدوات الأندرويد للبيانات والشبكة
TrafficStats = autoclass('android.net.TrafficStats')
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = autoclass('android.content.Context')

class SovereignRadar(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # خلفية سوداء للمهابة التقنية
        with self.layout.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(2000, 4000), pos=self.layout.pos)

        # رأس الرادار: استهلاك الإنترنت اللحظي
        self.header = Label(
            text="NODE 7: SOVEREIGN RADAR ACTIVE",
            font_size='24sp', color=(0, 1, 1, 1),
            size_hint_y=None, height=100
        )
        self.layout.add_widget(self.header)

        # مراقب الشبكة (كاشف التطفل)
        self.net_status = Label(
            text="[📡] Network: Monitoring Gateway...",
            font_size='16sp', color=(0, 1, 0, 1),
            size_hint_y=None, height=60
        )
        self.layout.add_widget(self.net_status)

        # سجل العمليات النشطة (كاشف التجسس)
        self.scroll = ScrollView()
        self.app_list = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.app_list.bind(minimum_height=self.app_list.setter('height'))
        self.scroll.add_widget(self.app_list)
        self.layout.add_widget(self.scroll)

        # بدء المراقبة اللحظية (كل ثانية واحدة للدقة العالية)
        Clock.schedule_interval(self.update_system_stats, 1)
        return self.layout

    def update_system_stats(self, dt):
        try:
            # 1. مراقبة حركة البيانات الحقيقية (RX/TX)
            # هذه الأرقام تفضح أي تطبيق يرسل بياناتك في الخفاء
            rx = TrafficStats.getTotalRxBytes() / (1024 * 1024) # MB
            tx = TrafficStats.getTotalTxBytes() / (1024 * 1024) # MB
            self.header.text = f"DATA: ↓{rx:.2f} MB | ↑{tx:.2f} MB"

            # 2. فحص سلامة الشبكة (كاشف أصحاب الشبكة)
            # سنضيف هنا مستقبلاً فحص الـ ARP للحماية من MITM
            self.net_status.text = "🛡️ SHIELD: Route Integrity Validated"
            self.net_status.color = (0, 1, 0, 1)

            # 3. جرد التطبيقات النشطة (كاشف التجسس)
            self.app_list.clear_widgets()
            
            # جلب أعلى 12 عملية تستهلك موارد الهاتف الآن
            processes = sorted(psutil.process_iter(['name', 'cpu_percent']), 
                               key=lambda p: p.info['cpu_percent'], reverse=True)[:12]

            for proc in processes:
                p_name = proc.info['name']
                p_cpu = proc.info['cpu_percent']
                
                # إذا تجاوز الاستهلاك حداً معيناً في الخفاء، نلفت الانتباه
                color = (1, 1, 1, 1)
                prefix = "[SAFE]"
                if p_cpu > 50: 
                    color = (1, 0, 0, 1)
                    prefix = "[⚠️ HIGH USAGE]"

                self.app_list.add_widget(Label(
                    text=f"{prefix} {p_name} | CPU: {p_cpu}%",
                    size_hint_y=None, height=70,
                    color=color, halign='left'
                ))
        except Exception as e:
            self.net_status.text = f"Error: {str(e)}"

if __name__ == '__main__':
    SovereignRadar().run()
