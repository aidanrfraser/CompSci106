# Matrices
# for loops are better due to finite length
# Use len
# use that to transpose
# [[5, 1], [4, 6], [2, 3]]
# transposes to:
# [[5, 4, 2], [1, 6, 3]]

# row comes first
#for row
#   for column
#       swap row and column

def transpose(matrixA):
    for row in range(len(matrixA[0])):
        for column in range(len(matrixA)):
            