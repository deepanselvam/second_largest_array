class Solution:
    def Linear_search(self,array,B):
        count=0
        for i in array:
            if i==B:
                count+=1
        return count
if _name_== "_main_":
    ob=Solution()
    array=list(map(int,input().split()))
    B=int(input())
    print(ob.Linear_search(array,B))
