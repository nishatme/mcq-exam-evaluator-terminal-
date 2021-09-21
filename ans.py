def make_dict():
    retdic=dict()
    numofq=int(input("How many questions are there in the exam?\n"))
    for i in range(numofq):
        print("Answer to question number",i+1,":\n")
        temp_string=input()
        # Create an exception for instant looping through the input so as not to input other strings than abcd
        retdic[i+1]=temp_string
    return retdic
