import sys
import os  
import boto3 
import time


existingbuckets = []

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    existingbuckets.append(bucket.name)


def savefiletobucket (filename, bucketname,keyname):
    print "Uploading filename:",filename
    print "bucketname:",bucketname
    print "keyname:",keyname
   
    s3.meta.client.upload_file(filename,bucketname,keyname)
    return True


def CreateBucket (bucketname):
    if (bucketname in existingbuckets):
        return False
        
    print "Creating bucket:", bucketname    
    s3.create_bucket(Bucket=bucketname)
    return True

def backuppics (mydir,bucketname):
    if (not CreateBucket (bucketname)):
        print "bucket already created!"   
        return

    print "bucket created:",bucketname
    for root, dirs, files in os.walk(mydir):
        for file in files:
            if (savefiletobucket (os.path.join(root,file),bucketname,file)):
               print "saved file:", file
            else:
               print "failed to save file",file   


          


def main (mydir, bucketname): 
    for root, dirs, files in os.walk(mydir):
        for mydir in dirs:
            print mydir
            backuppics (os.path.join(root,mydir),bucketname+"."+ mydir)


if __name__ == "__main__":
    if len(sys.argv) < 3:
      print "Usage: source bucketname"
      raise SystemExit(1)
    main(sys.argv[1],sys.argv[2])    