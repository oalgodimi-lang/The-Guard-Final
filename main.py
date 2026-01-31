from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# إجبار لون الخلفية لضمان الرؤية
Window.clearcolor = (0.1, 0.1, 0.1, 1) 

class BridgeScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        layout.add_widget(Label(text="الوصول إلى العقدة السابعة", font_size='24sp', color=(1, 0.84, 0, 1)))
        
        self.password_input = TextInput(multiline=False, password=True, hint_text="كلمة السر", size_hint_y=None, height=100)
        layout.add_widget(self.password_input)
        
        btn = Button(text="فتح الجسر", size_hint_y=None, height=100, background_color=(1, 0.84, 0, 1))
        btn.bind(on_press=self.check_password)
        layout.add_widget(btn)
        
        self.error_label = Label(text="", color=(1, 0, 0, 1))
        layout.add_widget(self.error_label)
        self.add_widget(layout)

    def check_password(self, instance):
        if self.password_input.text == "freedom" or self.password_input.text == "499712":
            self.manager.current = 'control_center'
        else:
            self.error_label.text = "خطأ في المفتاح"

class ControlCenter(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(Label(text="CENTER CONTROL (ACTIVE)", color=(1, 0.84, 0, 1)))
        self.add_widget(layout)

class TheGuardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(BridgeScreen(name='bridge'))
        sm.add_widget(ControlCenter(name='control_center'))
        return sm

if __name__ == '__main__':
    TheGuardApp().run()
