import json

class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        return json.dumps(strs)

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        return json.loads(str)
    
    

original = ["abc", "123", ", \\\""]

encoded = Solution().encode(original)
decoded = Solution().decode(encoded)

print(encoded)
print(decoded)
print(decoded == original)
