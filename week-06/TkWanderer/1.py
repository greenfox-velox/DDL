from first import return_map_int_matrix

def transform_matrix_to_map():
    map_matrix = return_map_int_matrix()
    my_dict = {}
    for row_numbers in range(10):
        for column_numbers in range(10):
            if map_matrix[row_numbers][column_numbers] == 0:
                my_dict.append(floor(row_numbers,column_numbers))
            else:
                my_dict.append(wall(row_numbers,column_numbers))
        print(my_dict)

transform_matrix_to_map()
