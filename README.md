# MIME-Description-Reference-
An incomplete reference of file extensions to their correlated MIME content types and descriptions.

Data in this file is in JSON format. Each entry looks something like this:

".ext" : { "descriptions" : ["A description of file content", "A redundant description"], "mimes" : ["file/content", "file/alternate"] }

I needed a good reference associating file extensions types to their verbal descriptions and MIME types, but to my dismay, I could find no such file on the surface web. So, I figured out how to dump system data from MacOS and wrote a small script to organize the data into a JSON file.

The reference is not complete. You may notice most entries have empty MIME arrays. Some entries may be redundant or incorrect. I will try my best to remove redundant descriptions, but most likely, I will not update MIME arrays.

I've also included the original Python script I wrote to extract, but not format, this data. The script is messy, not commented, and poorly optimized, but it works nonetheless. 
