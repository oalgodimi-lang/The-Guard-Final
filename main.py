from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import subprocess
import os

# محاولة استيراد مكتبة أندرويد لطلب الأذونات
try:
    from android.permissions import request_permissions, Permission
    PLATFORM_ANDROID = True
except ImportError:
    PLATFORM_ANDROID = False

class SovereignGuard(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        
        # طلب الأذونات فوراً إذا كنا على أندرويد
        if PLATFORM_ANDROID:
            request_permissions([Permission.MANAGE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])

        # تبويب الرادار
        self.tab_radar = TabbedPanelItem(text='RADAR 2.0')
        self.radar_display = Label(text="Initializing Scan...", color=(0, 1, 1, 1))
        self.tab_radar.add_widget(self.radar_display)
        self.add_widget(self.tab_radar)

        # تبويب الأمن السيادي
        self.tab_sec = TabbedPanelItem(text='SECURITY')
        sec_layout = BoxLayout(orientation='vertical', padding=20)
        self.sec_status = Label(text="SYSTEM STATUS: PROTECTED", color=(0, 1, 0, 1))
        panic_btn = Button(text="EMERGENCY PURGE", background_color=(1, 0, 0, 1), bold=True)
        panic_btn.bind(on_press=self.emergency_purge)
        sec_layout.add_widget(self.sec_status)
        sec_layout.add_widget(panic_btn)
        self.tab_sec.add_widget(sec_layout)
        self.add_widget(self.tab_sec)

        Clock.schedule_interval(self.pro_update, 2)

    def pro_update(self, dt):
        try:
            # قراءة مسار الشبكة المباشر
            output = subprocess.getoutput("cat /proc/net/dev | grep -E 'wlan|rmnet'")
            if "denied" in output or not output:
                self.radar_display.text = "[LOCKED]\nGrant 'All Files Access' in Settings"
            else:
                self.radar_display.text = f"[LIVE TRAFFIC]\n{output}"
        except:
            self.radar_display.text = "Searching for Signal..."

    def emergency_purge(self, instance):
        self.sec_status.text = "!!! DATA PURGED !!!"
        self.sec_status.color = (1, 0, 0, 1)

class TheGuardApp(App):
    def build(self):
        return SovereignGuard()

if __name__ == '__main__':
    TheGuardApp().run()
