#!/usr/bin/env python3
import os
import csv
from datetime import datetime, timedelta

def runTest(name, path, logPath):
	today = datetime.today()
	os.system("jmeter -n -t " + path + name + ".jmx -l " + logPath + name + '-' + str(today.year) + '-' + str(today.month) + '-' + str(today.day) + ".jtl")

def readLog(name, path):
	today = datetime.today()
	with open(path + name + '-' + str(today.year) + '-' + str(today.month) + '-' + str(today.day) + ".jtl", "r") as file:
		reader = csv.reader(file)
		for row in reader:
			if row[7]=="false":
				print(name + ", " + row[2] + ", " + row[8])

def runAndLogTests(name, testPath, logPath):
	runTest(name, testPath, logPath)
	readLog(name, logPath)
	removeLogs(name, logPath)

def removeLogsWindows(name, logPath):
	today = datetime.today()
	os.system("DEL " + logPath + name + '-' + str(today.year) + '-' + str(today.month) + '-' + str(today.day - 3) + ".jtl")

def removeLogs(name, logPath):
	today = datetime.today()
	os.system("rm " + logPath + name + '-' + str(today.year) + '-' + str(today.month) + '-' + str(today.day - 3) + ".jtl")

