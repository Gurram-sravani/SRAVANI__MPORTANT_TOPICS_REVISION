Dont use for key in count_dict:
        and if you are deleting the key when looping 
It will throw an error: RuntimeError: dictionary changed size during iteration
count_dict = {2:2, 3:1, 5:1}
for key in count_dict:  # Keys to iterate = [2,3,5]
  del count_dict[key]
After first iteration : count_dict : {3:1, 5:1}
# GETS ERROR
So Python stops the program and throws error : because  Python was expecting the dictionary size to remain the same while iterating.

Instead of iterating on the dictionary itself, iterate on a copy of the keys.
  Copy of keys = [2,3,5]
Even if you delete from dictionary:
count_dict becomes {3:1,5:1}
The loop is still safely iterating over:
[2,3,5]
for key in list(count_dict.keys()): 

''' When iterating directly over a dictionary using for key in count_dict,
Python expects the dictionary size to remain constant during iteration. 
If keys are added or removed (for example, using del count_dict[key]), Python raises a RuntimeError: dictionary changed size during iteration.

To avoid this, we iterate over list(count_dict.keys()). 
The list() function creates a separate shallow copy of the dictionary's keys at that moment. 
The loop then iterates over this independent list instead of the dictionary itself. 
Since the list does not change even if the dictionary is modified (keys deleted or added), it allows us to safely update the dictionary inside the loop without causing an iteration error. ''' 


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count_dict={}
        new_list=[]
        left_over=[]
        for i in range(len(arr1)):
            count_dict[arr1[i]]=count_dict.get(arr1[i],0)+1
        for element in arr2:
            if element in arr1:
                while count_dict[element]>=1:
                    new_list.append(element)
                    count_dict[element]-=1
                    if count_dict[element]==0:
                        del count_dict[element]
                        break
                    else:
                        continue
            else:
                continue
        for key in list(count_dict.keys()):
            while count_dict[key]>=1:
                left_over.append(key)
                count_dict[key]-=1
                if count_dict[key]==0:
                    del count_dict[key]
                    break
                else:
                    continue
        left_over.sort()
        return new_list+left_over



