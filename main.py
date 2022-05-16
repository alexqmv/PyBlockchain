import hashlib #importing hashlib library

class Networkus: # Main Class

	def __init__(self, previous_block_hash,transaction_list): #initiliazing 
		self.previous_block_hash = previous_block_hash #block hash
		self.transaction_list = transaction_list #transaction list

		self.block_data = "-".join(transaction_list) + "-" + previous_block_hash #random hash symbols
		self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Anna sends 2 NTW to Mike"                # Transaction 1 [Using]
t2 = "Mike sends 2.1 NTW to George"		       # Transaction 2 [Using]
t3 = "Daniel sends 2 NTW to Mike"
t4 = "Charlie sends 2 NTW to Mike"
t5 = "Kali sends 2 NTW to Mike"
t6 = "Charlie sends 2 NTW to Mike"
t7 = "Zosie sends 2 NTW to Mike"
t8 = "Stasy sends 2 NTW to Mike"

initial_block = Networkus(" NetworkusChain", [t1,t2]) #initial block where we use transaction1 and transaction2
print(initial_block.block_data) # just printing this block
print("Transaction ->", initial_block.block_hash) # there too

