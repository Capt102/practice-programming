class Linear_search:
    def search(self,arr,ele):
        i=0
        is_present=False
        while(i<len(arr)):
            if arr[i]==ele:
                is_present=True
                break
            i+=1
        print(is_present)

instance1=Linear_search()
lst=[20,12,4,34,23,18,19,29,34,36,43]
element=40
instance1.search(lst,element)