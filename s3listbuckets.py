#!/usr/bin/env python
from boto.s3.connection import S3Connection

conn = S3Connection()
price_regular = 0.030
price_reduced = 0.024
size=0
files=0

buckets = conn.get_all_buckets()

for i in buckets:
  for j in conn.get_bucket(i):
    #print j.name + ': ' + str(j.size/1024/1024) +'mb.'
    size+=j.size
    files+=1

mbused=size/1024/1024
gbused=size/1024/1024/1024

print ''
print 'All buckets are taking up '+ str(mbused) +' mb or ' + str(gbused) + ' gb.'
print 'Estimated monthly cost(regular): $' + str(gbused*price_regular) +'.'
print 'Estimated monthly cost(reduced redundancy): $' + str(gbused*price_reduced) +'.'
print str(files) + " files."
