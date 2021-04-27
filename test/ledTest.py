from tkinter import *

class LedTest:
	leds = []
	rows = 8
	columns = 18

	def switch_led(self, row, column, state):
		led=self.leds[row][column]
		if state==True:
			led.configure(bg="red")
		else:
			led.configure(bg="white")

	def run(self):
		self.window = Tk()
		self.window.title("Led test")
		self.window.geometry('400x200')

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