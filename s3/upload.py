import boto3
import sys


if len(sys.argv) != 3 :
	print "Please input bucket name and file name"

bucketname = sys.argv[1]
filename = sys.argv[2]

# Let's use Amazon S3
s3 = boto3.resource('s3')

data = open(filename, 'rb')
s3.Bucket(bucketname).put_object(Key=filename, Body=data)