# **nhathi-tran-creative-app-exam**
Final assignment for the seminar "Creative applications of Python and AI" of the summer semester 2024.

## **Project Overview**
This project creates images of a flower with varying petal colors using Python's Pillow library. The project generates a series of images and compiles them into a video. Additionally, the video is converted into a GIF (that will bes used later for the QR Code below), and a music file is generated by an AI and combined with the video to produce a final multimedia piece.

## **Installation Instructions**
To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/thi-nha/nhathi-tran-creative-app-exam.git

2. **Navigate to the Project Directory:**
   ```bash
   cd nhathi-tran-creative-app-exam

3. **Install the Required Dependencies:**
To run the code you'll need to install the following packages using pip:
   ```bash
   pip install Pillow
   pip install opencv-python
   pip install moviepy
   pip install transformers
   pip install scipy

Additionally, you need to ensure that ffmpeg is installed, as MoviePy requires it for video and audio processing. You can install it via the package manager on most systems:
   - **macOS**: brew install ffmpeg
   - **Windows**: https://ffmpeg.org/download.html
   

## **Usage Instructions**
To generate the flower images, video, and add music:

1. **Run the Python Script:**
   ```bash
   python create_musicvideo_flower.py

2. **Output Files:**
   - The generated images will be saved in the images directory.
   - The video will be saved as flower.mp4 in the video directory.
   - The GIF will be saved as flower.gif in the video directory.
   - The music file will be saved as audio.wav in the music directory.
   - The final video with music will be saved as flower_w_music.mp4 in the final_result directory.

## **Methodology**
### **Idea and Motivation**
My idea was to take the inputs from the seminars on the various creative possibilities of using Python and ultimately summarize them in a multimedia video. Art also means drawing inspiration from others and experimenting with what has been learned to create something new.
I adapted and expanded upon the code snippets that we discussed piece by piece in the seminars, to create a music file using AI and compile images into a video.
The goal was to create images of a flower and compile them into a multimedia video that includes an audio file generated through Python using AI.


### **Development Process**
**1. Research:**
- Investigated various image generation techniques using the Pillow library.
- Explored methods for combining images into videos and adding music using MoviePy and other Python tools.

**2. Implementation:**
- **Image Generation**: Multiple images of a flower are generated with varying petal colors.
- **Video Creation**: The images are compiled into a video, repeated twice to create a longer sequence.
- **GIF Creation**: The video is converted into a GIF.
- **Music Generation**: A music file is generated based on a text prompt using a pre-trained model.
- **Final Video**: The music is added to the video, creating the final multimedia piece.

## **Video**
Here is a QR Code to my video where you can see my demo of creating a musicvideo.

![](QR_to_myVideo.gif)

By the way, I also uploaded the code for this QR code, although it's not the primary art artifact 😊.

## **Credits**
This project uses the following libraries and resources:
- **Pillow**: For image creation and manipulation.
- **OpenCV**: For video creation.
- **MoviePy**: For video and GIF processing.
- **Transformers** (HuggingFace): For generating music using a pre-trained model.
- **SciPy**: For saving the generated audio as a WAV file.
  
## **License**
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. 

...To be honest, I'm not entirely sure if this section is necessary or what exactly should be included. I apologize for any confusion.
