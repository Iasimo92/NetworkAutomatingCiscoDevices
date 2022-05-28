import pexpect
import sys
print("#####################################")
print("###Starting Configuring OSPF on R1###")
print("#####################################")
child1 = pexpect.spawn('ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc 192.168.56.146 -l user')
child1.expect('Password:')
child1.sendline('pass')
child1.expect('R1>')
child1.sendline('enable')
child1.expect('Password:')
child1.sendline('pass')
child1.expect('R1#')
child1.sendline('terminal length 0')
child1.logfile=sys.stdout.buffer
child1.expect('R1#')
child1.sendline('conf t')
child1.expect('\(config\)#')
child1.sendline('router ospf 1')
child1.expect('\(config-router\)#')
child1.sendline('network 192.168.12.0 0.0.0.255 area 0')
child1.expect('\(config-router\)#')
child1.sendline('network 192.168.23.0 0.0.0.255 area 0')
child1.expect('\(config-router\)#')
child1.sendline('exit')
child1.close()
print("#####################################")
print("####End of Configuring OSPF on R1####")
print("#####################################")

print("#####################################")
print("###Starting Configuring OSPF on R4###")
print("#####################################")
child2 = pexpect.spawn('ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc 192.168.56.152 -l user')
child2.expect('Password:')
child2.sendline('pass')
child2.expect('R4>')
child2.sendline('enable')
child2.expect('Password:')
child2.sendline('pass')
child2.expect('R4#')
child2.sendline('terminal length 0')
child2.logfile=sys.stdout.buffer
child2.expect('R4#')
child2.sendline('configure terminal')
child2.expect('\(config\)#')
child2.sendline('router ospf 1')
child2.expect('\(config-router\)#')
child2.sendline('network 192.168.12.0 0.0.0.255 area 0')
child2.expect('\(config-router\)#')
child2.sendline('network 192.168.13.0 0.0.0.255 area 0')
child2.expect('\(config-router\)#')
child2.sendline('exit')
child2.close()
print("#####################################")
print("####End of Configuring OSPF on R4####")
print("#####################################")

print("#####################################")
print("###Starting Configuring OSPF on R5###")
print("#####################################")
child3 = pexpect.spawn('ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc 192.168.56.153 -l user')
child3.expect('Password:')
child3.sendline('pass')
child3.expect('R5>')
child3.sendline('enable')
child3.expect('Password:')
child3.sendline('pass')
child3.expect('R5#')
child3.sendline('terminal length 0')
child3.logfile=sys.stdout.buffer
child3.expect('R5#')
child3.sendline('configure terminal')
child3.expect('\(config\)#')
child3.sendline('router ospf 1')
child3.expect('\(config-router\)#')
child3.sendline('network 192.168.13.0 0.0.0.255 area 0')
child3.expect('\(config-router\)#')
child3.sendline('network 192.168.23.0 0.0.0.255 area 0')
child3.expect('\(config-router\)#')
child3.sendline('exit')
child3.close()
print("#####################################")
print("####End of Configuring OSPF on R5####")
print("#####################################")
