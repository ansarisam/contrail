# contrail

ABSTRACT

The global Covid-19 pandemic restrictions and lockdowns has considerably disrupted the world socio-economic order. However, the global scare has turned out to be atmospherically advantageous for the stratosphere and the global environmental health, due to reduction of about 5 years of aviation global warming [14]. This project on reduction of anthropogenic global warming, unlike previous research model from George Mason University (GMU) capstone projects, aims to build a model and early quantify contrail formation. The methodology adopted distinguishes the model’s technology by utilizing automatic downloads of satellites images and machine learning convolutional neural network, to detect contrails from the U.S Cornus region. This model will provide an attempted solution to support the gap in the knowledge of early quantifying of contrails and back the effort to limit anthropogenic emissions leading to global warming.

We automatically downloaded satellites images utilizing IDV Unidata tool for 2021 Fall season. The process involved fine tuning the parameters of data collection and this included using the most advanced satellites dataset from GOESRALL. The image type selected was within GOES-East Cornus region 10.3 and 11.2um temperature fields approximately 1200 images in all, were annotated with the labelling (VOTT) tool. The annotated images were then exported to Google drive synced to Google Colab ecosystem and provisioned to the machine learning (YOLO) algorithm for training and detection of contrails. Our prediction model was on the high side of 70% IoU. But confidence in performance was low due to the exigencies of limited contrail images not forth coming. The trend of performance suggests some level of confidence in the capability of this model. This model when fully implemented will aide to dynamically direct and redirect flight around contrail supersaturated forming region (ISSR) and avoiding contrail formation with its attending global warming effect

Importance of the problem. 
Severals factors of aviation can lead to global warming but the effect of contrail on global warming is immediate when compared to other factors like carbon dioxide. By identying contrail and redirecting the flights can provide an immediate remediation. 

IDV tutorail for image download( Data Acquisition: https://youtu.be/mFycQIa6UFU)
![image](https://user-images.githubusercontent.com/44238057/145661174-f09ae84b-80e8-4ba3-b983-e65a299d9e6a.png)

VoTT Data annotation tutorail - https://youtu.be/Z6tW82woZQU
![image](https://user-images.githubusercontent.com/44238057/145661210-3cc63dfc-83f0-4823-b1eb-1821fd6c214b.png)

Process diagram 

![image](https://user-images.githubusercontent.com/44238057/144654626-f69a85d9-ae11-43d2-9dfd-370eccfff435.png)

# DAEN-690-Identification_of_Contrail_Cirrus_Clouds
Team Name : 3D- Data Driven Dudes
Project   : Machine Learning Image Processing of Satellite Images for Identification of Contrail Cirrus Clouds
Mentors   : Dr. Lance Sherry, Director CATSR
            Dr. Shamshad (Sam) Ansari, President and CEO

Drive Link for the ssd model - https://drive.google.com/drive/folders/1N_KTqg3YSfpfVn7Gv_OCmI4cwM_6dtBQ?usp=sharing

Drive link for Data (Images, Annotations and Text) - https://drive.google.com/drive/folders/1TPOIkaxGSAIRvXP7XrHMsLfCTfGMWm5Y?usp=sharing

ImageProcessing.ipynb - It has code to transform the image to 3 different new Images(Blurred, Enhanced Contrast, Rotate by 180 degree)

XmlToTxt.py - Converts the Annotations to text files

Team Name : Vision
Project : Image Processing Satellite Images for Contrail
Mentors   : Dr. Lance Sherry, Director CATSR
            Dr. Shamshad (Sam) Ansari, President and CEO
            
Drive link for Data and trained yolo models - https://drive.google.com/drive/u/5/folders/1jxBJL8Wa-T41ICXsQozUCiqP7sTlgidB
![image](https://user-images.githubusercontent.com/44238057/144655148-0e6c5329-799d-4e0e-82dc-ef7622774c32.png)

ISL scripts - Used to download images via IDV tool in automated fashion

XmlToTxt.py - Convers the annotations to text files

YoloContrail-TeamVision.ipynb - Yolov3 algorithm for training the data

ObjectDetection.py - Object detection code using darknet - Generates bounding box json along with confidence for the detected contrail images

objectdetectionBox.py - Drawing bounding boxes on the images using openCV



