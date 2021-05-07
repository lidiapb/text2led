from tkinter import *
import threading

class LedTest(threading.Thread):
	leds = []

	def __init__(self, rows, columns):
		threading.Thread.__init__(self)
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
				led = self.leds[row][col]
				led.configure(bg="white")

	def draw_array(self, led_array):
		self.clear()
		for led in led_array:
			row = self.columns - (ord(led[0])-65)
			col = self.rows - int(led[1:])
			# Avoid overflow
			if(row >= 0 and row < self.rows and col >= 0 and col < self.columns):
				self.switch_led(row, col, True)

	def run(self):
		self.window = Tk()
		self.window.title("Led test")
		self.window.geometry('400x200')

		# Create leds elements
		for r in range(self.rows):
			row = []
			for c in range(self.columns):
				new_label = Label(self.window, text = " ", bg = "white")
				new_label.grid(column=c, row=r+1, padx=1, pady=1)
				row.append(new_label)
			self.leds.append(row)

		self.window.mainloop()

	def close(self):
		self.window.destroy()

if __name__ == '__main__':
	test = LedTest()
	test.run()