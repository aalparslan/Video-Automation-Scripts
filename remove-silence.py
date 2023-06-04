import moviepy.editor as mp
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from joblib import Parallel, delayed
from tqdm import tqdm

def process_section(video_path, start, end, margin_duration):
    video = mp.VideoFileClip(video_path)
    
    # Extract the audio from the video
    audio = video.audio
    
    # Convert the audio to pydub's AudioSegment format
    audio = AudioSegment.from_file(video_path)
    
    # Calculate the duration in milliseconds
    duration = end - start
    
    # Add margin to the start and end time
    start_with_margin = max(0, start - margin_duration)
    end_with_margin = min(audio.duration_seconds * 1000, end + margin_duration)
    
    # Create a new video clip with the specified section
    section_clip = video.subclip(start_with_margin / 1000, end_with_margin / 1000)
    
    return section_clip

def remove_silence(video_path, output_path, decibel_threshold, min_section_duration, margin_duration):
    video = mp.VideoFileClip(video_path)
    
    # Extract the audio from the video
    audio = video.audio
    
    # Convert the audio to pydub's AudioSegment format
    audio = AudioSegment.from_file(video_path)
    
    # Display progress while computing non-silent sections
    print("Computing non-silent sections...")
    
    # Detect non-silent sections
    non_silent_sections = detect_nonsilent(audio, min_silence_len=min_section_duration, silence_thresh=decibel_threshold)
    
    # Create a new video clip with proper audio using multiprocessing
    new_clips = []
    
    # Iterate over non-silent sections and process them one by one
    for start, end in tqdm(non_silent_sections, desc="Processing", unit=" section"):
        if end - start > min_section_duration:
            # Process the section and add it to the new clips list
            new_clip = process_section(video_path, start, end, margin_duration)
            new_clips.append(new_clip)
    
    # Concatenate the new video clips
    final_video = mp.concatenate_videoclips(new_clips)
    
    # Save the modified video to the output path
    final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")

# Example usage
video_path = "/Users/guest/Desktop/deneme/x.mp4"
output_path = "/Users/guest/Desktop/deneme/output_video.mp4"
decibel_threshold = -50
min_section_duration = 600  # milliseconds
margin_duration = 200  # milliseconds

remove_silence(video_path, output_path, decibel_threshold, min_section_duration, margin_duration)
