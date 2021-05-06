from tkinter import *
import threading

class Gui(threading.Thread):
	window = object()
	txt = object()		

	def __init__(self, callback):
		threading.Thread.__init__(self)
		self.callback = callback

	def clicked(self):
		input_text = self.txt.get()
		self.callback(input_text)

	def close(self):
		self.window.destroy()

	def run(self):
		self.window = Tk()
		self.window.title("Main window")
		self.window.geometry('300x50')

		self.txt = Entry(self.window, width=30)
		self.txt.grid(column=0, row=0, columnspan=14)

		btn = Button(self.window, text="Start", command=self.clicked)
		btn.grid(column=14, row=0, columnspan=4)

		self.window.mainloop()

if __name__ == '__main__':
	gui = Gui()
	gui.run()