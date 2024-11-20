from kivymd.app import MDApp
from kivy.lang import Builder
KV = '''
MDScreen:
    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDBoxLayout:
            orientation: 'horizontal'
            spacing: dp(10)
            size_hint_y: None
            height: dp(48)
            pos_hint: {"center_x": 0.5}

            MDLabel:
                id: theme_label
                text: "Light"  # Initial text
                halign: "left"
                valign: "center"

            MDSwitch:
                on_active: app.toggle_theme(self.active)
'''

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"  # Initial theme style
        return Builder.load_string(KV)

    def toggle_theme(self, is_active):
        if is_active:
            self.theme_cls.theme_style = "Dark"
            self.root.ids.theme_label.text = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
            self.root.ids.theme_label.text = "Light"

if __name__ == "__main__":
    MyApp().run()
