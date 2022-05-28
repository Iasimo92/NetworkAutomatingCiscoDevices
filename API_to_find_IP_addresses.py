import pexpect
import sys
child = pexpect.spawn('ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc 192.168.56.146 -l iasonas')
child.expect('Password:')
child.sendline('ericsson')
child.expect('R1>')
child.sendline('enable')
child.expect('Password:')
child.sendline('ericsson')
child.expect('R1#')
child.sendline('terminal length 0')
child.logfile=sys.stdout.buffer
child.expect('R1#')
child.sendline('show ip interface brief')
child.expect('R1#')
child.sendline('show cdp neighbors detail')
child.expect('R1#')
