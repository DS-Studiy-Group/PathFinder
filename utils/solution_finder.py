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
