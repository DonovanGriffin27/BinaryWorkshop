#Introduction
##Bad Seed Vulnerabilities
**Bad seed vulnerabilities** are **weaknesses** that come from **malicous** or compromised prelimary data or settings.
###Why they are bad
-Data Breaches
-DoS Attacks
-Atlered Data
-Unathorized personel has access to a system
-Depletes the level of trustworthines of a system
###Real Life Examples
A team of European and American mathematicians and cryptographers have discovered an unexpected weakness in the encryption system widely used worldwide for online shopping, banking, e-mail and other Internet services intended to remain private and secure.Generation of a regular RSA modulus consists of finding two random prime numbers. This must be done in such a way that these primes were not selected by anyone else before. The probability not to regenerate a prime is commensurate with the security level if NIST’s recommendation is followed to use a random seed of bit-length twice the intended security level. Clearly, this recommendation is not always followed.Irrespective of the way primes are selected (additive/sieving methods or methods using fresh random bits for each attempted prime selection), a variety of obvious scenarios is conceivable where poor initial seeding may lead to mishaps, with duplicate keys a consequence if no “fresh” local entropy is used at all. If the latter is used, the outcome may be worse. - New York Times, John Markoff

Netscape Communications has been at the forefront of the effort to integrate cryptographic techniques into Web servers and browsers. Netscape's Web browser supports the Secure Sockets Layer (SSL), a cryptographic protocol developed by Netscape to provide secure Internet transactions. Given the popularity of Netscape's browser and the widespread use of its cryptographic protocol on the Internet, we decided to study Netscape's SSL implementation in detail.

###The key-generation algorithm, also reverse-engineered from Netscape's browser. An attacker who can guess the PRNG seed value can easily determine the encryption keys used in Netscape's secure transactions.

'''
RNG_GenerateRandomBytes()
     x = MD5(seed);
     seed = seed + 1;
     return x;
 
 global variable challenge, secret_key;
 
 create_key()
     RNG_CreateContext();
     tmp = RNG_GenerateRandomBytes();
     tmp = RNG_GenerateRandomBytes();
     challenge = RNG_GenerateRandomBytes(); 
     secret_key = RNG_GenerateRandomBytes();
'''
Unfortunately for Netscape, U.S. regulations prohibit the export of products incorporating strong cryptography. In order to distribute an international version of its browser overseas, Netscape had to weaken the encryption scheme to use keys of just 40 bits, leaving only a million million possible key values. That may sound like a lot of numbers to try, but several people (David Byers, Eric Young, Damien Doligez, Piete Brooks, Andrew Roos, Adam Back, Andy Brown and many others) have been able to try every possible key and recover SSL- encrypted data in as few as 30 hours using spare CPU cycles from many machines. Since nearly all Netscape browsers in use are the free international version, the success of this attack demonstrates a fundamental vulnerability in Netscape that cannot be repaired under current export regulations.

#Approach
Based on what was shown in Ghidra, the time program uses CALL to get the time, seed, and generate a ranodm number. MOV to store the information.
The time program itself: 
1. Generates a random number from the current time.
2. Prompts the user to enter a number.
3. Runs a conditional statement to check if the user's guess (input) equals the random generated number.
4. Displays a conditional message based on if the user's guess was correct ot not.

##Solution
A solution must include that a different random number is generated each time. Which would mean the code will need ot be modidified. 
This can be acchieved by:
-import random
-import time
-create a "main" function
-implement a calculation that gives a random number range
