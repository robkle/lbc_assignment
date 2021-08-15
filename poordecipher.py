# A function to decrypt a string encrypted by the following function:
#	def poorcipher(text):
#		import base64
#		xorred = ''.join(chr(ord(k) ^ 15) for k in text)
#		return base64.encodebytes(xorred.encode())

def poordecipher(encryption):
	import base64
	decoded = base64.decodebytes(encryption.encode())
	return ''.join(chr(ord(k) ^ 15) for k in str(decoded.decode()))

# poordecipher("S2Bjf2dmYXwvZ255ai9uL2hgYGsvfGphfGovYGkvZ3piYH0h") returns:
# 'Dolphins have a good sense of humor.'
