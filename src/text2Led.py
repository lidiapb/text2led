class Text2Led:
	char2Matrix_dict = {} #TODO: Get from file
	
	def parse_text(self, text):
		# This methid takes a string and converts it to a char list all in uppercase
		text=text.upper()
		char_list=[c for c in text]
		return char_list

	def character_to_matrix(self, character):
		# Not implemented
		pass

	def matrix_conversion(self, input_matrix):
		# This method converts from a matrix of 1s and 0s to a list of coordinates A1, A2, etc. 
		# defined for a led matrix with letters being the columns and numbers the rows.
		#
		#  Example:
		# [[1, 0, 0],
		#  [0, 0, 0],
		#  [1, 1, 1]
		# ]
		# 
		# would be converted to: 
		#
		# [A1, A3, B1, C1]
		# 
		# meaning that only leds at those positions should be turned on.
	    result = []

	    for row_index in range(len(input_matrix)):
	        row = input_matrix[row_index]
	        #print(row)
	        for column_index in range(len(row)):
	            column = row[column_index]
	            #print(column)

	            if column == 1:
	                coodinates = chr(row_index+65)+ str (column_index+1)
	                result.append(coodinates)
	    #print(result)
	    return result
