#!/bin/bash

python3 API_to_find_IP_addresses.py  | grep up | awk '{print $2}' | head -n 3 > mylog3.txt
python3 API_to_find_IP_addresses.py | grep "IP address" > mylog5.txt


head -n 1 mylog5.txt>mylog4.txt
tail -n 1 mylog5.txt>>mylog4.txt
cat mylog4.txt | awk '{print $3}'>mylog6.txt
cat mylog6.txt

