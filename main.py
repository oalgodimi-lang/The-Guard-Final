from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
# استدعاء مكتبة الصلاحيات (الحقن التدريجي)
from android.permissions import request_permissions, Permission

# الأكواد الأصلية التي أرفقتها مسبقاً (LoginScreen, MainAppScreen, إلخ...)
# ... (سأضع لك فقط الجزء الذي يحتاج تعديل في الأسفل لسهولة اللصق)

class SovereignShieldApp(App):
    def build(self):
        # طلب الصلاحيات فور تشغيل التطبيق
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        
        self.sm = ScreenManager()
        # إضافة الشاشات (كما في الكود الأصلي)
        return self.sm

if __name__ == '__main__':
    SovereignShieldApp().run()
