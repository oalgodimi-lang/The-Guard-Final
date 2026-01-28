from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# إعدادات الواجهة (لون خلفية أسود للتمويه)
Window.clearcolor = (0, 0, 0, 1)

class SovereignShieldUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 10

        # شعار العقدة 7 (نصي)
        self.add_widget(Label(
            text="[🛡️ Sovereign Shield v1.0]",
            font_size='24sp',
            color=(0, 1, 0, 1), # لون أخضر Termux
            markup=True
        ))

        self.add_widget(Label(
            text="Node 7 - Sovereignty Protocol Active",
            font_size='14sp',
            color=(0, 0.8, 0, 1)
        ))

        # حقل إدخال الشفرة
        self.code_input = TextInput(
            hint_text="Enter Sovereignty Code...",
            password=True,
            multiline=False,
            size_hint_y=None,
            height='50dp',
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1)
        )
        self.add_widget(self.code_input)

        # زر التحقق
        self.verify_btn = Button(
            text="VERIFY ACCESS",
            size_hint_y=None,
            height='50dp',
            background_color=(0, 0.5, 0, 1),
            color=(1, 1, 1, 1)
        )
        self.verify_btn.bind(on_press=self.check_code)
        self.add_widget(self.verify_btn)

        # منطقة الرسائل
        self.status_label = Label(text="Waiting for authorization...", color=(0.5, 0.5, 0.5, 1))
        self.add_widget(self.status_label)

    def check_code(self, instance):
        if self.code_input.text == "freedom":
            self.status_label.text = "[✔] ACCESS GRANTED. Welcome, Founder."
            self.status_label.color = (0, 1, 0, 1)
            # هنا سيتم لاحقاً استدعاء وظائف الحماية الحقيقية
        else:
            self.status_label.text = "[✘] INVALID CODE. Security Alert Triggered."
            self.status_label.color = (1, 0, 0, 1)
            self.code_input.text = ""

class SovereignApp(App):
    def build(self):
        self.title = "Sovereign Shield"
        return SovereignShieldUI()

if __name__ == "__main__":
    SovereignApp().run()
