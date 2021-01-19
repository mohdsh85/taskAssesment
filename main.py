from fastapi import FastAPI
from starlette.responses import FileResponse
import urllib.request
from skimage.metrics import structural_similarity as ssim
import numpy as np
from cv2 import cv2  
from PIL import Image 

app = FastAPI()
Auth = 'kmrhn74zgzcq4nqb'
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get('/test')
def test():
    return {"test":"hello test"}

@app.get('/downloadImages')
def downloadImages():
    resource = urllib.request.urlopen("https://i.imgur.com/gZKMme4.jpg?&Auth="+Auth)
    resource2 = urllib.request.urlopen("https://i.imgur.com/gWzHdpx.png?&Auth="+Auth)
    output = open("file1.jpg","wb")
    output.write(resource.read())
    output.close()    
    output2 = open("file2.png","wb")
    output2.write(resource2.read())
    output2.close()    
    return {'status':'success, images downloaded '}
    
@app.get('/compareImages')
def compare_images():
    img = Image.open('file1.jpg').convert("RGB")
    dImage1 = np.asarray(img)
    (H, W,s) = dImage1.shape
    img2 = Image.open('file2.png').convert("RGB")
    img2_resize = img2.resize((W, H))
    dImage2 = np.asarray(img2_resize)
    (H, W,s) = dImage2.shape
    score = ssim(dImage2, dImage1, multichannel=True, full=True)
    return {"similarity":(score[0])}
