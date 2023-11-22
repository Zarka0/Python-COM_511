def reverse_kth_rows(matrix, k):
    for i in range(0, len(matrix), k):
        matrix[i:i+k] = matrix[i:i+k][::-1]

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    try:
        # Input matrix
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        k = int(input("Enter the value of k: "))

        if k > 0 and k <= len(matrix):
            reverse_kth_rows(matrix, k)
            print("\nMatrix after reversing every", k, "row(s):")
            print_matrix(matrix)
        else:
            print("Invalid value of k. Please choose a value between 1 and", len(matrix))

    except ValueError:
        print("Invalid input. Please enter a valid integer for k."