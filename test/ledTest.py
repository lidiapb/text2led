from tkinter import *

class LedTest:
	leds = []
	rows = 8
	columns = 18
	window = object()
	txt = object()

	def clicked(self):
		#TODO: Start test
		#self.switch_led(2,4,True)
		input_text = self.txt.get()
		print(input_text)

	def switch_led(self, row, column, state):
		led=self.leds[row][column]
		if state==True:
			led.configure(bg="red")
		else:
			led.configure(bg="white")

	def run(self):
		# Define the leds height and width
		self.window = Tk()
		self.window.title("Led test")
		self.window.geometry('400x200')

		self.txt = Entry(self.window, width=30)
		self.txt.grid(column=0, row=0, columnspan=14)

		btn = Button(self.window, text="Start", command=self.clicked)
		btn.grid(column=14, row=0, columnspan=4)

		# Create leds elements
		for c in range(self.columns):
			row = []
			for r in range(self.rows):
				new_label = Label(self.window, text = " ", bg = "white")
				new_label.grid(column=c, row=r+1, padx=1, pady=1)
				row.append(new_label)
			self.leds.append(row)

		self.window.mainloop()

if __name__ == '__main__':
	test = LedTest()
	test.run()