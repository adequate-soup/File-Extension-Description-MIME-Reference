# MIME-Description-Reference-
A somewhat complete reference of MIME content types to their correlated file extension and descriptions.

Data in this file is in JSON format. Each entry looks something like this:

{ "description" : "A description of file content", "extensions" : [".myext", ".ext"], "mimes" : ["file/content", "file/alternate"] }

I needed a good reference correlating MIME types to their verbal descriptions for a small webserver I was working on, but to my dismay, I could find no such file on the surface web. So, I figured out how to dump system data from MacOS and wrote a small script to organize the data into a JSON file.

The reference is not entirely complete. You may notice some entries have empty MIME and file extension arrays. Some entries may be redundant or incorrect, but the file contains complete refrerences for most commonly encountered content types. I may get around to making corrections if I have time.

I've also included the Python script I wrote to extract this data. The script is messy, not commented, and poorly optimized, but it works nonetheless. 
