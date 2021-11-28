import os
import glob
import json
import cv2
import subprocess
import pandas as pd
image_folder="C:/Users/aravk/Desktop/FinalProject/ImageOutput/inputNew/"
output_Json="C:/Users/aravk/Desktop/FinalProject/ImageOutput/outputJson/"
OUTPUT_PATH="C:/Users/aravk/Desktop/FinalProject/ImageOutput/outputBox/"
for jsonD in glob.glob(output_Json+"/*"):
    print(os.path.abspath(jsonD))
    with open(jsonD) as f:
        data =json.load(f)
        if(data!=[]):
            lenght = len(data)
            print(lenght)
            print(data)
            for i in range(lenght):
                filename = data[i]['image'].split('/')
                imagePath='C:/Users/aravk/Desktop/FinalProject/ImageOutput/inputNew/'+filename[-1]
                label = data[i]['predictions']['object']
                score = data[i]['predictions']['score']
                box = data[i]['predictions']['bbox']
                image_np = cv2.imread(os.path.abspath(imagePath))
                h=image_np.shape[0]
                w=image_np.shape[1]
                color=(122,68,143)
                (x,y) = (int(box[0]),int(box[1]))
                start=(int(box[0])+50,int(box[1]))
                end=(int(box[2])-50,int(box[3]))
                cv2.rectangle(image_np, start,end,
                              color, 2)
                text="{}: {}".format(label,score)
                scoreInt=int(score)
                if scoreInt > 50:
                    cv2.putText(image_np,text,(x+50,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,color,2)
                    OUTPUT_FILE = OUTPUT_PATH + filename[-1]
                    cv2.imwrite(OUTPUT_FILE, image_np)
