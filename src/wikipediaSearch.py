import wikipedia as wiki
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class mainPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Question: "))
        self.question = TextInput(multiline=False)
        self.add_widget(self.question)

        self.add_widget(Label(text="Answer: "))
        self.answer = Label(text="", id="inputAnswerId")
        self.add_widget(self.answer)

        self.submit = Button(text="Submit")
        self.submit.bind(on_press=root.onPress_submitButton)
        self.add_widget(self.submit)

    def onPress_submitButton(self, instance):
        q = self.question.text
        a_wiki = wiki.summary(str(q))
        print(a_wiki)
        instance.parent.ids.inputAnswerId.text = a_wiki

class EpicApp(App):
    def build(self):
        return mainPage()

if __name__ == "__main__":
    #while True:
    #    myInput = input("Question: ")
    #    print(wiki.summary(str(myInput)))
    EpicApp().run()