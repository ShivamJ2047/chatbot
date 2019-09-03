from tkinter import *
import chatbot as cb
root = Tk()
root.title("Chatbot - made by shivam")
root.geometry("280x200")
class Application(Frame):
    def __init__(self,master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.lbl = Label(self,text = "Welcome to chatbot made using pyTorch\n")
        self.lbl.grid()
        self.user = Label(self,text = "User: ")
        self.user.grid(sticky = W)
        self.ur_ent= Entry(self)
        self.ur_ent.grid(column =0,sticky = W,padx = 5 , pady = 5)
        self.submit_btn = Button(self,text = "Submit",command = self.send)
        self.submit_btn.grid(row = 2,column = 1,sticky = W)
        self.botLabel = Label(self,text = "Bot: ")
        self.botLabel.grid(sticky = W)
        self.result = Text(self,width = 25,height = 5,wrap= WORD)
        self.result.grid(column =0,columnspan = 2,sticky = W,padx = 5,pady =5)
    def send(self):
        self.inputToApp = self.ur_ent.get()
        self.guiInput(cb.encoder,cb.decoder,cb.searcher,cb.voc)
    def guiInput(self,encoder, decoder, searcher, voc):
        try:
            # Get input sentence
            input_sentence = self.inputToApp
            # Check if it is quit case
            #if input_sentence == 'q' or input_sentence == 'quit': break
            # Normalize sentence
            input_sentence = cb.normalizeString(input_sentence)
            # Evaluate sentence
            output_words = cb.evaluate(encoder, decoder, searcher, voc, input_sentence)
            # Format and print response sentence
            output_words[:] = [x for x in output_words if not (x == 'EOS' or x == 'PAD')]
            AppToOutput =' '.join(output_words)

        except KeyError:
            AppToOutput = "Error: Encountered unknown word."
        self.guiOutput(AppToOutput)
    def guiOutput(self,AppToOutput):
        self.result.delete(0.0,END)
        self.result.insert(0.0,AppToOutput)
    
app = Application(root)
