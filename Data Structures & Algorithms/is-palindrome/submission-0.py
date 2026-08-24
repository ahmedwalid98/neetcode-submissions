class Solution:
    def isPalindrome(self, s: str) -> bool:
       

        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        first = 0
        last = len(cleaned) - 1

        while first < last:
            if cleaned[first] == cleaned[last]:
                first += 1
                last -= 1
            else:
                return False

        return True

        


        