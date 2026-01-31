from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from android.permissions import request_permissions, Permission
import os

class GuardSlim(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text="[ Node 7 - Waiting for Sovereign Access ]", markup=True)
        self.layout.add_widget(self.label)
        # طلب الصلاحيات بتكتيك تدريجي لتجنب الانهيار
        Clock.schedule_once(self.ask_permissions, 1)
        return self.layout

    def ask_permissions(self, dt):
        # نطلب الصلاحيات الأساسية أولاً لضمان الإقلاع
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        self.label.text = " [cite: 2026-01-10] freedom \nRadar Active: Monitoring wlan0..."

if __name__ == '__main__':
    GuardSlim().run()
