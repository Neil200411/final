import webbrowser
from kivy.core.audio import SoundLoader
from Search_Engine import DictionaryScreen
from Loading_Screen import SplashScreen, CircularProgressBar
from Manager import screen_helper
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivy.uix.screenmanager import Screen, SlideTransition, FadeTransition, FallOutTransition, RiseInTransition, \
    SwapTransition

Window.size = (400, 600)

class FinalApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style= "Light"
        self.screen_manager = Builder.load_string(screen_helper)
        self.load_tables()  # Call this method after the screen manager is created
        self.click_sound = SoundLoader.load('Sounds/mouse-click-153941.mp3')
        self.click_sound2 = SoundLoader.load('Sounds/click.mp3')

        return self.screen_manager

    def toggle_theme(self, is_active):
        current_screen = self.root.get_screen('main')  # Replace with your actual screen name
        if 'theme_label' in current_screen.ids:
            if is_active:
                self.theme_cls.theme_style = "Dark"
                current_screen.ids.theme_label.text = "Dark"
                self.clearcolor = (0, 0, 0, 1)
            else:
                self.theme_cls.theme_style = "Light"
                current_screen.ids.theme_label.text = "Light"
                self.clearcolor = (1, 1, 1, 1)


    def play_click_sound(self):

        if self.click_sound:
            self.click_sound.play()

    def play_click_sound2(self):

        if self.click_sound2:
            self.click_sound2.play()

    def change_screen(self):
        self.root.current = "SplashScreen"

    def show_dictionary(self):
        self.root.current = 'dictionary'
        if self.theme_cls.theme_style == "Dark":
            clearcolor = (0, 0, 0, 1)  # Black for dark mode
        else:
            clearcolor = (1, 1, 1, 1)  # White for light mode

        self.root.transition = FallOutTransition(duration=0.3, clearcolor=clearcolor)

    def go_back_to_main(self):
        self.root.transition = SlideTransition(duration=0.5, direction='left')
        self.root.current = 'main'

    def show_table_screen(self, table_screen_name):
        if self.theme_cls.theme_style == "Dark":
            clearcolor = (0, 0, 0, 1)  # Black for dark mode
        else:
            clearcolor = (1, 1, 1, 1)  # White for light mode

        if table_screen_name == 'table':
            self.root.transition = RiseInTransition(duration=0.3, clearcolor=clearcolor)
        elif table_screen_name == 'table1':
            self.root.transition = RiseInTransition(duration=0.3, clearcolor=clearcolor)
        elif table_screen_name == 'table2':
            self.root.transition = RiseInTransition(duration=0.3, clearcolor=clearcolor)

        self.root.current = table_screen_name

        self.root.current = table_screen_name

    def load_tables(self):
        # Ensure the ScreenManager is initialized before accessing screens
        if self.screen_manager:
            table = MDDataTable(
                column_data=[("Abbreviation Words", dp(35)), ("Meanings", dp(45))],
                row_data=[("brb", "be right back"), ("idk", "I don't know"), ("lol", "laugh out loud")],
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                size_hint=(0.9, 0.8),
                height=200
            )
            table1 = MDDataTable(
                column_data=[("Terms", dp(20)), ("Meanings", dp(45)), ],
                row_data=[("python", "a high-level programming language"),
                          ("data", "facts and statistics collected together")],
                size_hint=(0.9, 0.8),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                height=200
            )
            table2 = MDDataTable(
                column_data=[("Slang Words", dp(20)), ("Meanings", dp(45))],
                row_data=[("yeet", "to throw something with force"), ("sus", "suspicious or suspect")],
                size_hint=(0.9, 0.8),
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                height=200
            )

            self.screen_manager.get_screen('table').ids.table_container.add_widget(table)
            self.screen_manager.get_screen('table1').ids.table1_container.add_widget(table1)
            self.screen_manager.get_screen('table2').ids.table2_container.add_widget(table2)

    def show_video(self):
        self.root.current = 'video'

    def open_link(self, url):
        # Open the link
        webbrowser.open(url)


DictionaryScreen()
SplashScreen()
CircularProgressBar()

class MainScreen(Screen):
    pass
class TableScreen(Screen):
    pass
class Table1Screen(Screen):
    pass
class Table2Screen(Screen):
    pass
class VideoScreen(Screen):
    pass

FinalApp().run()