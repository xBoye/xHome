# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import sys, hashlib, random

DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

def cipher(request):
	"""密码学"""
	return render(request, 'cipher/cipher.html')

def makersakeys11(request):
	"""密码生成"""
	context = {'publicKey':'publicKey', 'privateKey':'privateKey'}
	return render(request, 'cipher/makersakeys.html', context)

def gcd(a, b):
	# Return the GCD of a and b using Euclid's Algorithm
	while a != 0:
		a, b = b % a, a
	return b


def findModInverse(a, m):
	# Returns the modular inverse of a % m, which is
	# the number x such that a*x % m = 1

	if gcd(a, m) != 1:
		return None # no mod inverse if a & m aren't relatively prime

	# Calculate using the Extended Euclidean Algorithm:
	u1, u2, u3 = 1, 0, a
	v1, v2, v3 = 0, 1, m
	while v3 != 0:
		q = u3 // v3 # // is the integer division operator
		v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
	return u1 % m
	
def rabinMiller(num):
	# Returns True if num is a prime number.

	s = num - 1
	t = 0
	while s % 2 == 0:
		# keep halving s until it is even (and use t
		# to count how many times we halve s)
		s = s // 2
		t += 1

	for trials in range(5): # try to falsify num's primality 5 times
		a = random.randrange(2, num - 1)
		v = pow(a, s, num)
		if v != 1: # this test does not apply if v is 1.
			i = 0
			while v != (num - 1):
				if i == t - 1:
					return False
				else:
					i = i + 1
					v = (v ** 2) % num
	return True	
	
def isPrime(num):
	# Return True if num is a prime number. This function does a quicker
	# prime number check before calling rabinMiller().

	if (num < 2):
		return False # 0, 1, and negative numbers are not prime

	# About 1/3 of the time we can quickly determine if num is not prime
	# by dividing by the first few dozen prime numbers. This is quicker
	# than rabinMiller(), but unlike rabinMiller() is not guaranteed to
	# prove that a number is prime.
	lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

	if num in lowPrimes:
		return True

	# See if any of the low prime numbers can divide num
	for prime in lowPrimes:
		if (num % prime == 0):
			return False

	# If all else fails, call rabinMiller() to determine if num is a prime.
	return rabinMiller(num)
	
	
def generateLargePrime(keysize=1024):
	# Return a random prime number of keysize bits in size.
	while True:
		num = random.randrange(2**(keysize-1), 2**(keysize))
		if isPrime(num):
			return num

def makersakeys(request,keySize=1024):
	
	# Creates a public/private key pair with keys that are keySize bits in
	# size. This function may take a while to run.

	# Step 1: Create two prime numbers, p and q. Calculate n = p * q.
	print('Generating p prime...')
	p = generateLargePrime(keySize)
	print('Generating q prime...')
	q = generateLargePrime(keySize)
	n = p * q

	# Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
	print('Generating e that is relatively prime to (p-1)*(q-1)...')
	while True:
		# Keep trying random numbers for e until one is valid.
		e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
		if gcd(e, (p - 1) * (q - 1)) == 1:
			break

	# Step 3: Calculate d, the mod inverse of e.
	print('Calculating d that is mod inverse of e...')
	d = findModInverse(e, (p - 1) * (q - 1))

	publicKey = (n, e)
	privateKey = (n, d)

	print('Public key:', publicKey)
	print('Private key:', privateKey)
	
	context = {'publicKey':publicKey, 'privateKey':privateKey}
	return render(request, 'cipher/makersakeys.html', context)

	
def message_digest(request):
	"""消息摘要"""
	import hashlib
	msg = '修心未到无心地，万种千般逐水流^-^'
	if request.method=='POST':
		msg = request.POST['msg']
	sha256=hashlib.sha256()
	sha256.update(msg.encode('utf-8'))
	md = sha256.hexdigest()
	message = '消息：【' + msg +'】'
	message_digest = '【SHA256消息摘要】：' + md
	
	context = {'message':message,'message_digest':message_digest}
	return render(request, 'cipher/message_digest.html', context)
	
def digital_signature(request):
	msg = '况有南窗姬易在，此心那更起纤尘^-^'
	if request.method=='POST':
		msg = request.POST['msg']
	sha256=hashlib.sha256()
	sha256.update(msg.encode('utf-8'))
	md = sha256.hexdigest()
	message_digest = '消息摘要(sha256)：' + md

	# Runs a test that encrypts a message to a file or decrypts a message
	# from a file.
	filename = 'encrypted_file.txt' # the file to write to/read from
	mode = 'encrypt' # set to 'encrypt' or 'decrypt'

	#if mode == 'encrypt':
	message = md
	pubKeyFilename = 'D:\\xHome\\data\\cipher\\al_sweigart_privkey.txt'
	print('Encrypting and writing to %s...' % (filename))
	encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)

	print('Encrypted text:')
	print(encryptedText)
	digital_signature = '数字签名：' + encryptedText

	#elif mode == 'decrypt':
	privKeyFilename = 'D:\\xHome\\data\\cipher\\al_sweigart_pubkey.txt'
	print('Reading from %s and decrypting...' % (filename))
	decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)

	print('Decrypted text:')
	print(decryptedText)
	verify_signature = '签名验证：' + decryptedText

	message = '消息：【' + msg + '】'
	context = {'message':message, 'message_digest':message_digest, 'digital_signature':digital_signature, 'verify_signature':verify_signature}
	return render(request, 'cipher/digital_signature.html', context)
	
def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
	# Converts a string message to a list of block integers. Each integer
	# represents 128 (or whatever blockSize is set to) string characters.

	messageBytes = message.encode('ascii') # convert the string to bytes

	blockInts = []
	for blockStart in range(0, len(messageBytes), blockSize):
		# Calculate the block integer for this block of text
		blockInt = 0
		for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
			blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
		blockInts.append(blockInt)
	return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
	# Converts a list of block integers to the original message string.
	# The original message length is needed to properly convert the last
	# block integer.
	message = []
	for blockInt in blockInts:
		blockMessage = []
		for i in range(blockSize - 1, -1, -1):
			if len(message) + i < messageLength:
				# Decode the message string for the 128 (or whatever
				# blockSize is set to) characters from this block integer.
				asciiNumber = blockInt // (BYTE_SIZE ** i)
				blockInt = blockInt % (BYTE_SIZE ** i)
				blockMessage.insert(0, chr(asciiNumber))
		message.extend(blockMessage)
	return ''.join(message)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
	# Converts the message string into a list of block integers, and then
	# encrypts each block integer. Pass the PUBLIC key to encrypt.
	encryptedBlocks = []
	n, e = key

	for block in getBlocksFromText(message, blockSize):
		# ciphertext = plaintext ^ e mod n
		encryptedBlocks.append(pow(block, e, n))
	return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
	# Decrypts a list of encrypted block ints into the original message
	# string. The original message length is required to properly decrypt
	# the last block. Be sure to pass the PRIVATE key to decrypt.
	decryptedBlocks = []
	n, d = key
	for block in encryptedBlocks:
		# plaintext = ciphertext ^ d mod n
		decryptedBlocks.append(pow(block, d, n))
	return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
	# Given the filename of a file that contains a public or private key,
	# return the key as a (n,e) or (n,d) tuple value.
	fo = open(keyFilename)
	content = fo.read()
	fo.close()
	keySize, n, EorD = content.split(',')
	return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
	# Using a key from a key file, encrypt the message and save it to a
	# file. Returns the encrypted message string.
	keySize, n, e = readKeyFile(keyFilename)

	# Check that key size is greater than block size.
	if keySize < blockSize * 8: # * 8 to convert bytes to bits
		sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys.' % (blockSize * 8, keySize))


	# Encrypt the message
	encryptedBlocks = encryptMessage(message, (n, e), blockSize)

	# Convert the large int values to one string value.
	for i in range(len(encryptedBlocks)):
		encryptedBlocks[i] = str(encryptedBlocks[i])
	encryptedContent = ','.join(encryptedBlocks)

	# Write out the encrypted string to the output file.
	encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
	fo = open(messageFilename, 'w')
	fo.write(encryptedContent)
	fo.close()
	# Also return the encrypted string.
	return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
	# Using a key from a key file, read an encrypted message from a file
	# and then decrypt it. Returns the decrypted message string.
	keySize, n, d = readKeyFile(keyFilename)


	# Read in the message length and the encrypted message from the file.
	fo = open(messageFilename)
	content = fo.read()
	messageLength, blockSize, encryptedMessage = content.split('_')
	messageLength = int(messageLength)
	blockSize = int(blockSize)

	# Check that key size is greater than block size.
	if keySize < blockSize * 8: # * 8 to convert bytes to bits
		sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

	# Convert the encrypted message into large int values.
	encryptedBlocks = []
	for block in encryptedMessage.split(','):
		encryptedBlocks.append(int(block))

	# Decrypt the large int values.
	return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)
