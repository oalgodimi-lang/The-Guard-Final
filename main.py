
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.animation import Animation

# Set window to dark theme
Window.clearcolor = (0, 0, 0, 1) # Black background

class LoginScreen(Screen):
    password_input = ObjectProperty(None)
    status_label = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        # Node 7 Logo Placeholder
        self.node7_logo = Label(
            text='[color=#00FF00]العقدة 7[/color]\n[size=20]الدرع السيادي[/size]',
            markup=True,
            font_size='48sp',
            halign='center',
            valign='middle',
            size_hint_y=0.4
        )
        self.layout.add_widget(self.node7_logo)

        # Add pulsing animation to the logo
        self.animate_logo_pulse()

        # Password Input
        self.password_input = TextInput(
            hint_text='كلمة السر للحرية',
            password=True,
            multiline=False,
            size_hint_y=0.1,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(0, 1, 0, 1),
            font_size='24sp',
            padding_y=[15, 0], # Fixed padding for now to avoid error
            halign='center'
        )
        self.layout.add_widget(self.password_input)

        # Status Label
        self.status_label = Label(
            text='',
            markup=True,
            color=(1, 0, 0, 1), # Red for error
            font_size='18sp',
            size_hint_y=0.1
        )
        self.layout.add_widget(self.status_label)

        # Login Button
        login_button = Button(
            text='ادخل',
            size_hint_y=0.1,
            background_color=(0, 0.5, 0, 1),
            font_size='24sp'
        )
        login_button.bind(on_press=self.check_password)
        self.layout.add_widget(login_button)

        self.add_widget(self.layout)

    def check_password(self, instance):
        if self.password_input.text == 'freedom':
            self.manager.current = 'main_app'
        else:
            self.status_label.text = '[color=#FF0000]كلمة السر خاطئة. حاول مرة أخرى.[/color]'
            self.animate_shake(self.password_input)

    def animate_shake(self, widget):
        original_x = widget.x
        anim = Animation(x=original_x - 10, duration=0.05) + \
               Animation(x=original_x + 10, duration=0.05) + \
               Animation(x=original_x - 10, duration=0.05) + \
               Animation(x=original_x + 10, duration=0.05) + \
               Animation(x=original_x, duration=0.05)
        anim.start(widget)

    def animate_logo_pulse(self):
        # Animation to make the logo pulse by changing its opacity
        anim = Animation(opacity=0.5, duration=1) + \
               Animation(opacity=1.0, duration=1)
        anim.repeat = True
        anim.start(self.node7_logo)

class MainAppScreen(Screen):
    def __init__(self, **kwargs):
        super(MainAppScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)

        self.title_label = Label(
            text='[color=#00FF00]مركز القيادة[/color]',
            markup=True,
            font_size='36sp',
            halign='center',
            valign='middle',
            size_hint_y=0.2
        )
        self.layout.add_widget(self.title_label)

        # Placeholder for the three rooms
        rooms_layout = BoxLayout(orientation='vertical', spacing=15, size_hint_y=0.7)

        # Room 1: Application Monitoring
        room1_button = Button(
            text='[color=#00FF00]غرفة مراقبة التطبيقات[/color]',
            markup=True,
            background_color=(0.1, 0.1, 0.1, 1),
            font_size='28sp',
            size_hint_y=0.33
        )
        room1_button.bind(on_press=self.open_app_monitoring_room)
        rooms_layout.add_widget(room1_button)

        # Room 2: Network Monitoring and Jamming
        room2_button = Button(
            text='[color=#00FF00]غرفة مراقبة الشبكات والتشويش[/color]',
            markup=True,
            background_color=(0.1, 0.1, 0.1, 1),
            font_size='28sp',
            size_hint_y=0.33
        )
        room2_button.bind(on_press=self.open_network_monitoring_room)
        rooms_layout.add_widget(room2_button)

        # Room 3: Intrusion Monitoring
        room3_button = Button(
            text='[color=#00FF00]غرفة مراقبة محاولة أي اختراق أو تجسس[/color]',
            markup=True,
            background_color=(0.1, 0.1, 0.1, 1),
            font_size='28sp',
            size_hint_y=0.33
        )
        room3_button.bind(on_press=self.open_intrusion_monitoring_room)
        rooms_layout.add_widget(room3_button)

        self.layout.add_widget(rooms_layout)

        self.add_widget(self.layout)

    def open_app_monitoring_room(self, instance):
        print('فتح غرفة مراقبة التطبيقات (هيكل صامت)')
        # Placeholder for future implementation
        # self.manager.current = 'app_monitoring_screen'

    def open_network_monitoring_room(self, instance):
        print('فتح غرفة مراقبة الشبكات والتشويش (هيكل صامت)')
        # Placeholder for future implementation
        # self.manager.current = 'network_monitoring_screen'

    def open_intrusion_monitoring_room(self, instance):
        print('فتح غرفة مراقبة الاختراق (هيكل صامت)')
        # Placeholder for future implementation
        # self.manager.current = 'intrusion_monitoring_screen'

class SovereignShieldApp(App):
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(MainAppScreen(name='main_app'))
        return self.sm

if __name__ == '__main__':
    SovereignShieldApp().run()
