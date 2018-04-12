import json
import argparse
import base64
import httplib2

from ast import literal_eval
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'

def main(photo_file):
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials, discoveryServiceUrl=DISCOVERY_URL)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        service_request = service.images().annotate(body={
            'requests':[{
                'image':{
                    'content':image_content.decode('UTF-8')
                    },
                'features' : [{
                    'type' : 'LABEL_DETECTION',
                    'maxResults' : 1
                    }]
                }]
            })
        response = service_request.execute()
        label = response['responses'][0]['labelAnnotations'][0]
        print('Found label: %s for %s' % (label, photo_file))
        return 0
       
if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('image_file', help = 'The image you\'d like to label.')
        args = parser.parse_args()
        parser = argparse.ArgumentParser()
                    
        main(args.image_file)
        
