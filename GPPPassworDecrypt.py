
import sys
from Crypto.Cipher import AES
from base64 import b64decode

if(len(sys.argv) != 2):
  print ("Usage: gpprefdecrypt.py <cpassword>")
  sys.exit(0)

# Init the key
# From MSDN: http://msdn.microsoft.com/en-us/library/2c15cbf0-f086-4c74-8b70-1f2fa45dd4be%28v=PROT.13%29#endNote2
key = "4e 99 06 e8  fc b6 6c c9  fa f4 93 10  62 0f fe e8 f4 96 e8 06  cc 05 79 90  20 9b 09 a4  33 b6 6c 1b".split(" ")
key = "".join(key)
import binascii
key = binascii.unhexlify(key)




# Add padding to the base64 string and decode it
cpassword = sys.argv[1]
cpassword += "=" * ((4 - len(sys.argv[1]) % 4) % 4)
password = b64decode(cpassword)

# Decrypt the password
o = AES.new(key, AES.MODE_CBC, "\x00" * 16).decrypt(password)
_len = o[-1]+1
print(_len)

pwd = o.decode('utf16')

print(pwd[:_len])

#print(repr(o))
# Print it
#print(o[:-ord(o[-1])].decode('utf16'))