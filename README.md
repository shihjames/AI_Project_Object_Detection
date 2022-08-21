# AI_Project
## Detect Traffic Density with Video Recognition to Empower Smart City

## Introduction
* Inspired by Toyota’s prototype "city" of the future — Woven City.
* Aiming to detect traffic density with computer vision to manage traffic flow and provide optimization solutions to congested road sections to reduce congestion.
* Transfer learning with Computer Vision Mode.

## Dataset
* The datasets used in the project is MIOvision Traffic Camera Dataset (MIO-TCD), were collected by the University of Sherbrooke and Miovision Inc. Canada and are available at http://podoce.dinf.usherbrooke.ca/challenge/dataset/.
* It Contains 137,743 high-resolution images containing one (or more) foreground object(s) with one of the following 11 labels: Articulated truck, Bicycle, Bus, Car, Motorcycle, Motorized vehicle, Non-motorized vehicle, Pedestrian, Pickup truck, Single unit truck, Work van.

## Methodology
* Model Selection: We apply the YOLOv3 (You only Look Once) model for vehicle detection and run it in Google Colab Notebook with a free GPU.
* Data Preprocessing: 
  (1) Selected x images randomly from the MIO-TCD data set and split the data into training, validation and testing set. 
  (2) In order to fit our data to the model, we resized images into the same size, preprocess label data to the required format, and create a text file for each image. 
  (3) Each text file contains the class of the object, the x and y coordinate at the center of the label, and the width and height of the label (normalized).

## Results
* We've trained our model with 30 epoch and 60 epoch, our training losses keep descending and finally reach plateau. Our validation loss is very close to our train loss that determines that it's not overfitting.
* 
<img src="https://user-images.githubusercontent.com/68275741/185775675-9519dc3e-9812-4401-a2e2-2e170b97f5db.jpeg" width="500"> <img src="https://user-images.githubusercontent.com/68275741/185775676-23917a09-1511-4e8f-b65c-8cb6e3273294.png" width="500">

## Conclusions
* Our result performed 0.7 in mAP 0.5 and 0.5 in mAP 0.5:0.95.
* Precision-recall curve shows that bus, car, pickup_truck, motorcycle, articulated_truck performed over 0.8 mAP @ 0.5.

## Future Work
* Detect traffic density using live CCTV camera to manage traffic flow in real-time.
* Use connected networks and cloud technologies to combine additional data sources such as in-vehicle GPSs, weather data and street conditions, etc. 
* Multiple connected data with sophisticated data analysis and AI capabilities for an interconnected system that can power smart decisions to create smarter cities.
