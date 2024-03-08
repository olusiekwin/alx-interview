def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        prev_row = triangle[i - 1]
        for j in range(1, i):
            # Calculate the current element by summing the two elements directly above it
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))
