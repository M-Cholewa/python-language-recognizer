import tkinter as tk 
import recognize as rec
  
# Top level window 
frame = tk.Tk() 
frame.title("Language Recognizer 2000") 
frame.geometry('400x200') 
  
def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    language, confidence = rec.recognize_language(inp)
    lbl.config(text = "Language "+language+" with confidence "+str(confidence)) 
  
# TextBox Creation 
inputtxt = tk.Text(frame, height = 5,  width = 20) 
  
inputtxt.pack() 
  
# Button Creation 
printButton = tk.Button(frame,   text = "Print",   command = printInput) 
printButton.pack() 
  
# Label Creation 
lbl = tk.Label(frame, text = "") 
lbl.pack() 
frame.mainloop() 