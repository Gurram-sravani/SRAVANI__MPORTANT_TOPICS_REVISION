class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs=[]
        letter_logs=[]
        for i in range(len(logs)):
            result=logs[i].split(" ",1)
            identifier=result[0]
            content=result[1]
            if content[0].isdigit():
                digit_logs.append(logs[i])
            else:
                letter_logs.append(logs[i])
        print(letter_logs)
        print(digit_logs)
        letter_logs.sort(key=lambda log: (log.split(" ", 1)[1],log.split(" ", 1)[0]))  #  key= must receive a FUNCTION that takes one element and returns sort value
        return letter_logs+digit_logs

'''Careful and understand everything about string function how tuple unpack helpful, What if I use dictionary"
