class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit_count = defaultdict(int)
        ans = []

        for cpd in cpdomains:
            parts = cpd.split(" ")
            count = parts[0]

            part = parts[1].split(".")
            print(part)
            for i in range(len(part)):
                visit_count[".".join(part[i:])] += int(count)

        for key, val in visit_count.items():
            ans.append(f"{val} {key}")

        return ans
