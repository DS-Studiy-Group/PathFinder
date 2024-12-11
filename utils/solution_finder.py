def find_solution_subsets(nums, target):
    result = []

    def backtrack(start, current_subset, current_sum):
        if current_sum == target:
            result.append(current_subset[:])
            return
        if current_sum > target:
            return

        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset, current_sum + int(nums[i].value))
            current_subset.pop()

    backtrack(0, [], 0)
    return result


