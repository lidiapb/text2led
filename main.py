
WINDOWS = True

from src.text2Led import Text2Led
from src.led_manager import LedManager

if WINDOWS:
	from src.gui import Gui
	from test.ledTest import LedTest

import threading

class Manager():
	def convert_text(self, text):
		characters = self.t2l.parse_text(text) 
		print (characters)

		if WINDOWS:
			# Temp: Test connection with ledtest GUI by switching one led on
			self.led_test.switch_led(0, 0, True)
		
		# Pending call to the ledmanager
		

	def run_gui(self, button_callback):
		self.gui = Gui(button_callback)
		self.gui.run()

	def run_test(self):
		self.led_test = LedTest()
		self.led_test.run()

	def main(self):
		self.t2l = Text2Led()
		self.led_manager = LedManager()
		
		if WINDOWS:
			guiThread = threading.Thread(target = self.run_gui, args=(self.convert_text,))
			guiThread.start()

			testThread = threading.Thread(target = self.run_test)
			testThread.start()
		else:
			text = input("Introduce the text: ")
			self.convert_text(text)

if __name__ == '__main__':
	manager = Manager()
	manager.main()
