from ans import make_dict
from ansk import make_keys

app=Flask(__name__)

mistakes = list()
def give_exam():
    num=0
    numpq=float(input("Please tell us how many mark(s) each question would carry...\n"))
    ded=float(input("Please tell us the marks to be deducted for each question answered wrong (if any):\n"))
    answer_keys=make_keys()
    print("#####################################\n\n\n\n")
    answers=make_dict()
    for (i,v) in answers.items():
        if answer_keys[i]==v:
            num+=numpq
        else:
            if v==" ":
                num-=0
            else:
                mistakes.append(i)
                num-=ded
    return num


if __name__=="__main__":
    result=give_exam()
    print("\n====================\nYou have got",result,"numbers!\n=======================\n")
    if len(mistakes)>=1:
        print("Your mistakes were the following:\n")
        for i in range(len(mistakes)):
            print("Question number:",mistakes[i]);
