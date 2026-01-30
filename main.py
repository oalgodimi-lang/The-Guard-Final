from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from jnius import autoclass, cast
from android import api_version

# استدعاء أدوات النظام لفتح الإعدادات المحمية
PythonActivity = autoclass('org.kivy.android.PythonActivity')
Intent = autoclass('android.content.Intent')
Settings = autoclass('android.provider.Settings')
Uri = autoclass('android.net.Uri')
Environment = autoclass('android.os.Environment')

class GuardNode7(App):
    def build(self):
        self.title = "The Guard - Node 7 v1.1.9"
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=15)
        
        # الواجهة الأمامية
        self.header = Label(text="NODE 7: SOVEREIGN SHIELD v1.1.9", font_size='22sp', color=(0, 1, 1, 1))
        self.layout.add_widget(self.header)

        self.status_label = Label(text="[System Ready]\nEnter Cipher to Link Sovereign Permissions", halign='center')
        self.layout.add_widget(self.status_label)

        self.cipher_input = TextInput(hint_text="Enter Cipher", password=True, multiline=False, size_hint_y=None, height=120)
        self.layout.add_widget(self.cipher_input)

        self.btn = Button(text="ACTIVATE & LINK PERMISSIONS", size_hint_y=None, height=140, background_color=(0, 0.5, 0.8, 1))
        self.btn.bind(on_press=self.verify_and_open_settings)
        self.layout.add_widget(self.btn)

        self.log_label = Label(text="Log Status: Ready", font_size='12sp', color=(0.8, 0.8, 0.8, 1))
        self.layout.add_widget(self.log_label)

        return self.layout

    def verify_and_open_settings(self, instance):
        if self.cipher_input.text == "499712": # كلمة السر المتفق عليها
            self.log_label.text = "[✔] Cipher Accepted. Checking System Shield..."
            self.check_and_redirect()
        else:
            self.log_label.text = "[!] Invalid Cipher. Security Lock Active."

    def check_and_redirect(self):
        # التحقق إذا كان التطبيق يمتلك الإذن فعلياً
        if api_version >= 30:
            if not Environment.isExternalStorageManager():
                self.log_label.text = "[!] Access Denied. Redirecting to System Settings..."
                # فتح صفحة "الوصول إلى كل الملفات" فوراً
                self.open_all_files_access_settings()
            else:
                self.log_label.text = "[✔] Sovereign Access Already Active."
        else:
            self.log_label.text = "[i] Legacy API detected. Standard protection active."

    def open_all_files_access_settings(self):
        try:
            activity = PythonActivity.mActivity
            # كود "الانتزاع": يفتح صفحة الإعدادات الخاصة بتطبيقنا مباشرة
            intent = Intent(Settings.ACTION_MANAGE_APP_ALL_FILES_ACCESS_PERMISSION)
            uri = Uri.parse("package:" + activity.getPackageName())
            intent.setData(uri)
            activity.startActivity(intent)
        except Exception as e:
            self.log_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    GuardNode7().run()
