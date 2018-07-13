from hashlib import sha256
import time
import matplotlib.pyplot as plt

#plt.rcParams['font.sans-serif']=['SimHei'] #to display chinese character
#plt.rcParams['axes.unicode_minus']=False  #to display minus sign

data = "Mike Yee".encode()
hash=sha256(data).hexdigest()
print(hash)

print(str(5).encode())

# print(sha256(data).hexdigest()) # no matter how many times you run it, the result is going to be the same 256 character string


"""
Function that tries different values of nonce to get a hash
that satisfies our difficulty criteria.
"""


Blockchain_difficulty = 4
times =[]

for difficulty in range(1,Blockchain_difficulty+1):
	nonce = 0
	data1=data+str(nonce).encode()
	computed_hash = sha256(data1).hexdigest()

	start = time.clock()
	
	while not computed_hash.startswith('0' * difficulty):
		nonce += 1
		data1=data+str(nonce).encode()
		computed_hash = sha256(data1).hexdigest()
		if nonce%1000000==0:
			print(nonce)
			print(computed_hash)

	times.append(time.clock() - start)
	print(nonce)
	#print(data1)
	print(computed_hash)


print("時間: "+str(times))
diff=[x for x in range(1,Blockchain_difficulty+1)]

plt.plot(diff,times)
plt.title("mining difficulty vs time", fontsize=24)
plt.xlabel("difficulty", fontsize=14)
plt.ylabel('time',fontsize=14)
plt.tick_params(axis='both',which='major', labelsize=14)
plt.show()



