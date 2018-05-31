import sys, os, glob
from boto.s3.connection import S3Connection
from boto.s3.key import Key

AWS_ACCESS = ''
AWS_SECRET = ''

conn = S3Connection(AWS_ACCESS, AWS_SECRET)
bucket = conn.get_bucket('clothes-image')
directory = '/home/pi/Desktop'

def getFiles(dir):
    return [os.path.basename(x) for x in glob.glob(str(dir)+'*.jpg')]

def upload_S3(dir,file):
    k = Key(bucket)
    k.key = f
    k.set_contents_from_filename(dir + f)
    
def removeLocal(dir,file):
    os.remove(dir+file)
    
filenames = getFiles(directory)
print(filenames)

for f in filenames:
    print('Uploading %s to Amazon S3 bucket %s' % (f,bucket))
    upload_S3(directory, f)
    removeLocal(directory, f)
    
