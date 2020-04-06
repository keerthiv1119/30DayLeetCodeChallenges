'''
Author : Keerthi Vutukuri
Date : 02- 04-2020
Name : Group Anagrams
'''
import collections
strs = ["eat","ate","hi","ih"]
ans = collections.defaultdict(list)
for s in strs:
    ans[tuple(sorted(s))].append(s)
print(ans.values()
