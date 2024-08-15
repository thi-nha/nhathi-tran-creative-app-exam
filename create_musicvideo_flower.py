from PIL import Image, ImageDraw
import os
import sys

# Check if a directory is provided as an argument; if not, default to 'images'
if len(sys.argv) != 2:
    directory = "images"
else:
    directory = sys.argv[1]  # sys.argv[1] is the directory provided as an argument

# Create the directory if it does not exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Function to save images in the specified directory
def save_image(image, filename):
    filepath = os.path.join(directory, filename)
    image.save(filepath)

# Define image size
width, height = 400, 400
# Create a new image with a white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Define colors for drawing
yellow = (8, 25, 85)
blue = (18, 238, 234)
green = (144, 0, 223)
red = (186, 7, 1)
kern = (231, 255, 8)
leave = (115, 235, 130)
black = (0, 0, 0)

# Function to draw leaves
def draw_leaf(x, y, width, height, color):
    draw.polygon([(x, y), (x+width, y-height), (x-width, y-height)], fill=color, outline='black')

# Function to draw flower petals
def draw_petal(x, y, radius, color):
    draw.ellipse((x-radius, y-radius, x+radius, y+radius), fill=color, outline='black')

# Create the first image
draw.line((30, 150, 80, 200), fill='blue', width=3)  # Draw a blue line for rain for rain
draw.line((80, 50, 130, 100), fill='blue', width=3)  
draw.line((250, 30, 300, 80), fill='blue', width=3)  
draw.line((310, 50, 360, 100), fill='blue', width=3)  
draw.line((0, 30, 30, 60), fill='blue', width=3)  

# Define positions and sizes for leaves
leaf_positions = [(160, 330), (240, 370)]
leaf_width, leaf_height = 45, 20

# Draw leaves at specified positions
for pos in leaf_positions:
    draw_leaf(pos[0], pos[1], leaf_width, leaf_height, leave)

draw.line((200, 250, 200, 400), fill='green', width=10)  # Draw the stem

# Define positions and colors for petals
petal_positions = [(200, 160), (240, 200), (200, 240), (160, 200)]
petal_colors = [yellow, blue, green, red]
petal_radius = 50  # Set petal size

# Draw petals at specified positions with specified colors
for i, pos in enumerate(petal_positions):
    draw_petal(pos[0], pos[1], petal_radius, petal_colors[i])

draw_petal(200, 200, 20, kern)  # Draw the flower's center

# Save the first image
save_image(image, '1.png')

# Create the second image (with different petal color order)
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
draw.line((80, 200, 130, 250), fill='blue', width=3)  # Draw a blue line for rain for rain
draw.line((130, 100, 180, 150), fill='blue', width=3) 
draw.line((300, 80, 350, 130), fill='blue', width=3)  
draw.line((360, 100, 410, 150), fill='blue', width=3)  
draw.line((50, 80, 80, 110), fill='blue', width=3)  

# Draw leaves at specified positions
for pos in leaf_positions:
    draw_leaf(pos[0], pos[1], leaf_width, leaf_height, leave)

draw.line((200, 250, 200, 400), fill='green', width=10)  # Draw the stem

# Change petal color order for this image
petal_colors = [red, yellow, blue, green]

# Draw petals with the new color order
for i, pos in enumerate(petal_positions):
    draw_petal(pos[0], pos[1], petal_radius, petal_colors[i])

draw_petal(200, 200, 20, kern)  # Draw the flower's center

# Save the second image
save_image(image, '2.png')

# Create the third image (with different petal color order)
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
draw.line((120, 240, 170, 290), fill='blue', width=3)  # Draw a blue line for rain
draw.line((170, 140, 220, 190), fill='blue', width=3)  
draw.line((340, 120, 390, 170), fill='blue', width=3)  
draw.line((400, 140, 450, 190), fill='blue', width=3)  
draw.line((90, 120, 120, 150), fill='blue', width=3)  

# Draw leaves at specified positions
for pos in leaf_positions:
    draw_leaf(pos[0], pos[1], leaf_width, leaf_height, leave)

draw.line((200, 250, 200, 400), fill='green', width=10)  # Draw the stem

# Change petal color order for this image
petal_colors = [green, red, yellow, blue]

# Draw petals with the new color order
for i, pos in enumerate(petal_positions):
    draw_petal(pos[0], pos[1], petal_radius, petal_colors[i])

draw_petal(200, 200, 20, kern)  # Draw the flower's center

# Save the third image
save_image(image, '3.png')

# Create the fourth image (with different petal color order)
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
draw.line((180, 300, 230, 350), fill='blue', width=3)  # Draw a blue line for rain
draw.line((210, 220, 260, 270), fill='blue', width=3)  
draw.line((400, 180, 450, 230), fill='blue', width=3)  
draw.line((450, 190, 500, 240), fill='blue', width=3)  
draw.line((140, 170, 170, 190), fill='blue', width=3)  

# Draw leaves at specified positions
for pos in leaf_positions:
    draw_leaf(pos[0], pos[1], leaf_width, leaf_height, leave)

draw.line((200, 250, 200, 400), fill='green', width=10)  # Draw the stem

# Change petal color order for this image
petal_colors = [blue, green, red, yellow]

# Draw petals with the new color order
for i, pos in enumerate(petal_positions):
    draw_petal(pos[0], pos[1], petal_radius, petal_colors[i])

draw_petal(200, 200, 20, kern)  # Draw the flower's center

# Save the fourth image
save_image(image, '4.png')

# Show the last created image
image.show()

# Create the fifth image
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)
draw.line((30, 150, 80, 200), fill='blue', width=3)  # Draw a blue line for rain
draw.line((80, 50, 130, 100), fill='blue', width=3)  
draw.line((250, 30, 300, 80), fill='blue', width=3) 
draw.line((310, 50, 360, 100), fill='blue', width=3)  
draw.line((0, 30, 30, 60), fill='blue', width=3)  

# Draw leaves at specified positions
for pos in leaf_positions:
    draw_leaf(pos[0], pos[1], leaf_width, leaf_height, leave)

draw.line((200, 250, 200, 400), fill='green', width=10)  # Draw the stem

# Define petal positions and colors
petal_positions = [(200, 160), (240, 200), (200, 240), (160, 200)]
petal_colors = [yellow, blue, green, red]  # Set the petal colors for this image
petal_radius = 50  # Set petal size

# Draw petals at specified positions
for i, pos in enumerate(petal_positions):
    draw_petal(pos[0], pos[1], petal_radius, petal_colors[i])

draw_petal(200, 200, 20, kern)  # Draw the flower's center

# Save the fifth image
save_image(image, '5.png')

import sys
import cv2
import os
import glob

img_array = []

# Check if a directory is provided as an argument; if not, default to 'images'
if len(sys.argv) != 2:
    directory = "images"
else:
    directory = sys.argv[1]

# Function to sort files numerically by their name
def get_key(fp):
    """Sort files numerically based on their filename."""
    filename = os.path.splitext(os.path.basename(fp))[0]
    int_part = filename.split()[0]
    return int(int_part)

# Read and sort image files
for filename in sorted(glob.glob(f'{directory}/*.png'), key=get_key):
    print(filename)
    img = cv2.imread(filename)  # Load the image
    height, width, layers = img.shape  # Get image dimensions
    size = (width, height)  # Define size for video
    img_array.append(img)  # Add image to list

# Create the video directory if it does not exist
if not os.path.exists("video"):
    os.makedirs("video")

# Initialize the VideoWriter
out = cv2.VideoWriter('video/flower.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, size)

# Factor to repeat each image frame (e.g., 15 times)
frame_repeat = 15

# Repeat the image sequence twice
for _ in range(2):  # The sequence will play twice
    for img in img_array:  # For each image in the list
        for _ in range(frame_repeat):  # Write the same image multiple times to extend its display duration
            out.write(img)

# Release the video writer
out.release()

from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("video/flower.mp4")  # Load the video
videoClip.write_gif("video/flower.gif")  # Convert the video to GIF

from transformers import AutoProcessor, MusicgenForConditionalGeneration
import scipy
import datetime

# Create the music directory if it does not exist
if not os.path.exists("music"):
    os.makedirs("music")

# Load the pretrained model for music generation
model_name = "facebook/musicgen-small"
processor = AutoProcessor.from_pretrained(model_name)
model = MusicgenForConditionalGeneration.from_pretrained(model_name)

# Define the prompt for music generation
prompt = ['lofi kpop']  # Text prompt to guide music generation

# Prepare input for the model
inputs = processor(text=prompt, padding=True, return_tensors='pt')
audio_values = model.generate(**inputs, max_new_tokens=512)  # Generate music

# Save the generated music as a WAV file
scipy.io.wavfile.write(f"music/audio.wav",
                  rate=model.config.audio_encoder.sampling_rate,
                  data=audio_values[0,0].numpy())

print('SUCCESS')

import moviepy.editor as mp

video1 = mp.VideoFileClip("video/flower.mp4")  # Load the video
final = video1.set_audio(mp.AudioFileClip("music/audio.wav"))  # Add the generated music to the video

# Create the final result directory if it does not exist
if not os.path.exists("final_result"):
    os.makedirs("final_result")

# Save the final video with music
final.write_videofile("final_result/flower_w_music.mp4",
                      fps=60,
                      audio_codec="aac",
                      audio_bitrate="192k")
