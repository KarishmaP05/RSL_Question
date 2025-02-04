def min_shifts_to_max_binary(binary):
    n = len(binary)
    binary_str = ''.join(map(str, binary))  # Convert binary array to a string for easy manipulation
    max_binary = binary_str  # Start with the original binary as the max
    min_shifts = 0

    # Check all circular shifts (both left and right) to find the maximum binary value
    for shift in range(1, n):
        left_shifted = binary_str[shift:] + binary_str[:shift]  # Left circular shift
        right_shifted = binary_str[-shift:] + binary_str[:-shift]  # Right circular shift

        # Update maximum binary value and the number of shifts required
        if left_shifted > max_binary:
            max_binary = left_shifted
            min_shifts = shift
            direction = "left"
        
        if right_shifted > max_binary:
            max_binary = right_shifted
            min_shifts = shift
            direction = "right"

    return min_shifts, direction

# Example usage
print(min_shifts_to_max_binary([0, 1, 1, 0, 1, 0]))  # Output: (1, 'left')
print(min_shifts_to_max_binary([0, 1, 0, 1, 1]))     # Output: (2, 'right')