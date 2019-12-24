from random import randint
import time
from collections import deque

def randomInput(clock_type):
    randomClock=0
    counter=0
    if (clock_type=="session_key"):
        randomClock = randint(0, (2**65)-1)
        randomClock = "{0:{fill}64b}".format(randomClock, fill='0')
    elif (clock_type=="frame_counter"):
        randomClock = randint(0,(2**23)-1)
        randomClock = "{0:{fill}22b}".format(randomClock, fill='0')
    else:
        print ("Akses ditolak!")
        
    return randomClock

def tappedBit(shift_register):
    result = []
    if(shift_register=="lfsr1"):
        result = [13,16,17,18]
    elif (shift_register=="lfsr2"):
        result = [20,21]
    elif (shift_register=="lfsr3"):
        result = [7,20,21,22]
    else:
        print ("Access Denied!")
    return result

def clocking(lfsr,tapped_bit,key):
    lfsr = deque(lfsr)
    for num in range(0,len(key)):
        if len(tapped_bit)==4:
            resultXorLfsr = ((int(lfsr[tapped_bit[3]])) ^ int(lfsr[tapped_bit[2]]))
        else:
            resultXorLfsr = int(lfsr[tapped_bit[1]]) ^ int(lfsr[tapped_bit[0]])

        resultFinal = int(key[num]) ^ resultXorLfsr
        lfsr.rotate(1)
        lfsr[0] = str(resultFinal)
        # Validation Item
        # print "loop-"+str(num)
        # result = ''.join(lfsr)
        # print result
    return lfsr

# Main Program

lfsr1 = "{0:{fill}19b}".format(0, fill='0')   #19bit
lfsr2 = "{0:{fill}22b}".format(0, fill='0')   #22bit
lfsr3 = "{0:{fill}23b}".format(0, fill='0')   #23bit

print ("\n Algoritma Kriptografi A5\1 \n")

# Inisialisasi LFSR
print ("Inisiasi LFSR...\n")
time.sleep(1)
print (lfsr1)
print (lfsr2)
print (lfsr3)

# Generating Tapped Bit
print ("\nMenghasilkan bit yang disadap...\n")
time.sleep(3)
print ("LFSR 1 : "+str(tappedBit("lfsr1")))
print ("LFSR 2 : "+str(tappedBit("lfsr2")))
print ("LFSR 3 : "+str(tappedBit("lfsr3")))
print ("\nStep 1\n")

# Input Plaintext
plainText = input("Silahkan masukkan plaintext anda : ")
print ("Yang anda masukan : "+plainText)
plainText = ''.join(format(ord(x), 'b') for x in plainText)
plainText = list(plainText)

# Pembuatan Session Key Secara Random
print ("\nMembuat Session Key...\n")
time.sleep(3)
sessionKey = randomInput("session_key")
print ("Session Key dibuat : "+str(sessionKey)+" \n")
sessionKey = deque(sessionKey)

#XOR-ing session key dengan lfsr menggunakan tapped bit
print ("XOR-ing antara kunsi sesi dan LFSR denga bit yang disadap\n")
time.sleep(3)
lfsr1 = clocking(lfsr1, tappedBit("lfsr1"), sessionKey)
print ("Hasil XOR pada LFSR 1 : "+''.join(lfsr1))
time.sleep(1)
lfsr2 = clocking(lfsr2, tappedBit("lfsr2"), sessionKey)
print ("Hasil XOR pada LFSR 2 : "+''.join(lfsr2))
time.sleep(1)
lfsr3 = clocking(lfsr3, tappedBit("lfsr3"), sessionKey)
print ("Hasil XOR pada LFSR 3 : "+''.join(lfsr3))
time.sleep(3)
print ("\nStep 2\n")

# Pembuatan frame counter secara random
print ("Membuat bingkai penghitung...\n")
time.sleep(1)
frameCounter = randomInput("frame_counter")
print ("Bingkai penghitung dibuat : "+frameCounter+" \n")
frameCounter = deque (frameCounter)

#XOR-ing frame counter dengan lfsr pada step 1 menggunakan tapped bit
print ("XOR-ing antara bingkai penghitung dan LFSR denga bit yang disadap\n")
time.sleep(3)
lfsr1 = clocking (lfsr1, tappedBit("lfsr1"), frameCounter)
print ("Hasil XOR pada LFSR 1 : "+''.join(lfsr1))
time.sleep(1)
lfsr2 = clocking (lfsr2, tappedBit("lfsr2"), frameCounter)
print ("Hasil XOR pada LFSR 2 : "+''.join(lfsr2))
time.sleep(1)
lfsr3 = clocking (lfsr3, tappedBit("lfsr3"), frameCounter)
print ("Hasil XOR pada LFSR 3 : "+''.join(lfsr3))
time.sleep(3)
print ("\nStep 3\n")

# Penggunaan lfsr 100 kali irregular clock menggunakan majority bit
majority = "0"
majorityKey = [1]
counterZero = 0
counterOne = 0

# Checking majority bit dan loop irregular clock
print ("Irregular clocking of LFSR with majority bit\n")
for num in range (0,99):
    if (lfsr1[8]==majority):
        counterZero = counterZero + 1
    else :
        counterOne = counterOne + 1
    if (lfsr2[10]==majority):
        counterZero = counterZero + 1
    else :
        counterOne = counterOne + 1
    if (lfsr3[10]==majority):
        counterZero = counterZero + 1
    else :
        counterOne = counterOne + 1
    if (counterZero > counterOne):
        if (lfsr1[8]==majority):
            lfsr1 = clocking(lfsr1, tappedBit("lfsr1"), majorityKey)
        if (lfsr2[10]==majority):
            lfsr2 = clocking(lfsr2, tappedBit("lfsr2"), majorityKey)
        if (lfsr3[10]==majority):
            lfsr3 = clocking(lfsr3, tappedBit("lfsr3"), majorityKey)
    else :
        if (lfsr1[8]==majority):
            lfsr1 = clocking(lfsr1, tappedBit("lfsr1"), majorityKey)
        if (lfsr2[10]==majority):
            lfsr2 = clocking(lfsr2, tappedBit("lfsr2"), majorityKey)
        if (lfsr3[10]==majority):
            lfsr3 = clocking(lfsr3, tappedBit("lfsr3"), majorityKey)

time.sleep(3)
lfsr1 = clocking (lfsr1, tappedBit("lfsr1"), frameCounter)
print ("Irregular clocking result on lfsr 1 : "+''.join(lfsr1))
time.sleep(1)
lfsr2 = clocking (lfsr2, tappedBit("lfsr2"), frameCounter)
print ("Irregular clocking result on lfsr 2 : "+''.join(lfsr2))
time.sleep(1)
lfsr3 = clocking (lfsr3, tappedBit("lfsr3"), frameCounter)
print ("Irregular clocking result on lfsr 3 : "+''.join(lfsr3))
time.sleep(3)
print ("\nStep 4\n")

#Checking majority bit dan loop irregular clock part 2 + creating key stream
print ("Irregular clocking of LFSR (part2) with majority bit\n")
keyStream = ""

for num in range(0,227):
    counterZero = 0
    counterOne = 0

    if (lfsr1[8]==majority):
        counterZero = counterZero + 1
    else:
        counterOne = counterOne + 1
    if (lfsr2[10]==majority):
        counterZero = counterZero + 1
    else:
        counterOne = counterOne + 1
    if (lfsr3[10]==majority):
        counterZero = counterZero + 1
    else:
        counterOne = counterOne + 1

    temp = int(lfsr1[len(lfsr1)-1]) ^ int(lfsr2[len(lfsr2)-1]) ^ int(lfsr3[len(lfsr3)-1])
    keyStream = keyStream + str(temp)

    if(counterZero > counterOne):
        if (lfsr1[8]==majority):
            lfsr1 = clocking(lfsr1, tappedBit("lfsr1"), majorityKey)
        if (lfsr2[10]==majority):
            lfsr2 = clocking(lfsr2, tappedBit("lfsr2"), majorityKey)
        if (lfsr3[10]==majority):
            lfsr3 = clocking(lfsr3, tappedBit("lfsr3"), majorityKey)
time.sleep(3)
lfsr1 = clocking(lfsr1, tappedBit("lfsr1"), frameCounter)
print ("Irregular clocking (part 2) result on lfsr 1 : "+''.join(lfsr1))
time.sleep(1)
lfsr2 = clocking(lfsr2, tappedBit("lfsr2"), frameCounter)
print ("Irregular clocking (part 2) result on lfsr 2 : "+''.join(lfsr2))
time.sleep(1)
lfsr3 = clocking(lfsr3, tappedBit("lfsr3"), frameCounter)
print ("Irregular clocking (part 2) result on lfsr 3 : "+''.join(lfsr3))
print ("\nKey Stream : "+keyStream)
keyStream = list(keyStream)
print ("\nPlain Text : "+''.join(plainText))
time.sleep(3)
print ("\nFinal Step\n")

# Checking majority bit dan loop irregular clock part 2 + creating key stream
print  ("XOR-ing between Key Stream and Plain Text\n")
counter_loop= 0
controlLoop = False
chiperText = ""

if (len(keyStream) > len (plainText)):
    counterLoop = len (plainText)
    startIndexLower = len (keyStream) - counterLoop
    controlLoop = False
else :
     counterLoop = len (plainText)
     startIndexLower = len (keyStream) - counterLoop
     controlLoop = True

time.sleep(3)
for num in range (0,counterLoop-1):
    if (controlLoop):
        temp = int(plainText[startIndexLower]) ^ int(plainText[num])
    else:
        temp = int(keyStream[num]) ^ int(keyStream[startIndexLower])
    chiperText = chiperText + str(temp)

if (controlLoop):
    temp = plainText[0:startIndexLower]
else:
    temp = keyStream[0:startIndexLower]

time.sleep(3)
temp = ''.join(temp)
chiperText = temp +  chiperText
print ("Chipper  Text : "+chiperText)
print ("\n")

            

    
    
            
        
                              
                              
                


        
