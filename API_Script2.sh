#!/bin/bash

python3 API_to_find_IP_addresses.py | grep up > mylog3.txt
awk '{print $2}' mylog3.txt > mylog4.txt
var=$(wc -l mylog4.txt | awk '{print $1}')
echo "##############CHECKING#############################"
echo  ${var} "Ip addresses are configured in your device" 
echo "##############CHECK ENDS###########################"
