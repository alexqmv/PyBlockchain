import hashlib #importing hashlib library
import time

class Networkus_Blockchain: # Main Class

	def __init__(self, previous_block_hash,transaction_list): #initiliazing 
		self.previous_block_hash = previous_block_hash #block hash
		self.transaction_list = transaction_list #transaction list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash #random hash symbols
		self.block_hash = hashlib.md5(self.block_data.encode()).hexdigest()

class Networkus_Blockchain2:
	def __init__(self, pprevious_block_hash,ttransaction_list): #initiliazing 
		self.pprevious_block_hash = pprevious_block_hash #block hash
		self.ttransaction_list = ttransaction_list #transaction list

		self.bblock_data = "-".join(ttransaction_list) + "-" + pprevious_block_hash #random hash symbols
		self.bblock_hash = hashlib.md5(self.bblock_data.encode()).hexdigest()


t1 = "qumara99@icloud.com"                # Transaction 1 [Using]
t2 = "ilovedogs2000"		       # Transaction 2 [Using]


print("~----------------HASH GENERATOR----------------~")
time.sleep(2)

initial_block = Networkus_Blockchain(" NetworkusChain", [t1]) #initial block where we use transaction1 and transaction2
print(initial_block.block_data) # just printing this block
print("Generated hash login ->> ", initial_block.block_hash)
print("-----------------------------------------------")

iinitial_block = Networkus_Blockchain2(" NetworkusBlockchain", [t2]) #initial block where we use transaction1 and transaction2
print(iinitial_block.bblock_data) # just printing this bloc
print("Generated hash password ->> ", iinitial_block.bblock_hash) # there too


print("-----------------------------------------------")
