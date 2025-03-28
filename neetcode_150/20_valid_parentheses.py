class Solution:
    def isValid(self, s: str) -> bool:
        # STRATEGY:
        # Use a stack.
        # Use a dictionary that maps closing brackets to opening brackets
        parens_stack: list[str] = []
        close_to_open = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in close_to_open:
                if parens_stack and parens_stack.pop() == close_to_open[c]:
                    continue
                else:
                    return False
            else:
                parens_stack.append(c)

        return not parens_stack
