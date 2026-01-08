class Binary_search:
    def solution(self,arr,ele):
        arr.sort()
        low=0
        high=len(arr)-1
        is_present=False
        while(low<=high):
            mid=(low+high)//2
            if ele==arr[mid]:
                is_present=True
                break
            elif ele<arr[mid]:
                high=mid-1
            elif ele>arr[mid]:
                low=mid+1
        print(is_present)
instance1=Binary_search()
lst=[20,12,4,34,23,18,19,29,34,36,43]
element=54
instance1.solution(lst,element)
