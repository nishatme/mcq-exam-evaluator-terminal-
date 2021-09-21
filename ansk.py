def make_keys():
    retdic=dict()
    numofq=int(input("How many questions are there in this exam?\n"))
    for i in range(numofq):
        print("What is the answer to the question no",i+1,"?\n")
        temp_string=input()
        retdic[i+1]=temp_string
    return retdic
