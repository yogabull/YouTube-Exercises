#Dictionaries

#creating a new dictionary
d = {}
# another way to write the above: d = dict()
dict = dict()
#We are adding this info to the dictionary:
# d = {'George': 24, 'Tom': 32}

d['George'] = 24
d['Tom'] = 32
d['Jenny'] = 16

print ('George is', (d['George']))
print (d['Jenny'])

#This next line updates Jenny's age. The dictionary is modifiedself.
d['Jenny'] = 20
print ('Jenny\'s new age is:')
print (d['Jenny'])

#Values can be any 'type'
#Keys can only be certain types: most commonly strings and numbers

# how to iterate over key-value pairs in a dictionary?
print('This next code iterates through the dictionary.')
for key, value in d.items():
    print ('key:', key)
    print ('value:', value)
    print ('\f')

# print ('\a') #introduces a space and a bell/alarm

#Escpae Sequnce test:
# The carraige return escape sequence moves the cursor to the line's beginning..
# It will then overwright the string's first letters ie ' Does'.
print (' Does this come before: \rThis?')
