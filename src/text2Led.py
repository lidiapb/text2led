import json
class Text2Led:
    # TODO: Get path automatically
    with open('C:\\Users\\Lidia\\Documents\\Personal\\text2led\\src\\characters_matrix.json') as json_file:
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

            if matrix == []:
                matrix = [[] for idx in range(len(char_matrix))]

            # Append each row to the full matrix
            for row_index in range(len(char_matrix)):
                matrix[row_index] = matrix[row_index] + zeros + char_matrix[row_index]

        return matrix


    def character_to_matrix(self, character):
        # TODO: Check if key exists in dictionary. Return empty matrix otherwise
        return self.char2Matrix_dict[character]

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

            for column_index in range(len(row)):
                column = row[column_index]

                if column == 1:
                    coodinates = chr(row_index+65)+ str (column_index+1)
                    result.append(coodinates)

        return result

    def get_cut_matrix(self, input_matrix, start_col):
        # Return the part of the matrix starting from the column start_col and with maximum columns defined by self.columns. 
        # If there is space remaining, repeat the start of the matrix

        cut_matrix = []            
            
        # Initially cut row starting from the current start_col which changes with movement
        if start_col < len(input_matrix[0]):
            right_limit = start_col + 1
            right_zeros = [0 for ind in range(start_col - len(input_matrix[0]))]

        else:
            right_limit = len(input_matrix[0]) + 1
            right_zeros = []

        if start_col > self.columns:
            # If size exceeds available space, cut input row
            left_limit = start_col - self.columns
            left_zeros = []
            

        else:
            # Fill with zeros to the left to complete matrix size 
            left_limit = 0
            left_zeros = [0 for ind in range(self.columns - start_col)]               

        for row_index in range(len(input_matrix)):
            row = left_zeros + input_matrix[row_index][left_limit:right_limit] + right_zeros             
            cut_matrix.append(row)
        return cut_matrix



