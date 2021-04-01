# baidu-ai
### Public Dataset
1. FGNET
 - Link: https://yanweifu.github.io/FG_NET_data/
 - Description: 
 - ./images folder: all human face images. The groundtruth is used to name each image. For example, 078A11.JPG, means that this is the No.'78' person's image when he/she was 11 years old. 'A' is short for Age.
 - ./points folder: this is the 68 manual annotated points for each image in ./images folder.
The annotated data is of much higher quality than another dataset e.g. MORPH (saved in /export/beware/thumper/yf300/Age_estimation_org_data_backup/ageEstimation/MOPRH). However, MORPH is much bigger dataset than FG-NET.
 
2. CACD_VS
 - Link: https://bcsiriuschen.github.io/CARC/
 - Desc: The dataset contains 4,000 image pairs divided by ten folds. Identities in each fold are mutually exclusive. The images are named as pairId_0.jpg and pairId_1.jpg for each pair. First 400 image pairs [(0000_0.jpg,0000_1.jpg) - (0399_0.jpg,0399_1.jpg)] are first fold, in which first 200 image pairs (i.e. 0000 - 0199) are positive pairs and second 200 image pairs (i.e. 0200 - 0399) are negative pairs. The second fold contains image pair (0400 - 0799) and so on.
