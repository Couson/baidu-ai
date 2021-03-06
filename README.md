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

 3. MORPH Album 2 -- this isn't free; need to purchase the academic version for #$99.
 -  Link: 
  -  [1] http://www.cbsr.ia.ac.cn/users/dyi/agr.html
  -  [2] https://ebill.uncw.edu/C20231_ustores/web/classic/product_detail.jsp?PRODUCTID=8
 -  Desc: MORPH Album 2 [1] contains about 55,000 face images of more than 13,000 subjects. The capture time spans from 2003 to 2007. Age ranges from 16 to 77 years. Although it is a good and large database, the distributions of gender and ethnicity are uneven. The Male-Female ratio is about 5.5 : 1 and the White-Black ratio is about 4 : 1. Except for White and Black, the proportion of other ethnicity is very low (4%). For more information, refer to the link posted.

4. LFW
 - Link: http://vis-www.cs.umass.edu/lfw
 - Desc: Welcome to Labeled Faces in the Wild, a database of face photographs designed for studying the problem of unconstrained face recognition. The data set contains more than 13,000 images of faces collected from the web. Each face has been labeled with the name of the person pictured. 1680 of the people pictured have two or more distinct photos in the data set. The only constraint on these faces is that they were detected by the Viola-Jones face detector. More details can be found in the technical report below. There are now four different sets of LFW images including the original and three different types of "aligned" images. The aligned images include "funneled images" (ICCV 2007), LFW-a, which uses an unpublished method of alignment, and "deep funneled" images (NIPS 2012). Among these, LFW-a and the deep funneled images produce superior results for most face verification algorithms over the original images and over the funneled images (ICCV 2007).

### Private Dataset
1. CAF
2. ITWCC
