
WINDOWS = False

from src.text2Led import Text2Led

if WINDOWS:
	from src.gui import Gui
	from test.ledTest import LedTest
	import threading
else:
	from src.led_manager import LedManager

rows = 8
columns = 18

class Manager():
	def print_text(self, text):
		# Print the input text in the leds and optionally in the test GUI if working on WINDOWS

		characters = self.t2l.parse_text(text) 
		print (characters)

		# TODO: Create the real matrix of led position. This temporal matrix is for testing
		led_matrix = [[0,1],[1,1]]

		led_array = self.t2l.matrix_conversion(led_matrix)

		if WINDOWS:
			# Temp: Test connection with ledtest GUI by switching one led on
			self.led_test.draw_array(led_array)
		
		else:	
			self.led_manager.draw_array(led_array)

	def run_gui(self, button_callback):
		self.gui = Gui(button_callback)
		self.gui.run()

	def run_test(self):
		self.led_test = LedTest(rows, columns)
		self.led_test.run()

	def main(self):
		self.t2l = Text2Led()
		self.led_manager = LedManager()
		
		if WINDOWS:
			guiThread = threading.Thread(target = self.run_gui, args=(self.print_text,))
			guiThread.start()

			testThread = threading.Thread(target = self.run_test)
			testThread.start()
		else:
			text = input("Introduce the text: ")
			self.print_text(text)

if __name__ == '__main__':
	manager = Manager()
	manager.main()
