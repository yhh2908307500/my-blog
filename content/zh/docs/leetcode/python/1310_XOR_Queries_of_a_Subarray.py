class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 前缀异或：区间[l,r]异或等于pref[r+1]^pref[l]
        pref = [0]
        for e in arr:
            pref.append(e ^ pref[-1])
        ans = []
        for [l, r] in queries:
            ans.append(pref[r+1] ^ pref[l])
        return ans

    # def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    #     for i in range(len(arr) - 1):
    #         arr[i + 1] ^= arr[i]
    #     return [arr[j] ^ arr[i - 1] if i else arr[j] for i, j in queries]
