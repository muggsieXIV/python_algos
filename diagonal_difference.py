# // https://www.hackerrank.com/challenges/diagonal-difference/problem
# /* 
#     Given a square matrix (2d array) of integers n*n
#     Calculate the absolute difference between the sums of its diagonals
#         - top left to bottom right diagonal diagonal 1
#         - top right to bottom left diagonal diagonal 2 
#  */
# // function diagonalDifference(matrix){
# //     var x = martix[0];
# //     var y = matrix.length-1;
# //     var z = martix.length/2;
# //     // left to bottom right
    
# // }
# // diagonalDifference(
# //     [
# //         3,2,12
# //         ,4,5,6,
# //         7,10,4
# //     ]
# //     );

def diagonal_difference(matrix):
    is_valid = False 
    dgnl_diff = None

    # Check to make sure matrix is valid 
    if len(matrix) % 2 == 0 or len(matrix) % 3 == 0:
        is_valid = True

    if is_valid:
        # d1 = matrix[0]
        # d2 = len(matrix) - 1
        # dz = len(matrix) / 2

        length = len(matrix)
        diag1 = 0 
        diag2 = 0

        for i in range(0, length):
            for j in range(0, length): 
                if i == j:
                    diag1 += matrix[i]
        dgnl_diff = abs(diag1 - diag2)
        return dgnl_diff

    if not is_valid:
        return "Matrix is invalid, please try again"

    return dgnl_diff

print(diagonal_difference([3,2,12,4,5,6,7,10,4]))
