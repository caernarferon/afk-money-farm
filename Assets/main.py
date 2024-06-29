import os
import random
from moviepy.editor import VideoFileClip, ImageClip, TextClip, CompositeVideoClip

# Paths
flags_path = r"C:\Users\panjw_gco4a0t\Documents\GitHub\afk-money-farm\Assets\Flags"
templates_path = r"C:\Users\panjw_gco4a0t\Documents\GitHub\afk-money-farm\Assets\Templates"
output_path = r"C:\Users\panjw_gco4a0t\Documents\GitHub\afk-money-farm\OUTPUT"

# Load Templates
template_files = [os.path.join(templates_path, file) for file in os.listdir(templates_path) if file.endswith('.mp4')]

# Load Flags
flag_files = [os.path.join(flags_path, file) for file in os.listdir(flags_path) if file.endswith('.png')]

# Function to create a video with a specific template and random flags
def create_video(template_file, video_id):
    template_clip = VideoFileClip(template_file)

    # Randomly select three flags
    selected_flags = random.sample(flag_files, 3)
    
    # Define timestamps
    timestamps = [
        (3.08, 7.24),  # First flag
        (9.00, 13.16), # Second flag
        (14.27, 19.13) # Third flag
    ]
    
    answers_timestamps = [
        (7.25, 8.24),  # First answer
        (13.24, 14.25), # Second answer
        (19.23, 20.24) # Third answer
    ]

    # Create text and image clips for each flag segment
    segments = [template_clip]

    for i, (flag, timestamp, answer_timestamp) in enumerate(zip(selected_flags, timestamps, answers_timestamps)):
        flag_clip = (ImageClip(flag)
                     .set_duration(timestamp[1] - timestamp[0])
                     .resize(height=1920)  # Adjust height to fit 9:16 aspect ratio
                     .set_position('center')
                     .set_start(timestamp[0])
                     .set_end(timestamp[1]))

        answer_text = os.path.splitext(os.path.basename(flag))[0]
        answer_clip = (TextClip(answer_text, fontsize=70, color='white')
                       .set_duration(answer_timestamp[1] - answer_timestamp[0])
                       .set_position('center')
                       .set_start(answer_timestamp[0])
                       .set_end(answer_timestamp[1]))

        segments.extend([flag_clip, answer_clip])

    # Composite all segments
    final_clip = CompositeVideoClip(segments, size=template_clip.size)

    # Export the final video
    output_filename = os.path.join(output_path, f"VID{video_id}.mp4")
    final_clip.write_videofile(output_filename, codec="libx264")

# Generate videos
for i in range(1, 4):  # Example: Generate 3 videos
    template_file = random.choice(template_files)
    create_video(template_file, i)
