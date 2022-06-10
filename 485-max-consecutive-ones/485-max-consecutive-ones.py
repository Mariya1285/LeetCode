class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start, end = 0, 1
        max_len = 0
        if len(nums)==1:
            if nums[0]==0:
                return 0
            else:
                return 1
        else:
            while end<len(nums):
                print("end: ",end)
                print("start: ", start)
                if end!=len(nums)-1:
                    if nums[end]==1:
                        end+=1
                    else:
                        print("end: ",end)
                        print("start: ", start)
                        if (end-start)>max_len:
                            max_len=end-start
                            print("end element 0")
                        else:
                            pass

                        end+=1
                        start=end
                        print("MAX LEn: ", max_len)
                elif nums[end]==0 and end==len(nums)-1:
                    print("I m here")
                    if nums[end-1]==1:
                        if start!=0:
                            if (end-start+1)>max_len:
                                max_len=end-start+1
                            else:
                                pass
                        else:
                            if (end-start)>max_len:
                                max_len=end-start
                            else:
                                pass
                    else:
                        pass

                    end+=1
                    start=end
                    print("end max_len: ", max_len)
                
                elif nums[end]==1 and end==len(nums)-1:
                    if start!=0:
                        if (end-start+1)>max_len:
                                max_len=end-start+1
                        else:
                            pass
                    else:
                        if nums[end-1]!=1:
                            if (end-start)>max_len:
                                max_len=end-start 
                                return max_len
                            else:
                                pass
                        else:
                            if (end-start+1)>max_len:
                                max_len=end-start+1 
                                return max_len
                            else:
                                pass
                    end+=1
                    start=end
                
            print("**********************************")
            return max_len