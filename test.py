import pandas as pd
from PIL import Image
import os
import numpy as np
from keras.models import load_model
model = load_model('my_model.h5')

#testing accuracy on test dataset
from sklearn.metrics import accuracy_score
y_test = pd.read_csv('Test.csv')
labels = y_test["ClassId"].values
imgs = y_test["Path"].values
data=[]
for img in imgs:
    image = Image.open(img)
    image = image.resize((30,30))
    data.append(np.array(image))
X_test=np.array(data)
# pred = model.predict_classes(X_test)
pred = np.argmax(model.predict(X_test), axis=-1)


#Accuracy with the test data
from sklearn.metrics import accuracy_score
print(accuracy_score(labels, pred))
model.save("traffic_classifier.h5")