#!/usr/bin/python
# -*- coding: utf-8 -*-
# HARGAI PEMBUAT AJG CAPE GOBLOK
# Validator Hp
import sys
import requests
import json
import urllib
import time
import os


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'


class config:
    key = "49dfc70ef3d99728f9a2e97a63a8fc1d"  # go to https://numverify.com/


def banner():
    os.system('cls')
    print(color.PURPLE + """
,                
                                                                                              &@@@&&               
                                                                                           ,@&@&%@@@               
                                                                                         *&@%/##(/&@,              
                                                                                        %#((((**#%#@&              
                                                                                      %/((/(/*//((%%%              
                                                                                    /*(///(//(//*//(##*            
                  %&&&                                                            ,,(/*////#*/**//**,/@            
                   &@@#%@&*                                                      .,**//*/(///*//*,,/,/             
                     ##*//./%&#                                                .,,*/******//**,***.(/              
                      .,,/**,*,/**(#                                          ,..***(*****/*****,//#               
                        .,*,/*****,./*,*/                                    .*,*/**,***/****,*/(*                 
                           .,.*,*****,,,.*,/                                #%////********/,*//*                   
                             ....,*,,*,*,,,,*(*                            &#//***,**////**(*/%#/                  
                                .,,**,,,**,,*.*/.                        .#//,/*,,/**/**(**/*,*(&@*                
                                  &%,,*,,*****,,/,  *                   ///*/**,**//**/#**,*,/,/***                
                                    *(,,*.,****,,(/#/*//%              /(***,*.*//,**#*,,**..,*/(&&                
                                       #/*,,.,,/*,////*,/**/          ,(****,*//,*//,,/*.,*,,,,*/((                
                                          /**,,,**,,*(/,/,,*(%@      ,#*****/*,***,,/,*,,,**/*/#&@                 
                                            ,(*,,,**,,(,**,.*,,*/*   ((/*,(/**,,,*,.,,,,,******(@&                 
                                               (//*./,,(**,,,*,///%@#//**/*/.,,***,,,,*,/*/////(%,                 
                                                  #/*,/,,/**,*,**//%(*,/*#.**,,,,,.,,,//****/(#@@@                 
                                                    /#/*/,/,,*,,,*%(/(,/,*,,..,,,*,*******//(#@@(                  
                                                        ((##*(,#/((//*,,,,,,,*,,,****/////(((@&,                   
                                                          @@&@@@%%%%*,,,(***,,,***/((((((##@@@.                    
                                                          ..,(&&@@%(((/*//*/*////((((/((%%.                        
                                                                  #@&%%@&.....,/**//&                              
                                                                    &&&&@                                         

	Version - dev-1.0     WORK IN TERMUX BY RDROID99
	""" + color.END)


def main():
    banner()
    if len(sys.argv) == 2:
        number = sys.argv[1]
        api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
        output = requests.get(api)
        content = output.text
        obj = json.loads(content)
        country_code = obj['country_code']
        country_name = obj['country_name']
        location = obj['location']
        carrier = obj['carrier']
        line_type = obj['line_type']

        print(color.GREEN + "[+] " + color.END + "Phone number information gathering")
        print("--------------------------------------")
        time.sleep(0.2)
        if country_code == "":
            print(color.DARKCYAN + " - Getting Country" + color.END + "[" + color.RED + "FAILED " + color.END + "]")
        else:
            print(color.DARKCYAN + " - Getting Country" + color.END + "[" + color.GREEN + "OK " + color.END + "]")

        time.sleep(0.2)
        if country_name == "":
            print(
                color.DARKCYAN + " - Getting Country Name" + color.END + "[" + color.RED + "FAILED " + color.END + "]")
        else:
            print(color.DARKCYAN + " - Getting Country Name" + color.END + "[" + color.GREEN + "OK " + color.END + "]")

        time.sleep(0.2)
        if location == "":
            print(color.DARKCYAN + " - Getting Location" + color.END + "[" + color.RED + "FAILED " + color.END + "]")
        else:
            print(color.DARKCYAN + " - Getting Location" + color.END + "[" + color.GREEN + "OK " + color.END + "]")

        time.sleep(0.2)
        if carrier == "":
            print(color.DARKCYAN + " - Getting Carrier" + color.END + "[" + color.RED + "FAILED " + color.END + "]")
        else:
            print(color.DARKCYAN + " - Getting Carrier" + color.END + "[" + color.GREEN + "OK " + color.END + "]")

        time.sleep(0.2)
        if line_type == None:
            print(color.DARKCYAN + " - Getting Device" + color.END + "[" + color.RED + "FAILED " + color.END + "]")
        else:
            print(color.DARKCYAN + " - Getting Device" + color.END + "[" + color.GREEN + "OK " + color.END + "]")

        print("")
        print(color.GREEN + "[+] " + color.END + "Information Output")
        print("--------------------------------------")
        print(color.RED + "____________________________________")
        print(color.GREEN + " - Phone number: " + str(number))
        print(color.RED + "____________________________________")
        print(color.GREEN + " - Country: " + str(country_code))
        print(color.RED + "____________________________________")
        print(color.GREEN + " - Country Name: " + str(country_name))
        print(color.RED + "____________________________________")
        print(color.GREEN + " - Location: " + str(location))
        print(color.RED + "____________________________________")
        print(color.GREEN + " - Carrier: " + str(carrier))
        print(color.RED + "____________________________________")
        print(color.GREEN + " - Device: " + str(line_type))
        print(color.RED + "____________________________________" + color.END)
    else:
        os.system('call')
        os.system('date')
        print(color.BLUE + "[?] Usage:")
        print(color.CYAN + "	./%s <phone-number>" % (sys.argv[0]))
        print(color.CYAN + "	./%s +13213707446" % (sys.argv[0]) + color.END)


main()
