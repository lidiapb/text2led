
from src.text2Led import Text2Led
import time
import sys
import threading

WINDOWS = sys.platform.startswith('win')

if WINDOWS:
	from src.gui import Gui
	from test.ledTest import LedTest
	import threading
else:
	from src.led_manager import LedManager 	

rows = 18
columns = 11
period = 0.5 # Time between movements of the characters
chars_separation = 5 # Number of led columns to separate one character from the other

class Manager():
	last_iteration_time = 0

	def print_text(self, text):		
		print_thread = threading.Thread(target=self.print_text_threaded, args=(text,))
		print_thread.start()

	def print_text_threaded(self, text):
		# Print the input text in the leds and optionally in the test GUI if working on WINDOWS
		characters = self.t2l.parse_text(text) 
		led_matrix = self.t2l.charlist_to_matrix(characters)

		if(led_matrix != []):
			# Create led_matrix with zeros to the left and right for the full animation
			extended_led_matrix = []	
			zeros = [0 for col in range(columns)]
			for row in range(len(led_matrix)):
				extended_led_matrix.append(zeros + led_matrix[row] + zeros)

			index = 0

			while(True):
				time_now = time.time()
				if time_now - self.last_iteration_time < period:
					continue
				else:
					self.last_iteration_time = time_now
				
				cut_matrix = self.t2l.get_cut_matrix(extended_led_matrix, index)
				led_array = self.t2l.matrix_conversion(cut_matrix)

				if WINDOWS:
					self.led_test.draw_array(led_array)				
				else:	
					self.led_manager.draw_array(led_array)

				index+=1
				if index >= len(led_matrix[0]) + columns:
					index = 0
		else:
			print("No characters were converted")
							

	def run_gui(self, button_callback):
		self.gui = Gui(button_callback)
		self.gui.start()

	def run_test(self):
		self.led_test = LedTest(rows, columns)
		self.led_test.start()	

	def main(self):
		self.t2l = Text2Led(rows, columns, chars_separation)

		if WINDOWS:
				self.run_gui(self.print_text)
				self.run_test()
		else:
			self.led_manager = LedManager(rows=rows, cols=columns)
			text = input("Introduce the text: ")
			self.print_text(text)

if __name__ == '__main__':
	manager = Manager()
	manager.main()
