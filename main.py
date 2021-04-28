
from src.text2Led import Text2Led
from src.gui import Gui
from test.ledTest import LedTest

import threading

TEST_MODE = True

class Manager():
	def convert_text(self, text):
		characters = self.t2l.parse_text(text) 
		print (characters)

		if TEST_MODE:
			# Temp: Test connection with test by switching one led on
			self.led_test.switch_led(0, 0, True)

	def run_gui(self, button_callback):
		self.gui = Gui(button_callback)
		self.gui.run()

	def run_test(self):
		self.led_test = LedTest()
		self.led_test.run()

	def main(self):
		self.t2l = Text2Led()
		guiThread = threading.Thread(target = self.run_gui, args=(self.convert_text,))
		guiThread.start()

		if TEST_MODE:
			testThread = threading.Thread(target = self.run_test)
			testThread.start()
		else:
			pass
			#led programming

if __name__ == '__main__':
	manager = Manager()
	manager.main()