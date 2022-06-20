# Image_compression_k_means_clustering

This project is a lightweight Web App, <b>Flask</b> is used to serve the static HTML files and as a server.

It uses <b> K-Means </b>, A Machine Learning clustering algorithm, to cluster all the colors in an image into N(specified by user) clusters. It replaces the RGB value of every pixel with the RGB value of their respective cluster center which results in reducing the amount of memory required to save a picture.




### Algorithm :  K-means Clustering

<img src="./app/assets/Kmeans_animation.gif" alt="Kmeans_animation.gif">


### Comparison


#### Original Image(177kb) &#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195; Compressed Image(61kb)
 
<div>
<img src="./app/assets/palm_trees.jpg" alt="palm_trees.jpg" width = 250>
 &#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;&#8195;
<img src="./app/assets/compressed_image.png" alt="compressed_image.png" width = 250>
</div>






#### Web App - Demo


<img src="./app/assets/k-means_img_compression-demo.gif" alt="demo.gif" width = 600>






