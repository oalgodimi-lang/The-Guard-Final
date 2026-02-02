from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.core.text import LabelBase
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
# استدعاء مكتبة الصلاحيات (مهم جداً للحقن)
from android.permissions import request_permissions, Permission

Window.clearcolor = (0, 0, 0, 1)

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        self.node7_logo = Label(
            text='[color=#00FF00]Node 7[/color]\n[size=20]The Sovereign Shield[/size]',
            markup=True, font_size='48sp', halign='center', size_hint_y=0.4
        )
        self.layout.add_widget(self.node7_logo)
        
        self.password_input = TextInput(
            hint_text='Password for Freedom', password=True, multiline=False,
            size_hint_y=0.1, background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1), halign='center'
        )
        self.layout.add_widget(self.password_input)

        self.status_label = Label(text='', markup=True, size_hint_y=0.1)
        self.layout.add_widget(self.status_label)

        login_button = Button(text='Enter', size_hint_y=0.1, background_color=(0, 0.5, 0, 1))
        login_button.bind(on_press=self.check_password)
        self.layout.add_widget(login_button)
        self.add_widget(self.layout)

    def check_password(self, instance):
        if self.password_input.text == 'freedom':
            self.manager.current = 'main_app'
        else:
            self.status_label.text = '[color=#FF0000]Incorrect password.[/color]'

class MainAppScreen(Screen):
    # سيتم عرض الغرف الثلاث كما في الكود الأصلي
    pass

# إضافة بقية الشاشات (AppVault, GhostRoom, SentinelRoom) بنفس المنطق السابق

class SovereignShieldApp(App):
    def build(self):
        # طلب الصلاحيات فوراً عند تشغيل التطبيق في أندرويد
        try:
            request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        except:
            pass # لتجنب الخطأ عند التشغيل على الكمبيوتر للتجربة

        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        # هنا يتم إضافة بقية الشاشات...
        return self.sm

if __name__ == '__main__':
    SovereignShieldApp().run()
