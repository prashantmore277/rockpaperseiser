import random as rdm

#Define game function

def game():
	print("Welcome to Rock Paper Scissor\n")
	
	print("INFO :-")
	Name = str(input("Your Name : "))
	City = str(input("Your City : "))
	
	print("\nGame Rules :")
	print("1 ] R=Rock P=Paper S=Scissor\n2 ] Rock blends Scissor\n3 ] Paper covers Rock\n4 ] Scissor cuts Paper\n5 ] If Player won 1 point\n    added in players account\n6 ] If Bot won 1 point goes\n    in bots account\n7 ] For Tie one point add\n    in both players account\n8 ] Total matches compalsory\n9 ] At end Winner will be annouced\n")
	
	Count= 10
	Your_score=0
	Bot_score=0
	print("~~~~~~~~~~~~~~~~~~~~~~~\n")
	print("Your Score : ",Your_score)
	print("Bot Score : ",Bot_score)
	print("\n~~~~~~~~~~~~~~~~~~~~~~~\n")
	while (Count>0):
		print("~~~~~~~~~~~~~~~~~~~~~~~\n")
		Count-=1
		print("Round No = ",10-Count)
		print("\nYour Choise :\n")
		print("Rock = 1\nPaper = 2\nScissor = 3\n")
		List2 = ["Rock","Paper","Scissor"]
		P= int(input("Choose 1/2/3 = " ))
		B =rdm.randint(1,3)
		
		if(P==B):
			
			print("\nYour choise :",List2[P-1])
			print("Bot choise :",List2[B-1],"\n")
			print("__________Tie__________\n")
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
			
			
		elif(P==1 and B!=1 and B!=2 and B==3):
			print("Your choise :",List2[P-1])
			print("Bot choise :",List2[B-1])
			print("____Winner Winner____\n")
			print("\nRock blends Scissor\n")
			Your_score += 1
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
			
			
			
		elif (P==2 and B!=2 and B!=3 and B==1):
			print("Your choise :",List2[P-1])
			print("Bot choise :",List2[B-1])
			print("\n")
			print("  🤠🤠🤠🤠🤠🤠🤠🤠")
			print("____Winner Winner____\n")
			print("\nPaper covers Rock\n")
			Your_score += 1
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
			
			
		elif(P==3 and B!=3 and B!=1 and B==2):
			print("Your choise :",List2[P-1])
			print("Bot choise :",List2[B-1])
			print("\n")
			print("____Winner Winner____\n")
			print("\nSizzer cuts Paper\n")
			Your_score += 1
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
						
		elif( P!=B ):
			print("Your choise :",List2[P-1])
			print("Bot choise :",List2[B-1])
			print("\n")
			print("____Ping Pong Looser____\n")
			Bot_score += 1
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
		
		print("Match Remaning :",Count,"\n")
		print("~~~~~~~~~~~~~~~~~~~~~~~\n")
		print("\n")		
	print("\n")
	
	if(Your_score>Bot_score):
			#print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
			status = "Winner"
			print ("😃😃",status,"😀😀")
			print("~~~~~~~~~~~~~~~~~~~~~~\n")
			#print("~~~~~~~~~~~~~~~~~~~~~~\n")
	if(Bot_score>Your_score):
			#print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
			status = "Looser"
			print ("😡😡",status,"😡😡")
			print("~~~~~~~~~~~~~~~~~~~~~~\n")
			#print("~~~~~~~~~~~~~~~~~~~~~~\n")
	elif( Your_score==Bot_score   ):
			#print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("Your Score : ",Your_score)
			print("Bot Score : ",Bot_score,"\n")
			status = "Tied"
			print ("😑😑",status,"😑😑")
			
			#print("~~~~~~~~~~~~~~~~~~~~~~\n")
			print("~~~~~~~~~~~~~~~~~~~~~~\n")
			
# Create a record and save details of Game

	with open("pygamerecord.txt","a") as R:
		string= " "
		string += ("\n")
		string += str("\nRecord Details :")
		string += str("\n")
		string += str("My name is")+str(" ") +  str(Name)
		string += ("\n")
		string += str("My city is")+ str(" ") +  str(City)
		string += ("\n")
		string += str("Game Status")+ str(" ") +  str(status)
		string += ("\n")
		string += ("~~~~~~~~~~~~~~~~~~~~~~~~")
		R.write(string)
	menu()
# Define record function

def records():
	f=open("pygamerecord.txt","rt")
	RECORD=f.read()
	print(RECORD)
	f.close
	menu()

# Define clear records function

def clear_records():
	file = open("pygamerecord.txt","r+")
	file. truncate()
	file. close()
	print("\nRecords Clear Succesfully.....\n")
	menu()
	
def menu_dup_record():
		print("\nDuplecate Records: \n1 ] Type 1 to Create  ==> Winner Entry\n2 ] Type 2 to Create ==> Looser Entry\n3 ] Type 3 to Create ==> Tied Entry\n=>")
		dup_record()
		print("\nRecord added Successfully.......\n")
		menu()

def dup_record():
	Y=int(input())
	list3=["Winner","Looser","Tied"]
	with open("pygamerecord.txt","a") as R:
		print("INFO :-")
		Name = str(input("Your Name : "))
		City = str(input("Your City : "))
		string= " "
		string += ("\n")
		string += str("\nRecord Details :")
		string += str("\n")
		string += str("My name is")+str(" ") +  str(Name)
		string += ("\n")
		string += str("My Age is")+ str(" ") +str(City)
		string += ("\n")
		string += str("Game Status")+ str(" ") +str(list3[Y-1])
		string += ("\n")
		string += ("~~~~~~~~~~~~~~~~~~~~~~~~")
		R.write(string)
	


def menu():
	Z=int(input("\nMain menu: \n1 ] Type 1 to open ==> GAME\n2 ] Type 2 to open ==> RECORDS\n3 ] Type 3 to open ==> CLEAR RECORDS\n4 ] Type 4 to open ==> Duplicate RECORDS\n=>"))
	
	if (Z==1):
		game()
	if(Z==2):
		records()
	if(Z==3):
		clear_records()
	if(Z==4):
		menu_dup_record()
	else:
		print("/nPlz make valid choise...")
		menu()

	

menu()
