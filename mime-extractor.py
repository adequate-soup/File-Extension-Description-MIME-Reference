#!/usr/local/bin/python3.8

# v. 1.0 - Benjamin Sims - March, 19 2023

# Run the following command on MacOS to get lsdump.txt:

# /System/Library/Frameworks/CoreServices.framework/Frameworks/\
# LaunchServices.framework/Support/lsregister -dump -all system >\
# /Users/bensims/Desktop/lsdump.txt

import json

infilepath = "/path/to/lsdump.txt"

outfilepath = "/path/to/where/i/want/my/output"

infile = open(infilepath)

files = infile.readlines()

infile.close()

keys = ["type id:", "localizedDescription:", '"en" = "', "tags:",
        '"LSDefaultLocalizedValue" = "', "localizedShortNames:",
        '"English" = "', "localizedNames:", "bindings:", "claim id:"]

data = []

for x in range(len(files)):

    if files[x][:len(keys[0])] != keys[0] and files[x][:len(keys[9])] != keys[9]:

        continue

    linedata = {}

    if x+2 > len(files):

        break

    newLine = files[x+1]

    x += 1

    pairs = [[keys[1],keys[4]],
             [keys[1],keys[2]],
             [keys[7],keys[4]],
             [keys[7],keys[6]],
             [keys[5],keys[4]],
             [keys[5],keys[6]]]

    linedata["description"] = ""

    counter = 0

    while not linedata["description"]:
        
        if counter > 5:

            break

        pair = pairs[counter]

        z = x

        while newLine[:len(pair[0])] != pair[0]:

            if z+2 > len(files):

                break

            newLine = files[z+1]

            z += 1

        seen = "".zfill(len(pair[1]))

        description = ""

        for char in newLine:

            if seen == pair[1]:

                if char == '"':

                    break

                description += char

                continue

            seen = seen[1:] + char

        linedata["description"] = description

        counter += 1

    while "-----" not in newLine[:10]:

        if newLine[:len(keys[3])] == keys[3] or newLine[:len(keys[8])] == keys[8]:

            linedata["extensions"] = []

            linedata["mimes"] = []

            for tag in newLine.split()[1:-1]:

                newTag = tag.strip(",\n")

                if newTag[0] == ".":

                    linedata["extensions"].append(newTag)

                elif "/" in newTag:

                    linedata["mimes"].append(newTag)

            break

        if x+2 > len(files):

            break

        newLine = files[x+1]

        x += 1

    if "description" in linedata and "extensions" in linedata:

        if linedata["description"] and linedata["extensions"]:

            data.append(linedata)
    
outfile = open(outfilepath, "w")

outfile.write(json.dumps(data))

outfile.close()
