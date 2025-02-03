def longest_remaining_string(strings):
    if not strings:
        return ""

    # Step 1: Find the longest common prefix (LCP)
    sorted_strings = sorted(strings)
    first, last = sorted_strings[0], sorted_strings[-1]
    print(first, last )
    lcp_length = 0
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            lcp_length += 1
        else:
            break
    lcp = first[:lcp_length]

    # Step 2: Remove the LCP from each string and find the longest remaining string
    longest_remaining = ""
    for s in strings:
        remaining = s[len(lcp):]
        if len(remaining) > len(longest_remaining):
            longest_remaining = remaining

    return longest_remaining

# Example usage:
def execute_three_strings():
    strings1 = ["Thalaiva", "Thala", "Thalapathy"]
    strings2 = ["Raja", "Software"]
    strings3 = ["Hibambe", "Hibambe"]

    print("Output for strings1:", longest_remaining_string(strings1))  # Output: "pathy"
    print("Output for strings2:", longest_remaining_string(strings2))  # Output: "Software"
    print("Output for strings3:", longest_remaining_string(strings3))  # Output: ""

# Execute the function for all three sets of strings
execute_three_strings()