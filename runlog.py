#!/usr/bin/python
"""
Simple command line run logger. Stores entries as json lines. 
"""

import json
from argparse import ArgumentParser
from datetime import datetime


parser = ArgumentParser(description='Running log')

parser.add_argument("--print_all",
        action = "store_true",
        dest = "print_all")

parser.add_argument("--print_latest",
        action = "store_true",
        dest = "print_latest")

parser.add_argument("--print_fastest",
        action = "store_true",
        dest = "print_fastest")

parser.add_argument("--print_longest",
        action = "store_true",
        dest = "print_longest")

parser.add_argument("--add_entry",
        action = "store_true",
        dest = "add_entry")

def readLog():
    with open("log.jsonl", "r") as f:
        lines = f.read().splitlines()
    data = []
    for line in lines:
        if line is not '':
            lineData = json.loads(line)
            data.append(lineData)
    return data


def getAvgPace(entry):
    h, m, s = entry["time"].split(':')
    total_seconds = (int(h)*3600) + (int(m)*60) + int(s)
    seconds_per_mi = float(total_seconds) / float(entry["distance"])
    minutes_per_mi = int(seconds_per_mi / 60)
    seconds_remainder = int(seconds_per_mi - (minutes_per_mi * 60))
    return minutes_per_mi, seconds_remainder 


def getFastest(data):
    fastest = 36000
    fastest_entry = data[0]
    for entry in data:
        minutes, seconds = getAvgPace(entry)
        s = (int(minutes)*60) + int(seconds)
        if s < fastest:
            fastest_entry = entry
    return fastest_entry


def getLongest(data):
    longest = 0.0
    longest_entry = data[0]
    for entry in data:
        distance = float(entry["distance"])
        if distance > longest:
            longest_entry = entry
    return longest_entry


def addEntry():
    #print("Let's add the date to the log entry (format: \"Month Day, Year\").")
    #month = input("Input the month: ")
    #day = input("Input the day: ")
    #year = input("Input the year: ")
    #d = "{} {}, {}".format(month, day, year)
    dateTimeObj = datetime.now()
    d = dateTimeObj.strftime("%b %d %Y")
    dist = float(input("Input distance in miles: "))
    t = input("Input time (format: \"hh:mm:ss\"): ")
    entry = "{\"date\": \"" + d + "\", \"distance\": \"" + str(dist) + "\", \"time\": \"" + t + "\"}"
    with open("log.jsonl", "a") as f:
        f.write(entry)


def main():
    config = parser.parse_args()
    data = readLog()
    if config.print_all:
        for entry in data:
            minutes_per_mi, seconds_remainder = getAvgPace(entry)
            print("Date: {}, Distance: {}, Time: {}, Avg pace: {}:{:0=2d}".format(entry["date"],entry["distance"],entry["time"], minutes_per_mi, seconds_remainder))
    elif config.print_latest:
        entry = data[-1]
        minutes_per_mi, seconds_remainder = getAvgPace(entry)
        print("Date: {}, Distance: {}, Time: {}, Avg pace: {}:{:0=2d}".format(entry["date"],entry["distance"],entry["time"],minutes_per_mi,seconds_remainder))
    elif config.print_fastest:
        entry = getFastest(data)
        minutes_per_mi, seconds_remainder = getAvgPace(entry)
        print("Date: {}, Distance: {}, Time: {}, Avg pace: {}:{:0=2d}".format(entry["date"],entry["distance"],entry["time"],minutes_per_mi,seconds_remainder))
    elif config.print_longest:
        entry = getLongest(data)
        minutes_per_mi, seconds_remainder = getAvgPace(entry)
        print("Date: {}, Distance: {}, Time: {}, Avg pace: {}:{:0=2d}".format(entry["date"],entry["distance"],entry["time"],minutes_per_mi,seconds_remainder))
    elif config.add_entry:
        addEntry()
        print("Done!")


if __name__ == "__main__":
    main()
