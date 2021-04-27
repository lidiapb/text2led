
from src.textToLed import TextToLed
from test.ledTest import LedTest
TEST_MODE = True

def main():
	t2l = TextToLed()

	if TEST_MODE:
		text = "Hola"
		characters = t2l.parse_text(text) 
		print (characters)
	else:
		pass
		#led programming

if __name__ == '__main__':
	main()