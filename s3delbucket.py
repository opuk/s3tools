#!/usr/bin/env python
from boto.s3.connection import S3Connection
import sys

try:
  bucket = sys.argv[1]
except:
  print("nope.")
  sys.exit(1)

conn = S3Connection()

full_bucket = conn.get_bucket(bucket)

for i in full_bucket.list():
  print("Deleting " + i.name)
  i.delete()

print("Deleting bucket " + bucket)
conn.delete_bucket(bucket)
