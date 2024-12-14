def find_solution_subsets(cells, target):
    result = []

    def backtrack(start, current_subset: set, current_sum):
        if current_sum == target:
            result.append(current_subset.copy())
            return

        if current_sum > target:
            return

        for i in range(start, len(cells)):
            temp_subset = current_subset.copy()
            temp_subset.add(cells[i])
            backtrack(i + 1, temp_subset, current_sum + int(cells[i].value))

    backtrack(0, set(), 0)
    return result


def dfs_maze_with_target_and_sum(maze, start, target_sum, end):

    rows, cols = len(maze), len(maze[0])
    visited = set()
    path = []

    nums = [maze[r][c] for r in range(rows) for c in range(cols) if maze[r][c] != "WALL"]
    valid_subsets = find_solution_subsets(nums, target_sum)

    target_values = set(valid_subsets[0]) if valid_subsets else set() 

    def is_valid_move(row, col):
        """Check if moving to the given cell is valid."""
        return (
            0 <= row < rows and 0 <= col < cols and
            (row, col) not in visited and
            maze[row][col] != "WALL" and
            (not target_values or maze[row][col] in target_values)  
        )

    def dfs(row, col, current_sum):
       
        path.append((row, col))
        visited.add((row, col))

        if current_sum == target_sum:
            if dfs_to_end(row, col):
                return True

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if is_valid_move(new_row, new_col):
                if dfs(new_row, new_col, current_sum + maze[new_row][new_col]):
                    return True

        path.pop()
        visited.remove((row, col))
        return False

    def dfs_to_end(row, col):
        if (row, col) == end:
            return True

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in visited and maze[new_row][new_col] != "WALL":
                visited.add((new_row, new_col))
                path.append((new_row, new_col))
                if dfs_to_end(new_row, new_col):
                    return True
                path.pop()
                visited.remove((new_row, new_col))
        return False

    start_row, start_col = start
    if dfs(start_row, start_col, maze[start_row][start_col]):
        return path
    else:
        path.clear()
        visited.clear()
        if dfs_to_end(start_row, start_col):
            return path
        return []  # No path to the end found

