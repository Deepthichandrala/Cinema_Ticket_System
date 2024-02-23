print("Welcome to Online Voting!")
nomine_1="hari"
nomine_2="jabi"
candidate_1=0
candidate_2=0
voters_id=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
total_voters=len(voters_id)
while True:
    if voters_id==[]:
        print("voting session over")
        if candidate_1>candidate_2:
            percentage=(candidate_1/total_voters)*100
            print(nomine_1,"has won",percentage,"% votes")
            break
        elif candidate_2>candidate_1:
            percentage=(candidate_2/total_voters)*100
            print(nomine_2,"has won",percentage,"% votes")
            break
    else: 
        voter=int(input("enter your voter id no:"))
    if voter in voters_id:
        voters_id.remove(voter)
        print("choose the nomine that you want to vote for:")
        vote=int(input("1.Hari \n2.jabi \n  "))
        if vote==1:
            candidate_1+=1
            print("Thank you for casting your vote")
        elif vote==2:
            candidate_2+=1
            print("Thank you for casting your vote")
    else:
        print("you are not a voter here or you have alredy voted")
                
                
        
        
               
    