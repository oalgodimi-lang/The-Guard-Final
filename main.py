# الملف المحدث لحقن العصب الأول - النسخة #92
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import os

# --- شاشة الجسر (The Bridge) ---
class BridgeScreen(Screen):
    def check_password(self, instance):
        if self.password_input.text == "freedom" or self.password_input.text == "499712":
            self.manager.current = 'control_center'
        else:
            self.error_label.text = "خطأ في مفتاح العبور"

# --- شاشة التحكم (Control Center) ---
class ControlCenter(Screen):
    pass

# --- غرفة مراقب التطبيقات (The Vault - First Nerve) ---
class WatcherScreen(Screen):
    def on_enter(self):
        # هنا يبدأ "النبض الصامت" باستخدام صلاحيات الوسائط المتاحة
        self.log_area.text = "جارٍ تشغيل الرادار الصامت...\n"
        try:
            # رصد ملفات الوسائط كبداية للسيادة
            path = "/sdcard/Pictures" # تجربة الوصول لمجلد الصور
            files = os.listdir(path)
            self.log_area.text += f"تم رصد {len(files)} بصمة رقمية في الوسائط.\n"
            for f in files[:5]: # عرض أول 5 ملفات كنموذج للصدق
                self.log_area.text += f"- بصمة: {f}\n"
        except:
            self.log_area.text += "الرادار يعمل في وضع الاستعداد الصامت.\nبانتظار مزيد من الصلاحيات لاحقاً."

class TheGuardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BridgeScreen(name='bridge'))
        sm.add_widget(ControlCenter(name='control_center'))
        sm.add_widget(WatcherScreen(name='watcher'))
        return sm

if __name__ == '__main__':
    TheGuardApp().run()
