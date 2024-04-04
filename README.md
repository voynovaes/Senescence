# Live microscopic assessment of multipotent mesenchymal stromal cells senescence 

This pipeline can be used for analyzing cell aging in culture. The pre-trained models presented here are designed to work with phase-contrast images of mesenchymal multipotent stromal cells (MSCs). However, you can obtain models that work effectively with other cell types using the same approach.

# Basic usage
## Instance segmentation with Cellpose model
First and foremost, you need to use an instance segmentation model to obtain cell masks. We recommend using the LC models from the Cellpose model zoo. The LC4 model performs the best, but please note that it requires significant computational resources. You can download our [pretrained model](https://disk.yandex.com/d/P6ozzuQhfjHsAQ) for MSCs.
As a result, you should get something similar to the following image:
![Example_Cellpose](https://github.com/voynovaes/Senescence/assets/126082195/ee71e487-c269-4f36-a121-f89cde529796)


## Creating cells annotation file
To create your own file for cell annotation, you can refer to the code of **cells_annotation**, which allows you to automatically annotate your cells. For class-based annotation, you will need images of cell staining in the form of a binary layer. You can use beta-galactosidase staining, as we did in our case, or choose your own aging marker. 
 
**Warning!** Be careful when converting the staining image to a binary layer. It is crucial to ensure that the cell positions on the phase-contrast and staining images align correctly; otherwise, the annotation will be inaccurate. If you notice any misalignment during data analysis, consider aligning the paired images. It is possible that images from different cameras may not align perfectly. As an alternative, we suggest following the approach we took. We used the same monochrome camera and applied a red filter to obtain the staining images. To remove unwanted background signals, we also captured the original image using a color camera and adjusted the signal threshold to retain only the regions with actual staining. When choosing the threshold, it is essential to analyze multiple fields of view and cell types. This will help you find the optimal solution. Additionally, we recommend applying a size threshold to the staining spots, which can help address potential false-positive signals. As a result of working with a binary layer and adding a treshhold, you should get a similar image:
![168_0_001_001](https://github.com/voynovaes/Senescence/assets/126082195/bc4125e3-7f63-43f3-baf2-541dbf5427c2)

## Creating a custom image dataset
Next, you need to create the **custom_image_dataset** class, which will generate images of individual cells with the specified size. To do this, use the corresponding code. Don't forget to calculate the mean and std values for the training dataset as they are required for normalizing the resulting images. It is also important to choose the optimal cell image size, which should be specified in the dataset creation code. Afterward, you will be able to create instances of the **train_set** and **test_set** classes, which inherit from the **custom_image_dataset** class. 

## Cell senescence classification model
And finally, to perform the classification of your cells, you can download our [pretrained EfficientNet-B6 model](https://disk.yandex.ru/d/hhs_HskMeTn2zQ) for MSCs.

Please note that if your cells significantly differ in size or morphology from MSCs, the model may perform slightly worse. In such cases, you will likely need to fine-tune the model on your own data.

## Data evaluation
You can evaluate the model using **efficient_netb6_evaluation** code. 

# Full train and validation code
Full train and validation code is available in **model_train_and_test**. Here you can find all steps of this pipeline.

# System requirements
Linux, Windows, and Mac OS are supported for running the code. At least 8GB of RAM is required. 16GB-32GB may be required for larger images. For working with cell image classification, we recommend using a GPU with a minimum of 8 GB of memory size.

# Useful links 
* [Cellpose](https://github.com/MouseLand/cellpose)
* [EfficientNet](https://github.com/lukemelas/EfficientNet-PyTorch)
* [Our dataset](https://disk.yandex.ru/d/2MTM979NveB8tg)
