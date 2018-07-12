import csv

# ## this is called a method 
# def print_recommendation(row):
#   if row[0] == 1:
#      return {print('hello')}

# Client info
#clientname = input("What is the client name?")
clientname = "FakeCompany1"

# Introduction
print('Prepared for: *',clientname,'*')

print ('''
# IT Audit Executive Summary

## Introduction

We have found the following items to require immediate attention.  Please review carefully and call us to discuss ASAP!
''')


#First Category
print ('''
## Cat1
''')

with open("recs_cat1.csv") as csvfile:
   rows = csv.reader(csvfile, delimiter=',', quotechar='"')
   for row in rows:
        if row[0] in (None, ""):
             continue
        f = open('assets/%s' % row[3])
        file_contents = f.read()
        print (file_contents)
        f.close()


#Second Category
print ('''
## Cat2
''')

with open("recs_cat2.csv") as csvfile:
   rows = csv.reader(csvfile, delimiter=',', quotechar='"')
   for row in rows:
        if row[0] in (None, ""):
             continue
        f = open('assets/%s' % row[3])
        file_contents = f.read()
        print (file_contents)
        f.close()

# Conclusion
print ('''
## Conclusion

Please act on these recommendations as soon as possible. Thank you.
''')