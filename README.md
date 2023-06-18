# Live microscopic assessment of in multipotent mesenchymal stromal cells senescence 

This pipeline can be used for analyzing cell aging in culture. The pretrained models presented here are designed to work with phase-contrast images of mesenchymal multipotent stromal cells (MSCs). However, you can obtain models that work effectively with other cell types using the same approach.

# Basic usage
## Instance segmentation with Cellpose model
First and foremost, you need to use an instance segmentation model to obtain cell masks. We recommend using the LC models from the Cellpose model zoo. The LC4 model performs the best, but please note that it requires significant computational resources. To download our pretrained model for MSC, use the following code:

```python

```

## Creating cells annotation file
To create your own file for cell annotation, you can refer to the code of **cells_annotation**, which allows you to automatically annotate your cells. For class-based annotation, you will need images of cell staining in the form of a binary layer. You can use beta-galactosidase staining, as we did in our case, or choose your own aging marker.

## Creating custom image dataset
Next, you need to create the **custom_image_dataset** class, which will generate images of individual cells with the specified size. To do this, use the corresponding code. Don't forget to calculate the mean and std values for the train dataset as they are required for normalizing the resulting images. It is also important to choose the optimal cell image size, which should be specified in the dataset creation code. Afterwards, you will be able to create instances of the **train_set** and **test_set classes**, which inherit from the **custom_image_dataset class**.

## Cell senescence classification model
And finally, to perform the classification of your cells, you can load our pretrained EfficientNet-B4 model for MSC. You can do this using the following code:

```python

```
Please note that if your cells significantly differ in size or morphology from MSC, the model may perform slightly worse. In such cases, you will likely need to fine-tune the model on your own data.

# System requirements
Linux, Windows and Mac OS are supported for running the code. At least 8GB of RAM is required. 16GB-32GB may be required for larger images. For working with cell image classification, we recommend using a GPU with a minimum of 8 GB of memory size.

# Useful links 
[https://github.com/MouseLand/cellpose](url)
[https://github.com/lukemelas/EfficientNet-PyTorch](url)
