import os
import glob
import subprocess
import pandas as pd
image_folder="/Users/aadya/Downloads/new/"
yolov3_weights_path="/Users/aadya/Downloads/yolov3.weights"
cfg_path="/Users/aadya/Downloads/yolov3.cfg"
output_path="/Users/aadya/Downloads/output/"
for img in glob.glob(image_folder+"/*"):
    print(os.path.abspath(img))
    imagefile=os.path.basename(img)
    image_path=image_folder+imagefile
    image_name = os.path.basename(image_path)
    process = subprocess.Popen(['./darknet/darknet', 'detect',cfg_path, yolov3_weights_path, image_path],
                     stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    std_string = stdout.decode("utf-8")
    std_string = std_string.split(image_path)[1]
    count = 0
    outputList = []
    rowDict = {}
    for line in std_string.splitlines():

        if count > 0:
            if count%2 > 0:
                obj_score = line.split(":")
                obj = obj_score[0]
                score = obj_score[1]
                rowDict["object"] = obj
                rowDict["score"] = score
            else:
                bbox = line.split(",")
                rowDict["bbox"] = bbox
                outputList.append(rowDict)
                rowDict = {}
        count = count +1
    rowDict["image"] = image_path
    rowDict["predictions"] = outputList

    df = pd.DataFrame(rowDict)
    df.to_json(output_path+"/"+image_name.replace(".jpg", ".json").replace(".png", ".json"),orient='records')