from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import subprocess

class SovereignGuard(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.background_color = (0, 0, 0, 1) # خلفية سوداء احترافية

        # --- Tab: Radar (The Eye) ---
        self.radar_tab = TabbedPanelItem(text='RADAR')
        self.radar_scroll = ScrollView()
        self.radar_label = Label(text="Awaiting Permissions...", font_size='14sp', color=(0, 1, 1, 1), halign='left')
        self.radar_scroll.add_widget(self.radar_label)
        self.radar_tab.add_widget(self.radar_scroll)
        self.add_widget(self.radar_tab)

        # --- Tab: Security (Node 7) ---
        self.sec_tab = TabbedPanelItem(text='SECURITY')
        self.sec_label = Label(text="[STATUS] SECURE NODE ACTIVE", color=(0, 1, 0, 1))
        self.sec_tab.add_widget(self.sec_label)
        self.add_widget(self.sec_tab)

        # بدء التحديث بعد 2 ثانية لضمان استقرار التطبيق
        Clock.schedule_once(self.start_monitoring, 2)

    def start_monitoring(self, dt):
        Clock.schedule_interval(self.update_stats, 2)

    def update_stats(self, dt):
        try:
            # قراءة حذرة لملف الشبكة
            cmd = "cat /proc/net/xt_qtaguid/stats | head -n 10"
            output = subprocess.getoutput(cmd)
            if "Permission denied" in output:
                self.radar_label.text = "[!] Grant 'All Files Access' in Settings"
            else:
                self.radar_label.text = f"[LIVE DATA]\n{output}"
        except Exception as e:
            self.radar_label.text = f"Link Error: {str(e)}"

class TheGuardApp(App):
    def build(self):
        return SovereignGuard()

if __name__ == '__main__':
    TheGuardApp().run()
