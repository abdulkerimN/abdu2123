class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        
        @lru_cache(None)
        def fn(n): 
            """Return prob of of points between K and N given current point n."""
            if N < n: return 0
            if K <= n: return 1
            if n+1 < K: return (1+W)/W*fn(n+1) - 1/W*fn(n+W+1)
            return 1/W*sum(fn(n+i) for i in range(1, W+1))
        
        return fn(0)

class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        ans = [0]*K + [1]*(N-K+1) + [0]*W
        val = sum(ans[K:K+W])
        for i in reversed(range(K)): 
            ans[i] = val/W
            val += ans[i] - ans[i+W]
        return ans[0]