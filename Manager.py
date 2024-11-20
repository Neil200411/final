screen_helper = """
ScreenManager:
    SplashScreen:
    MainScreen:
    DictionaryScreen:
    TableScreen:
    Table1Screen:
    Table2Screen:
    VideoScreen:


<SplashScreen>:
    name: "SplashScreen"
    on_enter: self.ids.progress.start()
    MDFloatLayout:
        md_bg_color: 1, 0, 100/255, .1
        
        MDLabel:
            text: "App Name"
            font_size: "55sp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.8}
            halign: "center"
        
        Image:
            source: "Images/bite.gif"
            allow_stretch: True
            anim_delay: 0
            anim_reset: True
            size_hint: None, None
            size: 70, 70
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            halign: "center"
            
        CircularProgressBar:
            size_hint: None, None
            size: 200, 200
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            value: 100
        
        
<CircularProgressBar>
    canvas.before:
        Color:
            rgba: root.bar_color + [0.3]
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, 360)

    canvas.after:
        Color:
            rgb: root.bar_color
        Line:
            width: root.bar_width
            ellipse: (self.x, self.y, self.width, self.height, 0, root.set_value * 3.6)

    MDLabel:
        text: root.text
        font_size: "46sp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        halign: "center"
        color: root.bar_color



<MainScreen>:
    name: 'main'
    MDNavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: 'Final App'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("toggle")]]
                    MDLabel:
                        text: 'GUIDES:'
                        halign: 'center'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        size_hint_y: None
                        height: "48dp"
                    MDLabel:
                        text: 'Step1'
                        halign: 'center'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: 'Step2'
                        halign: 'center'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    MDLabel:
                        text: 'Step3'
                        halign: 'center'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        
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
        MDNavigationDrawer:
            id: nav_drawer
            BoxLayout:
                orientation: 'vertical'
                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text: 'Dictionary'
                            on_release: 
                                app.show_dictionary()
                                app.play_click_sound2()
                            IconLeftWidget:
                                icon: 'book-open-variant'
                        OneLineIconListItem:
                            text: 'Videos'
                            on_release: 
                                app.show_video()
                                app.play_click_sound2()
                            IconLeftWidget:
                                icon: 'video-outline'
                        OneLineIconListItem:
                            text: 'Quizzes'
                            IconLeftWidget:
                                icon: 'form-select'
                        OneLineIconListItem:
                            text: 'Articles'
                            IconLeftWidget:
                                icon: 'newspaper'
                        OneLineIconListItem:
                            text: 'About'
                            IconLeftWidget:
                                icon: 'information'
<DictionaryScreen>:
    name: 'dictionary'
    FloatLayout:
        MDTextField:
            id: search_input
            hint_text: "Enter abbreviation to search"
            size_hint: 0.6, None
            height: dp(40)
            pos_hint: {'center_x': 0.5, 'top': 0.88}

        MDFillRoundFlatButton:
            text: "Search"
            size_hint: None, None
            size: dp(150), dp(40)
            pos_hint: {'center_x': 0.8, 'top': 0.85}
            on_release: root.search_term(search_input)

        Label:
            text: "Dictionary Content Here"
            size_hint: None, None
            size: Window.width, Window.height * 0.7
            pos_hint: {'center_x': 0.5, 'top': 0.5}
            
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Dictionaries'
            left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
        Widget:

    BoxLayout:
        orientation: 'vertical'
        spacing: 10
        padding: 20
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}       

        MDRaisedButton:
            text: "View Abbreviation Table"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release:
                app.show_table_screen('table')
                app.play_click_sound()

        MDRaisedButton:
            text: "View Terms Table"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}            
            on_release:
                app.show_table_screen('table1')
                app.play_click_sound()
            

        MDRaisedButton:
            text: "View Slang Words Table"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}            
            on_release:
                app.show_table_screen('table2')
                app.play_click_sound()


<TableScreen>:
    name: 'table'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Abbreviation Table'
            left_action_items: [["arrow-left", lambda x: app.show_dictionary()]]
        MDBoxLayout:
            id: table_container
            padding: 10

<Table1Screen>:
    name: 'table1'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Terms Table'
            left_action_items: [["arrow-left", lambda x: app.show_dictionary()]]
        MDBoxLayout:
            id: table1_container
            padding: 10

<Table2Screen>:
    name: 'table2'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Slang Words Table'
            left_action_items: [["arrow-left", lambda x: app.show_dictionary()]]
        MDBoxLayout:
            id: table2_container
            padding: 10

<VideoScreen>:
    name: 'video'
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'Videos'
            left_action_items: [["arrow-left", lambda x: app.go_back_to_main()]]
        Widget:

    BoxLayout:
        orientation: 'vertical'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        spacing: 10
        padding: 20



        MDLabel:
            text: "Here are some helpful videos"
            halign: "center"
            size_hint_y: None
            height: "20dp"

        Image:
            source: 'Images/Arrowdown.png'
            size_hint_y: None
            height: "300"
            halign: "center"
            size: '30dp', '30dp'

        OneLineIconListItem:
            text: "[color=0000FF]    Being Safe on the Internet[/color]"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            markup: True  # Enables the use of markup
            halign: "center"
            on_release: app.open_link("https://youtu.be/HxySrSbSY7o?feature=shared")
            ImageLeftWidget:
                source: 'Images/img.png'

        OneLineIconListItem:
            text: "[color=0000FF]    11 Internet Safety Tips for Your Online Security[/color]"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            markup: True  # Enables the use of markup
            halign: "center"
            on_release: app.open_link("https://www.youtube.com/watch?v=aO858HyFbKI")
            ImageLeftWidget:
                source: 'Images/img_1.png'

        OneLineIconListItem:
            text: "[color=0000FF]    Online safety for grown ups[/color]"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            markup: True  # Enables the use of markup
            halign: "center"
            on_release: app.open_link("https://www.youtube.com/watch?v=iCs3aJYXLwo")
            ImageLeftWidget:
                source: 'Images/img_2.png'

        OneLineIconListItem:
            text: "[color=0000FF]    Digital Literacy – Staying safe online[/color]"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            markup: True  # Enables the use of markup
            halign: "center"
            on_release: app.open_link("https://www.youtube.com/watch?v=EyQeUwqCDWg")
            ImageLeftWidget:
                source: 'Images/img_3.png'

        OneLineIconListItem:
            text: "[color=0000FF]    60 Internet Slang Terms You NEED to Know![/color]"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            markup: True  # Enables the use of markup
            halign: "center"
            on_release: app.open_link("https://www.youtube.com/watch?v=PVnrDHHJwHM")
            ImageLeftWidget:
                source: 'Images/img_4.png'
"""

