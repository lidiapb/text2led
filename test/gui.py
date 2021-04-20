from tkinter import *

class LedTest:
	leds = []
	rows = 8
	columns = 18

	def clicked(self):
		#TODO: Start test
		self.switch_led(2,4,True)

	def switch_led(self, row, column, state):
		led=self.leds[row][column]
		if state==True:
			led.configure(bg="red")
		else:
			led.configure(bg="white")

	def main(self):
		# Define the leds height and width
		window = Tk()
		window.title("Led test")
		window.geometry('400x200')

		txt = Entry(window, width=30)
		txt.grid(column=0, row=0, columnspan=14)

		btn = Button(window, text="Start", command=self.clicked)
		btn.grid(column=14, row=0, columnspan=4)

		# Create leds elements
		for c in range(self.columns):
			row = []
			for r in range(self.rows):
				new_label = Label(window, text = " ", bg = "white")
				new_label.grid(column=c, row=r+1, padx=1, pady=1)
				row.append(new_label)
			self.leds.append(row)

		window.mainloop()

test = LedTest()
test.main()