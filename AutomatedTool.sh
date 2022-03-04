#!/bin/bash

echo "(+) Enter Domain / IP Address (+)"

read domain

if [ ! -d "$domain" ]; then
	mkdir $domain
	else
		echo "Try Other Domain"
		exit
fi

if [ -d "$domain" ]; then
	cd $domain
	echo "(*) Scanning ports (*)"
	nmap -sS -sC -O -p- $domain > nmap.txt
	cat nmap.txt
	echo "(*) Enter Host (*)"
	read host
	echo "(*) Scanning for directories (*)"
	gobuster dir -u $host -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt > gobuster.txt; grep 'Status:' gobuster.txt #| grep '^found' > gobuster.txt
	
fi
