from tkinter import *

class LedTest:
	leds = []

	def __init__(self, rows, columns):
		self.rows = rows
		self.columns = columns

	def switch_led(self, row, column, state):
		led=self.leds[row][column]
		if state==True:
			led.configure(bg="red")
		else:
			led.configure(bg="white")

	def clear(self):
		for row in range(self.rows):
			for col in range(self.columns):
				led = self.leds[row][column]
				led.configure(bg="white")

	def draw_array(self, led_array):
		for led in led_array:
			row = ord(led[0])-65
			col = int(led[1])
			switch_led(row, column, True)

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