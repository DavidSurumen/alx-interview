def island_perimeter(grid):
    perimeter = 0
    
    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:  # Check if the cell is land
                # Check top side
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Check bottom side
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Check left side
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Check right side
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
