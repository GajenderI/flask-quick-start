# Importing library

import cv2
from pyzbar.pyzbar import decode
from flask import Flask, request, Response
import numpy as np
import base64
import re
import json
from PIL import Image
from io import BytesIO

# Initialize the Flask application
app = Flask(__name__)

def decodeImage(img):
    try:
        detectedBarcodes = decode(img)
        return detectedBarcodes
    except TypeError:
     	   print ("cannot unpack non-iterable NoneType object")
         
# Make one method to decode the barcode
@app.route('/ecapi/bcdecode', methods=['POST'])
def BarcodeReader():

    image_data = re.sub('^data:image/.+;base64,', '', request.form['theFile'])
    im = Image.open(BytesIO(base64.b64decode(image_data)))

    detectedBarcodes = decodeImage(im)
    
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
        return json.dumps({'result': 'failed', 'message': "Barcode Not Detected or your barcode is blank/corrupted!"}), 200, {'ContentType': 'application/json'}
    else:
        if detectedBarcodes[0].data!="":
            return json.dumps({'result': 'success', 'text': detectedBarcodes[0].data.decode("utf-8"), 'type': detectedBarcodes[0].type}), 200, {'ContentType': 'application/json'}
		
# start flask app
app.run(host="0.0.0.0", port=5000, debug=True)