[image1]: ./code_images/image_1.png
[image2]: ./code_images/image_2.png
[image3]: ./code_images/image_3.png
[image4]: ./code_images/image_4.png
[image5]: ./code_images/image_5.png
[image6]: ./code_images/image_6.png

# Face Dataset Generator
This simple program was developed to help in generation datasets that you can <br> use for facial detection and recognition models. <br>
The program uses OpenCV's <b><i>haarcascade_frontalface_alt2.xml</i></b> for <br> face detection then the detected face is saved in the folder you specify. <br>
For this program images would be saved under a folder called <b><i>images</i></b> already <br> specified for you and a subfolder which you'll specifiy yourself, e.g <b><i>martin</i></b>

# How to
- Create a virtual environment: <br>
<code>virtualenv dataset</code>
- Start the environment: (Linux)<br>
<code>source dataset/bin/activate</code>
- Use pip to install dependencies: <br>
<code>pip3 install -r requirements.txt</code>
- Run the generator: <br>
<code>python3 dataset_maker.py</code> <br>
This should prompt you for a folder name as below <br>
![image1] <br>
Once you click <b><i>Entr</i></b>, a video stream will start showing. <b><i>A green bounding box indicates that images are being saved</i></b>.
![image2] <br>
- The directories are <br>
![image3] ![image4] ![image5]
<br>
- Sample image <br>
![image6]
- To quit press <b><i>Q</i></b>