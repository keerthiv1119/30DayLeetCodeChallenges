def countElements(self, arr: List[int]) -> int:
        dictionary = {}
        for i in arr:
            dictionary[i] = 1
        count = 0
        for x in arr:
            if x + 1 in dictionary:
                count += 1
        return count
