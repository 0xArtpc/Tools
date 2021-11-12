#!/usr/bin/env python

import subprocess #Permite utilizar os comandos do Sistema Operativo
import optparse
import re

def get_args ():
    parser = optparse.OptionParser() #Quando tem letra maiuscula significa que é uma classe
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC") #dest serve para ler a variavel
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args() # Valores introduzidos pelo utilizador
    if not options.interface:
        #Código para o erro
        parser.error ("[-] Please specify a interface, use --help for more information")
    elif not options.new_mac:
        #Código para o erro
        parser.error ("[-] Please specify new a mac address, use --help for more information")
    return options #returnar os valores pq nao sao variaveis globais


def change_mac (interface, new_mac):
    #print ("\n{+} Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call("ifconfig " + interface +" down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def get_current_mac(interface):
    ifconfig_res = subprocess.check_output(["ifconfig", interface]) #Dar output ao ifconfig com eth0
    mac_address_res = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_res) #b reads regex code

    if mac_address_res:
        return mac_address_res.group(0)
    else:
        print ("[-] Dont has any Mac address")

options = get_args() #chamar a função com o return anterior
current_mac = get_current_mac(options.interface) #tem a variavel current_mac por causa do return l. 32

current_mac_decoded = current_mac.decode("utf-8")

print ("[+] Current Mac " + str(current_mac_decoded) + "\n")
change_mac (options.interface, options.new_mac)


if current_mac_decoded != options.new_mac:
    print ("[+] Mac address changed from " + current_mac_decoded + " to " + options.new_mac)
else:
    print ("Your Mac address was not changed, try again.")

print ("\n[+] Current Mac " + str(options.new_mac))
