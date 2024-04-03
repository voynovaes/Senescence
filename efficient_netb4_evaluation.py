# -*- coding: utf-8 -*-
"""Efficient_NetB4_evaluation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gFUpUDTd-vjUKw-fUHxMUEDh0uN7mg1x
"""

image_size = 490 #you can add here your size of cell images

import efficientnet_pytorch
from efficientnet_pytorch import EfficientNet
model_name = 'efficientnet-b6'
model = EfficientNet.from_pretrained(model_name, num_classes=1) 

# If the model input is a single-band image, you must use the following code
from efficientnet_pytorch.utils import Conv2dStaticSamePadding
model._conv_stem = Conv2dStaticSamePadding(1, 56, kernel_size=(3, 3), stride=(2, 2), image_size = image_size, bias=False)

# Here you need to add path to efficientnetb4_state_dict
model.load_state_dict(torch.load("path_to_model_state_dict"))
model = model.to(device)

model.eval()

# Evaluate the model on the validation set
true_labels = []
probs = []

with torch.no_grad():
    for images, labels in val_loader:
        # Move images and labels to the device (e.g., GPU) if available
        images = images.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(images)
        prob = torch.sigmoid(outputs)

        # Accumulate probabilities and true labels
        true_labels.extend(labels.cpu().numpy())
        probs.extend(prob.cpu().numpy())

from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(true_labels, probs)
accuracy_scores = []
for thresh in thresholds:
    accuracy_scores.append(accuracy_score(true_labels, [m > thresh for m in probs]))

accuracies = np.array(accuracy_scores)
max_accuracy = accuracies.max()
max_accuracy_threshold =  thresholds[accuracies.argmax()]
print(max_accuracy)
print(max_accuracy_threshold)

predictions = []
for prob in probs:
    pred = (prob > max_accuracy_threshold)
    predictions.extend(pred)

from sklearn.metrics import classification_report

# Calculate classification report
report = classification_report(true_labels, predictions)
