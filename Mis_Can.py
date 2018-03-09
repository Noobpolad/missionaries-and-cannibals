class Coast:

	def __init__(self,m,k):
		self.next_coast = None
		self.mis = m
		self.can = k
		self.side = 'E' #Stands for East ;)

	def Eaten(self):
		if self.mis < self.can and self.mis > 0:
			return True
		return False		

	#If the side is W and all troops are there, then success.	

	def Success(self):
		if self.side == 'W' and self.can == 3 and self.mis == 3:
			return True	
		return False	

#Value is the we pass the next coast and IONo is the command must be ignored on the next iteration, to avoid the infinite recursion.			

def Solution(value,ignore_operationNo):
	cur = value

	#If the first iteration create a new West-coast with the parameters can -> 0 mis -> 0 side -> W and next -> current coast

	if cur.next_coast == None:
		cur.next_coast = Coast(0,0)
		cur.next_coast.next_coast = cur
		cur.next_coast.side = 'W'

	if cur.Eaten() or cur.next_coast.Eaten():
		return False

	print('The coast:{}\nNumber of mis:{}\nNumber of can:{}\n'.format(cur.side,cur.mis,cur.can))	

	if cur.Success():
		return True

	#The first operation. Send one mis to next coast, if on Num of mis on cur coast is > 0 and the we are not repeating the same action twice.
	#After sending Use the recursion. If its True, return True. Else, return troops to the previous condition.  

	if cur.mis > 0 and ignore_operationNo != 1:
		cur.mis -= 1
		cur.next_coast.mis += 1
		if Solution(cur.next_coast,1):
			return True
		cur.mis += 1
		cur.next_coast.mis -= 1

	#The second operation. Send one can to next coast, if on Num of can on cur coast is > 0 and the we are not repeating the same action twice.
	#After sending Use the recursion. If its True, return True. Else, return troops to the previous condition.	

	if cur.can > 0 and ignore_operationNo != 2:
		cur.can -= 1
		cur.next_coast.can += 1
		if Solution(cur.next_coast,2):
			return True
		cur.can += 1
		cur.next_coast.can -= 1	

	#The third operation. Send two mis to next coast, if on Num of mis on cur coast is > 1 and the we are not repeating the same action twice.
	#After sending Use the recursion. If its True, return True. Else, return troops to the previous condition.	

	if cur.mis > 1 and ignore_operationNo != 3:
		cur.mis -= 2
		cur.next_coast.mis += 2
		if Solution(cur.next_coast,3):
			return True
		cur.mis += 2
		cur.next_coast.mis -= 2	

	#The fourth operation. Send two can to next coast, if on Num of can on cur coast is > 1 and the we are not repeating the same action twice.
	#After sending Use the recursion. If its True, return True. Else, return troops to the previous condition.	
		
	if cur.can > 1 and ignore_operationNo != 4:
		cur.can -= 2
		cur.next_coast.can += 2
		if Solution(cur.next_coast,4):
			return True
		cur.can += 2
		cur.next_coast.can -= 2

	#The Fifth operation send one can and one mis to next coast, if its possible.
	#After sending Use the recursion. If its True, return True. Else, return troops to the previous condition.	

	if (cur.can > 1 and cur.mis > 1 and cur.side == 'W' and ignore_operationNo != 5 ) or (cur.can == 1 and cur.mis == 1 and cur.side == 'E' and ignore_operationNo != 5 ):
		cur.can -= 1
		cur.next_coast.can += 1
		cur.mis -= 1
		cur.next_coast.mis += 1
		if Solution(cur.next_coast,5):
			return True
		cur.mis += 1
		cur.next_coast.mis -= 1	
		cur.can += 1
		cur.next_coast.can -= 1								

print(Solution(Coast(3,3),0))