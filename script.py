#STRINGS & CONSOLE OUTPUT
#Acces by index
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:

+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5

So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]

print fifth_letter

#string methods
parrot = "Norwegian Blue"
print len(parrot)
#lower() get rid of all the capitalization in your strings. You call
parrot = "Norwegian Blue"

print parrot.lower()
#upper()
parrot = "norwegian blue"

print parrot.upper()

#The str() method turns non-strings into strings!
"""Declare and assign your variable on line 4,
then call your method on line 5!"""

pi = 3.14
print str(pi)

#on the Dot notation
"""Let's take a closer look at why
 you use len(string) and str(object),
 but dot notation (such as "String".upper())
 for the rest."""
 ministry = "The Ministry of Silly Walks"

print len(ministry)
print ministry.upper()

#Printing Variables

the_machine_goes = "Ping!"
print the_machine_goes

#String Concatenation
# Print the concatenation of "Spam and eggs"
"""This will print out the phrase spam and eggs"""
print "Spam " + "and " + "eggs"
