from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorAppMAM(App):
    def build(self):
        # Main layout (vertical)
        main_layout_mam = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Display
        self.display_mam = TextInput(
            readonly=True,
            halign="right",
            font_size=32,
            size_hint=(1, 0.2),
        )
        main_layout_mam.add_widget(self.display_mam)

        # Buttons layout (grid)
        buttons_layout_mam = GridLayout(cols=4, spacing=10, size_hint=(1, 0.8))

        buttons_mam = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "CLEAR", "=", "+"
        ]

        for btn_text_mam in buttons_mam:
            button_mam = Button(
                text=btn_text_mam,
                font_size=24,
                on_press=self.on_button_press_mam
            )
            buttons_layout_mam.add_widget(button_mam)

        main_layout_mam.add_widget(buttons_layout_mam)
        return main_layout_mam

    def on_button_press_mam(self, instance):
        btn_text_mam = instance.text

        if btn_text_mam == "CLEAR":
            self.display_mam.text = ""
        elif btn_text_mam == "=":
            try:
                result_mam = str(eval(self.display_mam.text))
                self.display_mam.text = result_mam
            except:
                self.display_mam.text = "Error"
        else:
            self.display_mam.text += btn_text_mam

if __name__ == "__main__":
    CalculatorAppMAM().run()
