import json
import os
class Text2Led:
    with open(os.path.join(os.path.abspath(os.getcwd()),'src','characters_matrix.json')) as json_file:
        char2Matrix_dict = json.load(json_file)   

    # Number of led columns to separate one character from the other
    chars_separation = 2 

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
    
    def parse_text(self, text):
        # This methid takes a string and converts it to a char list all in uppercase
        text=text.upper()
        char_list=[c for c in text]
        return char_list

    def charlist_to_matrix(self, characters):
        
        matrix = []
        zeros = [0 for sep in range(self.chars_separation)]
        for character in characters:            
            char_matrix = self.character_to_matrix(character)

            if char_matrix != []:
                if matrix == []:
                    matrix = [[] for idx in range(len(char_matrix))]

                # Append each row to the full matrix
                for row_index in range(len(char_matrix)):
                    if matrix[row_index] == []:
                        matrix[row_index] = matrix[row_index] + char_matrix[row_index]
                    else:
                        matrix[row_index] = matrix[row_index] + zeros + char_matrix[row_index]

        return matrix


    def character_to_matrix(self, character):
        if character in self.char2Matrix_dict.keys():
            return self.char2Matrix_dict[character]
        else:
            return []

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
        # [A1, B1, C1, C3]
        # 
        # meaning that only leds at those positions should be turned on.

        result = []

        for row_index in range(len(input_matrix)):
            row = input_matrix[row_index]

            for column_index in range(len(row)):
                column = row[column_index]

                if column == 1:
                    coordinates = chr(self.columns-row_index+65)+ str(self.rows - column_index)
                    result.append(coordinates)

        return result

    def get_cut_matrix(self, input_matrix, start_col):
        # Return the part of the matrix starting from the column start_col and with maximum columns defined by self.columns. 
        # If there is space remaining, repeat the start of the matrix

        cut_matrix = []                  

        for row_index in range(len(input_matrix)):
            row =  input_matrix[row_index][start_col:start_col+self.columns]             
            cut_matrix.append(row)
        return cut_matrix



