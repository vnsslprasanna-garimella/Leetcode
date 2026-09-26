class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d=dict(knowledge)
        res=[]
        cur=[]
        inside=False
        for ch in s:
            if ch=='(':
                inside=True
            elif ch==')':
                inside=False
                key=''.join(cur)
                res.append(d.get(key,'?'))
                cur=[]
            elif inside:
                cur.append(ch)
            else:
                res.append(ch)
        return ''.join(res)