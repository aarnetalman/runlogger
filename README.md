# Runlogger - a simple command line run logger written in Python

Supports:
* adding new entries (date, distance, time)
* automatically calculates the pace (minutes/km)
* viewing all the entries
* viewing the latest run
* viewing the fastest run
* viewing the longest run


### Format

Stores entries as json lines. 
```
{"date": "June 8, 2020", "distance": "7.3", "time": "00:46:29"}
```

### Options

```
--add_entry : Add new entry interactively from the command line
--print_all : View all the entries
--print_latest : View the latest entry
--print_fastest : View the entry for the fastest run
--print_longest : View the entry for the longest run
```

### TODO

Add statistics and graphs to view progress

