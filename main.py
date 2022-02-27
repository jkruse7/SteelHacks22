from PittAPI import laundry as PittAPI
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import MDList, ThreeLineListItem, IconLeftWidget, OneLineIconListItem, OneLineListItem

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
<MenuScreen>:
    name: 'menu'
    BoxLayout:
        padding:10
        # Adding image from the system
        Image:
            source: 'Laundry.jpg'
            # Giving the size of image
            size_hint_x: 0.1
            # allow stretching of image
            allow_stretch: False

    MDRectangleFlatButton:
        text: 'Check Machine Status'
        pos_hint: {'center_x':0.22,'center_y':0.8}
        on_press: root.manager.current = 'upload'
    MDRectangleFlatButton:
        text: 'Check Machine Status'
        pos_hint: {'center_x':0.62,'center_y':0.45}
        on_press: root.manager.current = 'upload'


<UploadScreen>:
    name: 'upload'
    BoxLayout:
        orientation: "vertical"
        BoxLayout:
            size_hint: 1,.1
            orientation: "horizontal"
            Button:
                text:"Washer"
            Button:
                text:"Dryer"
        ScrollView:
            GridLayout:
                orientation: "lr-tb"
                size_hint_y: None
                height: self.minimum_height  #<<<<<<<<<<<<<<<<<<<<
                row_default_height: 60
                cols:1
                
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt1
                        text:"GA02"
                        on_press: root.showStatus1()
                    Button:
                        id:txt2
                        text:"GA03"
                        on_press: root.showStatus2()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt3
                        text:"GA16"
                        on_press: root.showStatus3()
                    Button:
                        id:txt4
                        text:"GA15"
                        on_press: root.showStatus4()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt5
                        text:"BA14"
                        on_press: root.showStatus5()
                    Button:
                        id:txt6
                        text:"BA01"
                        on_press: root.showStatus6()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt7
                        text:"BA02"
                        on_press: root.showStatus7()
                    Button:
                        id:txt8
                        text:"BA03"
                        on_press: root.showStatus8()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt9
                        text:"BA04"
                        on_press: root.showStatus9()
                    Button:
                        id:txt10
                        text:"BA05"
                        on_press: root.showStatus10()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt11
                        text:"BA06"
                        on_press: root.showStatus11()
                    Button:
                        id:txt12
                        text:"BA07"
                        on_press: root.showStatus12()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt13
                        text:"BA08"
                        on_press: root.showStatus13()
                    Button:
                        id:txt14
                        text:"BA09"
                        on_press: root.showStatus14()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt15
                        text:"BA10"
                        on_press : root.showStatus15()
                    Button:
                        id:txt16
                        text:"BA11"
                        on_press: root.showStatus16()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt17
                        text:"BA12"
                        on_press: root.showStatus17()
                    Button:
                        id:txt18
                        text:"BA13"
                        on_press: root.showStatus18()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt19
                        text:"BA15"
                        
                        on_press : root.showStatus19()
                    Button:
                        id:txt20
                        text:"BA17"
                        on_press : root.showStatus20()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt21
                        text:"BA18"
                        on_press : root.showStatus21()
                    Button:
                        id:txt22
                        text:"BA19"
                        on_press : root.showStatus22()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt23
                        text:"BB05"
                        on_press : root.showStatus23()
                    Button:
                        id:txt24
                        text:"BB01"
                        on_press : root.showStatus24()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt25
                        text:"BB02"
                        on_press : root.showStatus25()
                    Button:
                        id:txt26
                        text:"BB03"
                        on_press : root.showStatus26()
                BoxLayout:
                    size_hint: 1,.1
                    orientation: "horizontal"
                    Button:
                        id:txt27
                        text:"BA04"
                        on_press : root.showStatus27()
                    Button:
                        id:txt28
                        text:"BB06"
                        on_press : root.showStatus28()
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'

"""


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    def showStatus1(self):
        name = self.ids.txt1.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                name = str(machine[i]['machine_status'])
                self.ids.txt1.text = name

    def showStatus2(self):
        name = self.ids.txt2.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt2.text = str(machine[i]['machine_status'])

    def showStatus3(self):
        name = self.ids.txt3.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt3.text = str(machine[i]['machine_status'])

    def showStatus4(self):
        name = self.ids.txt5.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt4.text = str(machine[i]['machine_status'])

    def showStatus5(self):
        name = self.ids.txt5.text
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt5.text = str(machine[i]['machine_status'])

    def showStatus6(self):
        name = self.ids.txt6.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt6.text = str(machine[i]['machine_status'])

    def showStatus7(self):
        name = self.ids.txt7.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt7.text = str(machine[i]['machine_status'])

    def showStatus8(self):
        name = self.ids.txt8.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt8.text = str(machine[i]['machine_status'])

    def showStatus9(self):
        name = self.ids.txt9.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt9.text = str(machine[i]['machine_status'])

    def showStatus10(self):
        name = self.ids.txt10.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt10.text = str(machine[i]['machine_status'])

    def showStatus11(self):
        name = self.ids.txt11.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt11.text = str(machine[i]['machine_status'])

    def showStatus12(self):
        name = self.ids.txt12.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt12.text = str(machine[i]['machine_status'])

    def showStatus13(self):
        name = self.ids.txt13.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt13.text = str(machine[i]['machine_status'])

    def showStatus14(self):
        name = self.ids.txt14.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt14.text = str(machine[i]['machine_status'])

    def showStatus15(self):
        name = self.ids.txt15.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt15.text = str(machine[i]['machine_status'])

    def showStatus16(self):
        name = self.ids.txt16.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt16.text = str(machine[i]['machine_status'])

    def showStatus17(self):
        name = self.ids.txt17.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt17.text = str(machine[i]['machine_status'])

    def showStatus18(self):
        name = self.ids.txt18.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt18.text = str(machine[i]['machine_status'])

    def showStatus19(self):
        name = self.ids.txt19.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt19.text = str(machine[i]['machine_status'])

    def showStatus20(self):
        name = self.ids.txt20.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt20.text = str(machine[i]['machine_status'])

    def showStatus21(self):
        name = self.ids.txt21.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt21.text = str(machine[i]['machine_status'])

    def showStatus22(self):
        name = self.ids.txt22.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt22.text = str(machine[i]['machine_status'])

    def showStatus23(self):
        name = self.ids.txt23.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt23.text = str(machine[i]['machine_status'])

    def showStatus24(self):
        name = self.ids.txt24.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt24.text = str(machine[i]['machine_status'])

    def showStatus25(self):
        name = self.ids.txt25.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt25.text = str(machine[i]['machine_status'])

    def showStatus26(self):
        name = self.ids.txt26.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt26.text = str(machine[i]['machine_status'])

    def showStatus27(self):
        name = self.ids.txt27.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt27.text = str(machine[i]['machine_status'])

    def showStatus28(self):
        name = self.ids.txt28.text
        print(name)
        machine = PittAPI.get_status_detailed("TOWERS")
        for i in range(len(machine)):
            if (str(machine[i]['machine_id']) == name):
                print(str(machine[i]['machine_status']))
                self.ids.txt28.text = str(machine[i]['machine_status'])


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(UploadScreen(name='upload'))


class DemApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemApp().run()