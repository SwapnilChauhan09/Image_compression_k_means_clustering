# import files
from flask import Flask,request,jsonify,send_file
import base64
from skimage import io
from sklearn.cluster import KMeans
import numpy as np

# create flask App

app = Flask(__name__)

@app.route('/')
def index():
    return '''Server Works!<hr>
<form action="/processing" method="POST" enctype="multipart/form-data">
<input type="file" name="image">
<button>OK</button>
</form>    
'''
@app.route("/compress", methods = ["POST"])
def get_compressed_img():
    return send_file('./assets/palm_trees.jpg', mimetype='image/gif')

    
@app.route('/processing', methods=['POST'])
def process():
    # read image
    file = request.files['image']  
    img = io.imread(file)

    # get the height width and dimension
    (row,column,dimension) =  img.shape

    # flatten the image
    flat_img = img.reshape(row * column,dimension)

    # fit the model
    k_mean = KMeans(n_clusters=2)
    k_mean.fit(flat_img)

    # map it with nearest cluster
    compressed_image = k_mean.cluster_centers_[k_mean.labels_]

    # clip the range
    compressed_image = np.clip(compressed_image.astype('uint8'), 0, 255)

    # reshape image
    compressed_image = compressed_image.reshape(row,column,3)

    # save 
    io.imsave('./assets/compressed_image.png', compressed_image)

    return send_file('./assets/compressed_image.png', mimetype='image/gif')
  

if __name__ == "__main__":
    pass
    
# run the App
app.run(port=8080, debug = True)