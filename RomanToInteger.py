class Solution:
    def romanToInt(self, s: str) -> int:
        # Previous must always be >= next, or it's a subtraction
        returnNumber = 0
        numerals= {
            "I": 1,
            "V": 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        previous = None
        for c in s:
            returnNumber += numerals[c]
            if previous and numerals[previous] < numerals[c]:
                # remove previous
                returnNumber -= numerals[previous]
                # remove from next number
                returnNumber -= numerals[previous]
            previous = c
        return returnNumber
        