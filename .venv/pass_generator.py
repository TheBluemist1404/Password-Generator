from kivy.uix.boxlayout import BoxLayout
import random

class PassGenerator(BoxLayout):
    lower_case = "qwertyuiopasdfghjklzxcvbnm"
    upper_case = "QWERTYUIOPASDFGHJKLZXCVBNM"
    number = "1234567890"
    special_character = "!@#$%^&*()-_=+\|[]{};:/?.,<>`~"

    char_set = [lower_case,upper_case,number,special_character]

    def __init__(self,**kwargs):
        super(PassGenerator,self).__init__(**kwargs)

    def generate(self, *args):
        txt = self.text_input.input.text
        if not txt.isdigit():
            self.output.text = "Invalid length"
        else:
            if int(txt) != 0:
                self.output.text = "Valid length"
            else:
                self.output.text = "Invalid length"

        if self.output.text == "Valid length":
            char_set = self.char_set.copy()
            if self.upper.check.state == 'normal':
                char_set.remove(self.char_set[1])
            if self.number.check.state == 'normal':
                char_set.remove(self.char_set[2])
            if self.special.check.state == 'normal':
                char_set.remove(self.char_set[3])

            password = ""
            for _ in range(int(txt)):
                str = random.choice(char_set)
                char = random.choice(str)
                password += char
            self.output.text = password


