def solution(S):
    result = []

    # Iterate through each position of the strings
    for pos in range(len(S[0])):
        # Create a dictionary to store positions where each character occurs
        hashmap = {}

        # Iterate through each string
        for i, string in enumerate(S):
            # Get the character at the current position
            ch = string[pos]

            # Check if the character has occurred before at this position
            if ch in hashmap:
                # Found a pair of strings with a common letter at the same position
                result.append([hashmap[ch], i, pos])
                return result
            # Update the hashmap with the position of the character
            hashmap[ch] = i

    # If no pair is found, return an empty array
    return result

# Examples
S1 = ["abc", "bca", "dbe"]
print(solution(S1)) 

S2 = ["zzzz", "ferz", "zdsr", "fgtd"]
print(solution(S2))  

S3 = ["gr", "sd", "rg"]
print(solution(S3))     

S4 = ["bdafg", "ceagi"]
print(solution(S4))  
