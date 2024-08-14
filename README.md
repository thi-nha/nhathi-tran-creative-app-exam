# nhathi-tran-creative-app-exam
Final assignment for the seminar "Creative applications of Python and AI" of the summer semester 2024.

# **Flower Image and Video Generator**

## **Project Overview**
This project creates artistic images of a flower with varying petal colors using Python's Pillow library. The project generates a series of images and compiles them into a video. Additionally, the video is converted into a GIF, and a music file is generated and combined with the video to produce a final multimedia piece.

## **Installation Instructions**
To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/flower-image-video-generator.git

2. Navigate to the Project Directory:
cd flower-image-video-generator

3. Install the Required Dependencies:
Ensure you have Python 3.6 or higher installed. Then, install the dependencies using pip:
pip install -r requirements.txt

Usage Instructions
To generate the flower images, video, and add music:

1. Run the Python Script:

bash

python clean_create_flower.py


Output Files:

The generated images will be saved in the images directory.
The video will be saved as flower.mp4 in the video directory.
The GIF will be saved as flower.gif in the video directory.
The music file will be saved as audio.wav in the music directory.
The final video with music will be saved as flower_w_music.mp4 in the final_result directory.

Methodology
Idea and Motivation
The project was inspired by the intersection of art and programming. The goal was to create visually appealing, algorithmically generated images of a flower and compile them into a multimedia presentation.

Development Process
Research:

Investigated various image generation techniques using the Pillow library.
Explored methods for combining images into videos and adding music using MoviePy and other Python tools.
Implementation:

Image Generation: Multiple images of a flower are generated with varying petal colors.
Video Creation: The images are compiled into a video, repeated twice to create a longer sequence.
GIF Creation: The video is converted into a GIF.
Music Generation: A music file is generated based on a text prompt using a pre-trained model.
Final Video: The music is added to the video, creating the final multimedia piece.
Screenshots or Video
Include a screenshot of the generated flower images or a link to the final video demonstrating the project in action.

Credits
This project uses the following libraries and resources:

Pillow: For image creation and manipulation.
OpenCV: For video creation.
MoviePy: For video and GIF processing.
Transformers (HuggingFace): For generating music using a pre-trained model.
