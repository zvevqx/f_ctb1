title : cli image/video tools ( ffmpeg / imagemagick )
author: zvevqx
published: 2025-11-22
cat: tools
desc: ws

...


# Multimedia Cheat Sheet - Advanced Commands

Here are some advanced commands for two powerful multimedia tools: FFmpeg and ImageMagick.

## FFmpeg Cheat Sheet

FFmpeg is a powerful tool for manipulating video and audio files.

### Basic Commands

| Command | Description |
| --- | --- |
| `ffmpeg -i input.mp4 output.avi` | Convert MP4 file to AVI |
| `ffmpeg -i input.mp4 -ss 00:00:10 -t 00:00:05 output.mp4` | Trim a video from 10 seconds to 15 seconds |
| `ffmpeg -i input.mp4 -vn output.mp3` | Extract audio from a video file |
| `ffmpeg -i input.mp4 -vf "scale=640:360" output.mp4` | Resize a video to 640x360 pixels |

### Advanced Commands

| Command | Description |
| --- | --- |
| `ffmpeg -i input.mp4 -filter_complex "[0:v]split[v1][v2];[v1]scale=640:360[v1out];[v2]scale=1280:720[v2out]" -map "[v1out]" -map "[v2out]" -preset ultrafast -c:v libx264 -c:a copy output.mp4` | Split a video into two different resolutions (640x360 and 1280x720) |
| `ffmpeg -i input.mp4 -i watermark.png -filter_complex "overlay=10:10" output.mp4` | Add a watermark to a video |
| `ffmpeg -i input.mp4 -af "pan=stereo|c0=c1|c1=c0" output.mp4` | Convert mono audio to stereo |
| `ffmpeg -i input.mp4 -c:v libx264 -crf 23 -preset veryslow -c:a copy -movflags +faststart output.mp4` | Encode a video with a CRF value of 23 and a very slow preset, and enable fast start for streaming |

## ImageMagick Cheat Sheet

ImageMagick is a powerful tool for manipulating images.

### Basic Commands

| Command | Description |
| --- | --- |
| `convert input.jpg output.png` | Convert a JPEG file to PNG |
| `convert input.png -resize 50% output.png` | Resize a PNG file to 50% of its original size |
| `convert input.png -rotate 45 output.png` | Rotate a PNG file by 45 degrees |
| `convert input.png -crop 100x100+10+10 output.png` | Crop a 100x100 pixel region of a PNG file, starting from the point (10,10) |

### Advanced Commands

| Command | Description |
| --- | --- |
| `convert input.png -morphology Convolve Sobel:1 output.png` | Apply a Sobel edge detection filter to a PNG file |
| `convert input.png -colorspace Gray -negate output.png` | Convert a PNG file to grayscale and invert its colors |
| `convert input.png -threshold 50% output.png` | Apply a binary threshold to a PNG file |
| `convert input1.png input2.png -compose Difference -composite -normalize output.png` | Compute the absolute difference between two PNG files |

### Batch Processing with Mogrify

ImageMagick's `mogrify` command allows you to process multiple images in a directory at once. Here are some useful commands:

| Command | Description |
| --- | --- |
| mogrify -resize 50% *.jpg | Resize all JPEG files in the current directory to 50% of their original size |
| mogrify -format png *.jpg | Convert all JPEG files in the current directory to PNG |
| mogrify -rotate 90 *.png | Rotate all PNG files in the current directory by 90 degrees |
| mogrify -strip *.jpg | Remove EXIF data from all JPEG files in the current directory |

Note that mogrify modifies the original files in place, so be sure to make a backup of your files before using this comman| --- | --- |
| mogrify -resize 50% *.jpg | Resize all JPEG files in the current directory to 50% of their original size |
| mogrify -format png *.jpg | Convert all JPEG files in the current directory to PNG |
| mogrify -rotate 90 *.png | Rotate all PNG files in the current directory by 90 degrees |
| mogrify -strip *.jpg | Remove EXIF data from all JPEG files in the current directory |

**Note that mogrify modifies the original files in place, so be sure to make a backup of your files before using this command**.
