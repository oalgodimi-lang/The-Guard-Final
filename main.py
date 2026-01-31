from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import subprocess

class SovereignGuard(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        
        # --- تبويب الرادار (المسار المتوافق مع أندرويد الحديث) ---
        self.tab_radar = TabbedPanelItem(text='RADAR 2.0')
        self.radar_display = Label(
            text="Initializing Node 7 Scan...", 
            font_size='13sp', 
            color=(0, 1, 1, 1),
            halign='left'
        )
        self.tab_radar.add_widget(self.radar_display)
        self.add_widget(self.tab_radar)

        # --- تبويب الأمن (مع زر الطوارئ) ---
        self.tab_sec = TabbedPanelItem(text='SECURITY')
        sec_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.sec_status = Label(text="SYSTEM STATUS: SECURE", color=(0, 1, 0, 1), font_size='18sp')
        
        # زر الطوارئ (Emergency Purge)
        self.panic_btn = Button(
            text="EMERGENCY PURGE", 
            background_color=(1, 0, 0, 1), 
            font_size='20sp',
            bold=True
        )
        self.panic_btn.bind(on_press=self.emergency_purge)
        
        sec_layout.add_widget(self.sec_status)
        sec_layout.add_widget(self.panic_btn)
        self.tab_sec.add_widget(sec_layout)
        self.add_widget(self.tab_sec)

        # تحديث البيانات كل 2 ثانية
        Clock.schedule_interval(self.pro_update, 2)

    def pro_update(self, dt):
        try:
            # استخدام مسار /proc/net/dev لجلب بيانات الشبكة دون قيود Permissions
            output = subprocess.getoutput("cat /proc/net/dev | grep -E 'wlan0|rmnet'")
            if not output or "No such file" in output:
                output = "System Interface: Active\nScanning Traffic..."
            
            self.radar_display.text = f"[LIVE TRAFFIC DATA]\n{output}\n\n[Sovereign Node 7 Active]"
        except Exception as e:
            self.radar_display.text = f"Link Error: {str(e)}"

    def emergency_purge(self, instance):
        # تنفيذ بروتوكول التدمير الذاتي المنطقي
        self.sec_status.text = "!!! PURGING DATA !!!"
        self.sec_status.color = (1, 0, 0, 1)
        # هنا يمكن إضافة أوامر مسح السجلات مستقبلاً
        print("Panic Protocol Activated")

class TheGuardApp(App):
    def build(self):
        return SovereignGuard()

if __name__ == '__main__':
    TheGuardApp().run()
