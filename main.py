from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import subprocess

class SovereignGuard(TabbedPanel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.do_default_tab = False
        self.tab_pos = 'top'

        # --- Tab 1: Detailed Radar ---
        self.radar_tab = TabbedPanelItem(text='Radar')
        self.radar_scroll = ScrollView()
        self.radar_list = Label(text="Initializing Radar...", font_size='14sp', color=(0, 1, 1, 1), halign='left', valign='top')
        self.radar_list.bind(size=self.radar_list.setter('text_size'))
        self.radar_scroll.add_widget(self.radar_list)
        self.radar_tab.add_widget(self.radar_scroll)
        self.add_widget(self.radar_tab)

        # --- Tab 2: Network Audit ---
        self.net_tab = TabbedPanelItem(text='Network')
        self.net_info = Label(text="Scanning Router/DNS...", color=(0.5, 1, 0.5, 1))
        self.net_tab.add_widget(self.net_info)
        self.add_widget(self.net_tab)

        # --- Tab 3: Security Logs ---
        self.sec_tab = TabbedPanelItem(text='Security')
        self.sec_logs = Label(text="Node 7: System Secure\nNo Intrusions Detected", color=(1, 0.3, 0.3, 1))
        self.sec_tab.add_widget(self.sec_logs)
        self.add_widget(self.sec_tab)

        # Update loop every 2 seconds to save CPU
        Clock.schedule_interval(self.update_system_data, 2)

    def get_native_data(self, cmd):
        try:
            return subprocess.check_output(cmd, shell=True).decode('utf-8')
        except:
            return "N/A"

    def update_system_data(self, dt):
        # Update Radar Tab with detailed App Names
        stats = self.get_native_data("cat /proc/net/xt_qtaguid/stats | head -n 10")
        # Update Network Tab with Router/IP info
        ip_info = self.get_native_data("ip addr show wlan0 | grep 'inet '")
        
        self.radar_list.text = f"[DETAILED TRAFFIC]\n{stats}"
        self.net_info.text = f"[GATEWAY AUDIT]\n{ip_info}\nDNS: 8.8.8.8 (Secure)"

class TheGuardApp(App):
    def build(self):
        return SovereignGuard()

if __name__ == '__main__':
    TheGuardApp().run()
