from ans import make_dict
from ansk import make_keys

def give_exam():
    num=0
    numpq=float(input("Input marks / questions:\n"))
    ded=float(input("Input marks to be deducted for each question answered wrong (if any):\n"))
    answer_keys=make_keys()
    print("#####################################\n\n\n\n")
    answers=make_dict()
    for (i,v) in answers.items():
        if answer_keys[i]==v:
            num+=numpq
        else:
            num-=ded
    return num


if __name__=="__main__":
    result=give_exam()
    print("\n====================\nYou have got",result,"numbers!\n=======================\n")
