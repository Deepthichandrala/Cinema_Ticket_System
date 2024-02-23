
def _init_(self):
    self.candidates = {}
    self.voters = {}

def add_candidate(self, candidate_name):
    if candidate_name not in self.candidates:
        self.candidates[candidate_name] = 0
        print(f"Candidate {candidate_name} added successfully.")
    else:
        print(f"Error: Candidate {candidate_name} already exists.")

def vote(self, voter_name, candidate_name):
    if voter_name not in self.voters:
        if candidate_name in self.candidates:
            self.candidates[candidate_name] += 1
            self.voters[voter_name] = candidate_name
            print(f"Thank you, {voter_name}, for voting for {candidate_name}.")
        else:
            print(f"Error: Candidate {candidate_name} does not exist.")
    else:
            print(f"Error: {voter_name}, you have already voted.")

def display_results(self):
    print("\nVoting Results:")
    for candidate, votes in self.candidates.items():
        print(f"{candidate}: {votes} votes")

while True:
        print("\nWelcome to the Online Voting System")
        print("1. Add Candidate")
        print("2. Vote")
        print("3. Display Results")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            candidate_name = input("Enter the candidate's name: ")
            voting_system.add_candidate(candidate_name)
        elif choice == '2':
            voter_name = input("Enter your name: ")
            candidate_name = input("Enter the candidate's name you want to vote for: ")
            voting_system.vote(voter_name, candidate_name)
        elif choice == '3':
            voting_system.display_results()
        elif choice == '4':
            print("Exiting the Online Voting System.")
            break
        else:
            print("Invalid choice. Please try again.")