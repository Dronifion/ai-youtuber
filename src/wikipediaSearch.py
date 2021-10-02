import wikipedia as wiki
import kivy
from kivy.app import App
#from kivy.lang import Builder # it is to import Builder
#from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
#from kivy.uix.textinput import TextInput
#from kivy.uix.button import Button
#from kivy.uix.progressbar import ProgressBar 

# class mainPage(GridLayout):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.cols = 2

#         self.add_widget(Label(text="Question: "))
#         self.question = TextInput(multiline=False)
#         self.add_widget(self.question)

#         self.add_widget(Label(text="Answer: "))
#         self.answer = Label(text="", id="inputAnswerId")
#         self.add_widget(self.answer)

#         self.submit = Button(text="Submit")
#         self.submit.bind(on_press=root.onPress_submitButton)
#         self.add_widget(self.submit)

#     def onPress_submitButton(self, instance):
#         q = self.question.text
#         a_wiki = wiki.summary(str(q))
#         print(a_wiki)
#         instance.parent.ids.inputAnswerId.text = a_wiki

# building kv file as string
#kvfile = Builder.load_string("""

#""")

# This class stores the info of .kv file
# when it is called goes to my.kv file
class MainWidget(GridLayout):
    
    def onPress_submitButton(self):
        q = self.txtQuestion.text
        if len(q) > 0:
            try:
                ans_wiki = wiki.summary(str(q))
                self.txtAnswer.text = ans_wiki
            except Exception:
                wikiMulti = None
                for new_query in wiki.search(str(q)):
                    try:
                        wikiMulti += wiki.summary(new_query)
                    except Exception:
                        pass
                self.txtAnswer.text = wikiMulti        
            

    def onPress_saveFileButton(self):
        ans = self.txtAnswer.text
        self.lblFileStatus.text = ''
        if len(ans) > 0:
            with open('wikiResult.txt', 'w') as fh:
                fh.write(ans)  
                self.lblFileStatus.text = 'Saved'      


# define the App class
# and just pass rest write on kvfile
# not necessary to pass
# can also define function in it
class EpicApp(App):
    def build(self):
        # return a MainWidget() as a root widget
        return MainWidget()

if __name__ == "__main__":
    #while True:
    #    myInput = input("Question: ")
    #    print(wiki.summary(str(myInput)))
    EpicApp().run()