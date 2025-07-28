# Flipping an Image

def flip_and_invert_image(image: list[list[int]]) -> list[list[int]]:
    flipped_and_inverted: list[list[int]] = []
    for row in image:
        flipped_and_inverted_row: list[int] = []
        for element in reversed(row):
            flipped_and_inverted_row.append(element ^ 1)

        flipped_and_inverted.append(flipped_and_inverted_row)
        
    return flipped_and_inverted


inputs = ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]])

for i in inputs:
    print(i, "\t\t\t", flip_and_invert_image(i))


"""
    [1, 1, 0] -> [1, 0, 0]

    
"""
