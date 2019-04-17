# ROT13 Cipher Encoding and Decoding.

# Encoding 

def encode(string,key):
	
	encoded_string = ''
	for i in string:
		if ord(i)>=ord('A') and ord(i)<=ord('Z'):
			if ord(i)+key>ord('Z'):
				encoded_string+=chr(ord('A')+ord(i)+key-ord('Z')-1)
			else:
				encoded_string+=chr(ord(i)+key)
		elif ord(i)>=ord('a') and ord(i)<=ord('z'):
			if ord(i)+key>ord('z'):
				encoded_string+=chr(ord('a')+ord(i)+key-ord('z')-1)
			else:
				encoded_string+=chr(ord(i)+key)
		else:
			encoded_string+=i
	print('\nThe encoded string is:- \n\n{}\n'.format(encoded_string))

# Decoding

def decode(string,key):
	
	decoded_string = ''
	for i in string:
		if ord(i)>=ord('A') and ord(i)<=ord('Z'):
			if ord(i)-key<ord('A'):
				decoded_string+=chr(ord('Z')-key+ord(i)-ord('A')+1)
			else:
				decoded_string+=chr(ord(i)-key)
		elif ord(i)>=ord('a') and ord(i)<=ord('z'):
			if ord(i)-key<ord('a'):
				decoded_string+=chr(ord('z')-key+ord(i)-ord('a')+1)
			else:
				decoded_string+=chr(ord(i)-key)
		else:
			decoded_string+=i
	print('\nThe decoded string is:- \n\n{}\n'.format(decoded_string))

#Driver Code

query = input('\nEnter encode for encoding and decode for decoding.\n\n')

if query == 'encode':
	string = input('\nEnter string.\n\n')
	key = 13
	encode(string,key)

elif query == 'decode':
	string = input('\nEnter string.\n\n')
	key = 13
	decode(string,key)

else:
	print('Please try again.')