class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        mapp = defaultdict(int)

        for i in range(len(responses)):
            responses[i] = set(responses[i])

        for res in responses:
            for r in res:
                mapp[r] += 1

        mapp = dict(sorted(mapp.items(), key=lambda x: (-x[1], x[0])))

        return next(iter(mapp))
