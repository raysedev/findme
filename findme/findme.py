import shodan
import sys
import os
import subprocess
import shlex
import json

SHODAN_API_KEY = "Your API Key Here"

api = shodan.Shodan(SHODAN_API_KEY) 

while True:
	print "Welcome to FindMe (Developed by RayseDev)"
	question = raw_input("Press enter to continue or type in ? for help: ")

	if question == "?":
		print "------------------Help-------------------"
		print ""
		print "-------------General-Options-------------"
		print ""
		print "IP option - Get a list of vulnerable IP's"
		print "ALL option - Get a list of vulnerable devices(All data)"
		print ""
		print "---------------Save-to-log---------------"
		print ""
		print "Saving IP's to a log will give you a log.txt file at the main directory of FindMe and it is going to be usable for a ping test"
		print ""
		print "------------------Ping-------------------"
		print ""
		print "After you save the IP's to a log you can  use the file for a ping connection test"
		print ""
	else:
		dataquestion = raw_input("What data do you need?(IP/ALL): ")

		if dataquestion == "all":
			print "Retrieving information..."
			from findmeall import start
			start()
			question = raw_input("Do you want me to save these in a log? Y/n: ")
			if question == "y":
				print "Wait a moment..."
				os.system("python findmealllog.py >> datalog.txt")
			if question == "n":
				break

		if dataquestion == "ip":
			print "Retrieving information..."
			from findmeip import start
			start()
			question = raw_input("Do you want me to save these in a log? Y/n: ")
			if question == "y":
				print "Wait a moment..."
				os.system("python findmeiplog.py >> log.txt")
				pingquestion = raw_input("Do you want me to ping the IP's from the log you just made? Y/n: ")
				if pingquestion == "y":
					os.system("chmod +x ping.sh")
					os.system("./ping.sh")
			if question == "n":
				break
		

		

