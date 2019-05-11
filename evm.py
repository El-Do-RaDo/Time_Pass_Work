import sys

def vote (voting_list, ballot_list, num):
 
    if num == 1:
        voting_list.append("TDP") 
        print("Voted for TDP")
        print(voting_list)
    elif num == 2:
        voting_list.append("YSRCP") 
        print("Voted for YSRCP")
        print(voting_list)
    elif num == 3:
        voting_list.append ("BJP")
        print("Voted for BJP")
        print(voting_list)
    elif num == 4:
        voting_list.append ("Congress")
        print("Voted for Congress")
        print(voting_list)
    elif num == 5:
        voting_list.append ("JANASENA")
        print("Voted for JANASENA")
        print(voting_list) 
    elif num == 6:
        voting_list.append ("NOTA")
        print("Voted for NOTA")
        print(voting_list)
    elif num == 7:
        sys.exit()
    else:
        print("input not given")


def vote_d (voting_list, ballot_list, num):
 
    if num == 1:
        voting_list.append("BJP") 
        print("Voted for TDP")
        print(voting_list)
    elif num == 2:
        voting_list.append("BJP") 
        print("Voted for YSRCP")
        print(voting_list)
    elif num == 3:
        voting_list.append ("BPJ")
        print("Voted for BJP")
        print(voting_list)
    elif num == 4:
        voting_list.append ("BJP")
        print("Voted for Congress")
        print(voting_list)
    elif num == 5:
        voting_list.append ("BJP")
        print("Voted for JANASENA")
        print(voting_list) 
    elif num == 6:
        voting_list.append ("BJP")
        print("Voted for NOTA")
        print(voting_list)
    elif num == 7:
        sys.exit()
    else:
        print("input not given")


voting_list = []
ballot_list = []
for i in range(100):
	b = input("Enter ballot number: ")
	if b in ballot_list:
		print("You have already voted")
	else:
		print("1. TDP")
		print("2. YSRCP")
		print("3. BJP")
		print("4. Congress")
		print("5. Janasena")
		print("6. NOTA") 
		print("7. Exit")
		num = int(input("Press button whom you want to vote: "))
		ballot_list.append(b)
		if i>80:
			vote(voting_list, ballot_list, num)
		else:
			vote_d(voting_list, ballot_list, num)

cy = voting_list.count("YSRCP")
if cy < 9:
	for i in range(0,6):
		voting_list[i] = 'YSRCP'	
print(voting_list)




















