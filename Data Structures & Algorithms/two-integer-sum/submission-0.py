class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
                # Map to store the value as the key and its index as the value
        seen_numbers = {}
        for current_index, current_num in enumerate(nums):
                complement = target - current_num
                                            
                                                    # Check if the complement is already in our hash map
                if complement in seen_numbers:
                        # If found, return the index of the complement and the current index
                        return [seen_numbers[complement], current_index]
                                                                                            
                        # If not found, store the current number and its index in the map
                seen_numbers[current_num] = current_index
                                                                                                                    
        return []  # Return empty if no solution is found (per constraints, shouldn't happen)

                                