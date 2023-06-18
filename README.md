# Senescence

# Live microscopic assessment of in multipotent mesenchymal stromal cells senescence 

This pipeline can be used for analyzing cell aging in culture. The pretrained models presented here are designed to work with phase-contrast images of mesenchymal multipotent stromal cells (MSCs). However, you can obtain models that work effectively with other cell types using the same approach.

# Basic usage

First and foremost, you need to use an instance segmentation model to obtain cell masks. We recommend using the LC models from the Cellpose model zoo. The LC4 model performs the best, but please note that it requires significant computational resources. To download our pretrained model for MSC, use the following code:

```python

```

To create your own file for cell annotation, you can refer to the code of CustomImageDataset, which allows you to automatically annotate your cells. For class-based annotation, you will need images of cell staining in the form of a binary layer. You can use beta-galactosidase staining, as we did in our case, or choose your own aging marker.
