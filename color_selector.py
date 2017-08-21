import json
from pprint import pprint
from PIL import Image

def most_frequent_colour(image):

    w, h = image.size
    pixels = image.getcolors(w * h)

    most_frequent_pixel = pixels[0]

    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, '#%02x%02x%02x' % colour)
    
    print "%s was used %i times in that area." % (most_frequent_pixel[1], most_frequent_pixel[0])

    return most_frequent_pixel[1]

with open('config.json') as data_file:
    data  = json.load(data_file)

img = Image.open("image.jpg")

image_width = img.size[0]
image_height = img.size[1]

box_width = data['bounds']['width']
box_height = data['bounds']['height'] 

box_x = data['bounds']['x']
box_y = data['bounds']['y']


img3 = img.crop((
    box_x,
    box_y,
    box_x + box_width,
    box_y + box_height
    ))

color = most_frequent_colour(img3)

pprint(color)