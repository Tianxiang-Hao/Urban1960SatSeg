# Urban1960SatSeg: Unsupervised Semantic Segmentation of Mid-20<sup>th</sup> century Urban Landscapes with Satellite Imageries
The appendix and supplementary materials are available at the following link:[🔗 Appendix and Supplementry](https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/appendix_and_supplementary.pdf)

## 🌍 Overview

<div align="center">
  <img src="https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/pictures/Intro.png" style="width: 80%;">
</div>

## 📊 Datasets

<div align="center">
  <img src="https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/pictures/relatedwork.jpg" style="width: 50%;">
</div>

Visualization of high-resolution remote sensing segmentation datasets by year, resolution, and coverage. More recent datasets show greater diversity in resolution and extent, while Urban1960SatBench is the earliest with relatively high resolution, bridging a key temporal gap.
### 🔧 How to use
<div align="center">
  <img src="https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/pictures/dataset.png" style="width: 70%;">
</div>

Urban1960SatBench is a high-fidelity, city-scale semantic segmentation benchmark derived from declassified 1964 Keyhole (KH-4A) panchromatic satellite imagery co-registered with the 1965 official Xi’an urban distribution map. Through rigorous geo-referencing and expert manual annotation, the dataset provides pixel-level labels for impervious surfaces and four urban land-use categories (roads, buildings, water bodies and other urban types). Xi’an, as one of China’s oldest capitals, exhibits a unique juxtaposition of millennia-old cultural heritage and modern urbanization pressures. Consequently, Urban1960SatBench not only pioneers historical urban analysis using reconnaissance imagery but also establishes a challenging domain for segmentation models, owing to grayscale distortions and limited spatial resolution. This dataset facilitates studies in historical urban morphology reconstruction, cultural heritage conservation, and cross-temporal model generalization, offering a foundational resource for both Remote Sensing (RS) and Computer Vision (CV) communities.

#### Data preparation
To access the full dataset, you can download it from:[🔗 Urban1960SatBench](https://doi.org/10.7910/DVN/HT2B1S)

The usage examples of the data are in the Python files [Urban1960SatSS](https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/datasets/urban1960satss.py) and [Urban1960SatISP](https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/datasets/urban1960satisp.py)

Note: This version is the next iteration after optimizing the details in the article, and there are slight differences in the paper version.

## 📊 Model
<div align="center">
  <img src="https://github.com/Tianxiang-Hao/Urban1960SatSeg/blob/main/pictures/model.png" style="width: 70%;">
</div>

### Model details will be announced soon...

## 📢 Reference & Statement
The architecture of the Model is mainly referenced from [Dino](https://github.com/facebookresearch/dino),[Dinov2](https://github.com/facebookresearch/dinov2), [SAM2](https://github.com/facebookresearch/sam2) and [Primaps](https://github.com/visinf/primaps). 

All experiments are carried out on NVIDIA 4090.

Urban1960SatSeg will be continuously updated to include additional locations, time periods, and other categories, supporting broader research on early urban development processes and image segmentation.

## Citing Urban1960SatSeg

If you find this datasets or repository useful, please consider giving a star :star: and citation :t-rex::

```
@misc{hao2025urban1960satsegunsupervisedsemanticsegmentation,
      title={Urban1960SatSeg: Unsupervised Semantic Segmentation of Mid-20$^{th}$ century Urban Landscapes with Satellite Imageries}, 
      author={Tianxiang Hao and Lixian Zhang and Yingjia Zhang and Mengxuan Chen and Jinxiao Zhang and Haohuan Fu},
      year={2025},
      eprint={2506.09476},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2506.09476}, 
}
```
```
@data{DVN/HT2B1S_2025,
author = {Hao, Tianxiang and Zhang,Lixian and Zhang,Yingjia and Chen, Mengxuan and Zhang,Jinxiao and Fu,Haohuan},
publisher = {Harvard Dataverse},
title = {{Urban1960SatBench}},
year = {2025},
version = {V1},
doi = {10.7910/DVN/HT2B1S},
url = {https://doi.org/10.7910/DVN/HT2B1S}
}
```
