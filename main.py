from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import random

# إعداد خلفية النظام السوداء لتعزيز الهيبة الرقمية
Window.clearcolor = (0, 0, 0, 1)

Builder.load_string('''
<Manager>:
    ShowcaseLogin:
    Dashboard:
    MonitorRoom:
    ObfuscatorRoom:
    AnalystRoom:

<ShowcaseLogin>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: 50
        spacing: 20
        Label:
            text: 'THE GUARD - NODE 7'
            font_size: '28sp'
            color: 0, 1, 0, 1
            bold: True
        Label:
            text: 'نظام الحارس - العقدة السابعة'
            font_size: '16sp'
            color: 0, 0.6, 0, 1
        TextInput:
            id: code_input
            hint_text: 'Sovereignty Code'
            password: True
            multiline: False
            size_hint_y: None
            height: '50dp'
            background_color: 0.1, 0.1, 0.1, 1
            foreground_color: 0, 1, 0, 1
        Button:
            text: 'INITIALIZE SYSTEM'
            size_hint_y: None
            height: '60dp'
            background_color: 0, 0.4, 0, 1
            on_press: root.verify()

<Dashboard>:
    name: 'dashboard'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        Label:
            text: 'CONTROL CENTER / مركز التحكم'
            color: 0, 1, 0, 1
            font_size: '22sp'
        Button:
            text: '📊 DATA MONITORING (المراقبة)'
            background_color: 0.1, 0.1, 0.1, 1
            on_press: root.manager.current = 'monitor'
        Button:
            text: '📡 NETWORK OBFUSCATOR (التشويش)'
            background_color: 0.1, 0.1, 0.1, 1
            on_press: root.manager.current = 'obfuscator'
        Button:
            text: '🧠 SECURITY ANALYST (التحليل)'
            background_color: 0.1, 0.1, 0.1, 1
            on_press: root.manager.current = 'analyst'
        Button:
            text: 'LOGOUT / خروج'
            size_hint_y: None
            height: '40dp'
            background_color: 0.5, 0, 0, 1
            on_press: root.manager.current = 'login'

<MonitorRoom>:
    name: 'monitor'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            id: traffic_label
            text: 'SCANNING TRAFFIC...'
            font_size: '20sp'
            color: 0, 1, 0, 1
        Label:
            id: alert_label
            text: 'STATUS: SECURE'
            bold: True
        Label:
            id: countdown_label
            text: ''
            font_size: '60sp'
            bold: True
            color: 1, 0, 0, 1
        Button:
            text: 'BACK TO COMMAND'
            size_hint_y: None
            height: '50dp'
            on_press: root.back_to_dash()

<ObfuscatorRoom>:
    name: 'obfuscator'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        Label:
            text: 'NETWORK OBFUSCATION'
            color: 0, 0.6, 1, 1
            font_size: '22sp'
        Label:
            id: packet_label
            text: 'Sending Dummy Data...'
            font_size: '12sp'
            color: 0.5, 0.5, 0.5, 1
        Button:
            text: 'STOP BRIDGE'
            size_hint_y: None
            height: '50dp'
            on_press: root.manager.current = 'dashboard'

<AnalystRoom>:
    name: 'analyst'
    BoxLayout:
        orientation: 'vertical'
        padding: 20
        spacing: 15
        Label:
            id: analyst_text
            text: 'Security Expert Waiting for Logs...'
            halign: 'center'
            font_size: '18sp'
        Button:
            text: 'EXPLAIN SECURITY EVENTS'
            size_hint_y: None
            height: '60dp'
            background_color: 0, 0.3, 0.6, 1
            on_press: root.explain()
        Button:
            text: 'BACK'
            on_press: root.manager.current = 'dashboard'
''')

class ShowcaseLogin(Screen):
    def verify(self):
        # التحقق من رمز السيادة الخاص بك [cite: 2026-01-27]
        if self.ids.code_input.text == "freedom 499712":
            self.manager.current = 'dashboard'

class Dashboard(Screen): pass

class MonitorRoom(Screen):
    def on_enter(self):
        self.destruction_counter = 10
        self.is_critical = False
        self.event = Clock.schedule_interval(self.update_traffic, 1)
    
    def update_traffic(self, dt):
        out_val = random.randint(5, 120)
        self.ids.traffic_label.text = f"OUTGOING: {out_val} kb/s"
        
        # إذا اكتشف النظام حركة بيانات مريبة (أعلى من 90) يبدأ التدمير الذاتي للردع [cite: 2026-01-24]
        if out_val > 90 and not self.is_critical:
            self.is_critical = True
            self.ids.alert_label.text = "🚨 INTRUDER DETECTED - DATA LEAK!"
            self.ids.alert_label.color = (1, 0, 0, 1)
            Clock.schedule_interval(self.start_self_destruct, 1)
        
        if not self.is_critical:
            self.ids.alert_label.text = "STATUS: SECURE"
            self.ids.alert_label.color = (0, 1, 0, 1)

    def start_self_destruct(self, dt):
        if self.destruction_counter > 0:
            # وميض درامي (أحمر/أسود) لإرهاب المتسلل وإبهار الداعم
            Window.clearcolor = (0.5, 0, 0, 1) if self.destruction_counter % 2 == 0 else (0, 0, 0, 1)
            self.ids.countdown_label.text = str(self.destruction_counter)
            self.destruction_counter -= 1
        else:
            Window.clearcolor = (0, 0, 0, 1)
            self.ids.traffic_label.text = "SYSTEM PURGED"
            self.ids.alert_label.text = "YOU HAVE NOTHING HERE, INTRUDER."
            self.ids.countdown_label.text = "OFFLINE"
            return False

    def back_to_dash(self):
        Clock.unschedule(self.event)
        Window.clearcolor = (0, 0, 0, 1)
        self.manager.current = 'dashboard'

class ObfuscatorRoom(Screen):
    def on_enter(self):
        self.ob_event = Clock.schedule_interval(self.send_dummy, 0.2)
    def send_dummy(self, dt):
        # توليد بيانات وهمية لإخفاء نشاط التصفح الحقيقي [cite: 2026-01-24]
        hex_data = "".join(random.choice("0123456789ABCDEF") for _ in range(32))
        self.ids.packet_label.text = f"OBFUSCATING: 0x{hex_data} -> LOCAL NET"
    def on_leave(self):
        Clock.unschedule(self.ob_event)

class AnalystRoom(Screen):
    def explain(self):
        # محاور التحليل المعالجة البرمجية [cite: 2026-01-24]
        explanations = [
            "تم حجب محاولة دخول غير مصرح بها للشبكة المحلية.",
            "بروتوكول التشويش النشط يمنع المتسلل من معرفة نوع تصفحك.",
            "المعالجة: تم تحويل كافة البيانات الخارجة إلى صيغة Hex مشفرة.",
            "النظام يكتشف محاولة سحب بيانات.. تم تفعيل حواجز العقدة السابعة."
        ]
        self.ids.analyst_text.text = random.choice(explanations)

class Manager(ScreenManager): pass

class GuardApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    GuardApp().run()
