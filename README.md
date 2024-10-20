# Flipkart-GRiD-6.0
## [Solution of Flipkart GRiD 6.0 - Robotics Challenge](https://unstop.com/hackathons/flipkart-grid-60-robotics-challenge-flipkart-grid-60-flipkart-1024253)

  - Team name
  
       - **ssguptaa1212**
  
  - Members
  
      - [Shubhi Gupta](https://github.com/ShubhiGupta20)
  
      - [Princy Sharma](https://github.com/05princy)
                   
      - [Meenakshi](https://github.com/Mi-5555)
  
  - Architecture
  
     - Resnet18 pretrained model for detecting shelf life of fruits & vegetables

     
# Problem

## Theme: 

Smart Vision Technology Quality Control
Smart vision technology to use advanced imaging systems and algorithms to capture and analyze visual information. In the context of quantity and quality testing, it helps automate the quality inspection process by identifying a product, its quantity and any defects or quality attributes.

We performed 3 steps :

### **1. OCR to extract details from image/label**

For this we used,
- **Python:** For building the machine learning model, implementing the OCR system, and managing the image processing.
- **TensorFlow/Keras:** Libraries are employed to train and run the fruit freshness detection model.
- **Tesseract OCR:** Used for extracting text from product labels.
- **OpenCV:** Used for image processing that helps in detecting and analyzing the visual features of the fruits.

### **2. Using OCR to get expiry date details**

It consists : 
- Dataset of Product Labels
- Labeling and Annotations
- Image Preprocessing for OCR : It consists OpenCV, GrayScale conversion etc.
- Text Recognition Tool : KerasOCR
- Character Segmentation

### **3. Detecting freshness of fresh produce**

The dataset comprises a diverse range of fruits and vegetables commonly found in culinary settings, including apples, oranges, bananas, tomatoes, cucumbers, carrots, and more. Each item in the dataset is captured in multiple images, representing both fresh and rotten/stale states. The dataset encompasses a variety of fruit and vegetable types to ensure the generalization and robustness of the classification models.

**Key Features of dataset are:** Image Variety, Freshness levels, Annotation, High- Quality Images, Large scale of Images.

The classification report shows how well the fruit classification model performed. Overall, the model did really well with high scores for most of the fruits. It achieved an accuracy of 0.98, which means it predicted the correct fruit in nearly 98% of cases. The macro average scores were also impressive, with precision, recall, and F1-score all around 0.99. This means the model performed consistently across all fruit classes, regardless of class imbalance. The weighted average scores took into account the number of instances for each fruit and were still quite good, all at 0.98.

The next classification report shows how well the model performed in differentiating between fresh and spoiled fruits. With an accuracy of 0.98, the model correctly classified fruits in nearly 98% of cases. The precision, recall, and F1-scores for both classes were around 0.98, indicating consistent and accurate predictions. Overall, our model demonstrated strong performance in distinguishing between fresh and spoiled fruits, achieving high accuracy and precision.

Here is the diagram of ResNet-18 Model Architecture:
   
![ResNet-18 Model Architecture](https://i.postimg.cc/cxxQ2J45/model.png)
   
### Technology Used: 

#### Hardware Specifications:

- Raspberry Pi 4 Model B(4GB LPDDR4 RAM) – core processing unit.
- Raspberry Pi 4 Model B Camera Module – captures high-resolution images of fruits and product labels.
- Ethernet Cable
- SD Card (16 GB)
- 5V/3V USB-C Power Supply (Adapter)

