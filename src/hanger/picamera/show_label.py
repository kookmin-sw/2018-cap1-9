import json
import argparse
import base64
import httplib2
import MySQLdb
import webcolors

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
                    'maxResults' : 5
                    },
                    {
                    'type' : 'IMAGE_PROPERTIES',
                    'maxResults' : 1
                    }]
                }]
            })
        response = service_request.execute()
        #label = response['responses'][0]['labelAnnotations'][0]
        #print json.dumps(response, indent=1, sort_keys=True)	#Print it out and make it somewhat pretty.
        blue = response['responses'][0]['imagePropertiesAnnotation']['dominantColors']['colors'][0]['color']['blue']
        green = response['responses'][0]['imagePropertiesAnnotation']['dominantColors']['colors'][0]['color']['green']
        red = response['responses'][0]['imagePropertiesAnnotation']['dominantColors']['colors'][0]['color']['red']

        requested_color = (red, green,  blue)
        closest_name = get_colour_name(requested_color)
        print closest_name
        
        label1 = response['responses'][0]['labelAnnotations'][0]['description']
        label2 = response['responses'][0]['labelAnnotations'][1]['description']
        label3 = response['responses'][0]['labelAnnotations'][2]['description']
        label4 = response['responses'][0]['labelAnnotations'][3]['description']
        label5 = response['responses'][0]['labelAnnotations'][4]['description']
        list = ['clothing', 'product', 'pink', 'white', 'blue', 'khaki', 'black', 'red']
        label = label1
        
        if label1 in list :
            label1 = 'null'
            label = label2
        elif label2 in list :
            label2 = 'null'
            label = label3
        elif label3 in list :
            label3 = 'null'
            label = label4
        elif label4 in list :
            label4 = 'null'
            label = label5
        elif label5 in list :
            label5 = 'null'
            label = 'null'
            
        print label1
        print label2
        print label3
        print label4
        print label5

        upper = ['jacket', 'shorts', 'active shorts', 'dress',
                     'day dress', 'blouse', 'sleeve', 'collar', 'cardigan',
                     'jumper', 'pullover', 'shirt', 'sweat-shirt', 'T-shirt', 'tshirts', 'tshirt', 'sweater']
        if label1 in upper :
            position = 'upper'
        elif label2 in upper :
            position = 'upper'
        elif label3 in upper :
            position = 'upper'
        elif label4 in upper :
            position = 'upper'
        elif label5 in upper :
            position = 'upper'
        else :
            position = 'lower'

        print position
            
        db = MySQLdb.connect(host="34.225.233.100",
                                          user="root",
                                          passwd="1234",
                                          db="VT")
        cur = db.cursor()
        
        cur.execute("""INSERT INTO Clothes_Info(Color, Kind, Picture_Addr, position) VALUES (%s, %s, %s, %s)""", (closest_name, label, photo_file.replace('.png', ''), position))
        db.commit()
        for row in cur.fetchall():
            print(row[1])
    
        db.close()

        return 0

def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_color):
    try:
        closest_name = webcolors.rgb_to_name(requested_color)
    except ValueError:
        closest_name = closest_colour(requested_color)
    return closest_name

if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('image_file', help = 'The image you\'d like to label.')
        args = parser.parse_args()
        parser = argparse.ArgumentParser()
                    
        main(args.image_file)
        
