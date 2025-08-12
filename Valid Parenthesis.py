class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # Mapping of each opening bracket to its correct closing bracket
        mapping = {'(': ')', '[': ']', '{': '}'}

        # Stack to keep track of opening brackets we have seen
        stack = []

        # Loop through each character in the string
        for ch in s:
            # If the character is an opening bracket
            if ch in mapping:
                # Push it onto the stack
                stack.append(ch)

            # If the character is a closing bracket
            elif ch in mapping.values():
                # If stack is empty, that means there's no matching opening bracket
                if not stack:
                    return False

                # Pop the last opening bracket from stack
                last_open = stack.pop()

                # Check if the closing bracket matches the correct one from mapping
                if mapping[last_open] != ch:
                    return False

            # If character is not a bracket at all (invalid input)
            else:
                return False

        # If stack is empty at the end, all brackets matched correctly
        return len(stack) == 0
# Testing the function
sol = Solution()

# Example 1: Valid parentheses
print(sol.isValid("()[]{}"))   # True

# Example 2: Invalid parentheses
print(sol.isValid("(]"))       # False

# Example 3: Another valid example
print(sol.isValid("{[()]}"))   # True