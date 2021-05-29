'''
Python CLI Voting System
'''
import sys
class VotingSystem(object):
    def __init__(self):
        self.admin={
            'username' : 'ali',
            'password' : 'Qwer@1234'
        }

        self.nominees = []
        self.votes = {}
        self.voted = []
        self.election_name=''

    def check_admin_auth(self):
        attempts = 3
        print("[Admin Login]")
        while attempts > 0:
            username = input("> User name : ")    
            password = input("> Password : ")

            if username == self.admin['username'] and password == self.admin['password']:
                return True

            print("Invalid Crenentials")    
            attempts -= 1
            print(f"Attempts Left : {attempts}")

        print("Maximum Attempts Reached, Exiting the program")   
        return False
    
    def start_voting(self):
        print(f"Voting started for [{self.election_name}] Election")
        while True:
            c=int(input("1] Cast Vote  2] End Voting  "))
            if c == 1:
                voter_id = input("> Voter Id:")
                if True: #Assessment
                    if voter_id not in self.voted:
                        print("Enter the number corresponding to the party name you want to vote")
                        for i,v in enumerate(self.nominees):
                            print(f"[{i+1}] {v} ", end=" ")    
                    print()    
                    while True:
                        p=int(input("> "))
                        if p in range(1, len(self.nominees)+1):
                            self.voted.append(voter_id)
                            self.votes[self.nominees[p-1]] +=1
                            print("You have successful voted")
                            break
                        else:
                            print("Invalid Choice, Try again")  
                    else:
                        print("You have already voted")          
                else:
                    print("Invalid Voter Id, Try again")            
            elif c == 2:
                if self.check_admin_auth():
                    self.end_voting()
                else:
                    print("Invalid Credentials")    
            else:
                print("Invalid Choice")     

    def end_voting(self):
        print(f"Voting Result for - {self.election_name}")  

        print("[Votes Table]\n")
        print(" | ".join(self.nominees))
        for k,v in self.votes.items():
            print(f"{v}",' '*(len(k)-len(str(v))),'|',end=" ")
        print()    

        print("[Election Winner]")

        max_voted_party = max(self.votes, key=self.votes.get)
        max_votes = self.votes[max_voted_party]

        winner=[]
        for k,v in self.votes.items():
            if v == max_votes:
                winner.append(k)

        if len(winner)>1:
            print("The election is ended with tie between following parties: ")        
            print(*winner, sep=',')
            print(f"Each party got {max_votes} votes")
        else:
            print(f"{max_voted_party} has won the election with {max_votes} votes")    
        sys.exit(0)    


    def start(self):
        to_proceed = True
        print("<<<<<<  WELCOME TO EVOLVES VOTING SYSTEM  >>>>>")
        print("- Please Login to Process")

        if self.check_admin_auth():

            while to_proceed:
                self.election_name = input("> Enter Election Name: ")
                total_nominees = int(input("> Enter Number of NOminees: "))

                print(f"Enter the name's for {total_nominees} nominees")
                for i in range(total_nominees):
                    n=input(f"Nominee [{i+1}] :")
                    self.nominees.append(n)
                    self.votes.setdefault(n,0)
                print("[Nominees]\n"," | ".join(self.nominees),"\n")
                print("1] Proceed 2] Reset 3] Exit")
                c=int(input("> "))
                if c == 1:
                    to_proceed=False
                    self.start_voting()
                elif c == 2:
                    break   
                elif c == 3:
                    sys.exit(0)   
                else:
                    print("Invalid Choice")    
            else:
                sys.exit(0) 


if __name__=='__main__':
    vc=VotingSystem()                   
    vc.start()

