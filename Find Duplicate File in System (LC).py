class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        ans=defaultdict(list)

        for file in paths:
            splited = file.split(" ")
            directory=splited[0]

            for i in splited[1:]:
                name,content=i.split("(")
                content=content[:-1]

                full_path= f"{directory}/{name}"
                ans[content].append(full_path)

            
        return [val for key,val in ans.items() if len(val)>1]
