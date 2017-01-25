# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

import sys
import hashlib

DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

def cipher(request):
	"""密码学"""
	return render(request, 'cipher/cipher.html')	
	
def message_digest(request):
	"""消息摘要"""
	import hashlib
	msg = 'helle world!'
	if request.method=='POST':
		msg = request.POST['msg']
	sha256=hashlib.sha256()
	sha256.update(msg.encode('utf-8'))
	md = sha256.hexdigest()
	message = '消息：【' + msg +'】'
	message_digest = 'sha256散列值：' + md
	
	context = {'message':message,'message_digest':message_digest}
	return render(request, 'cipher/message_digest.html', context)
	
def digital_signature(request):
	msg = 'helle world!'
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
