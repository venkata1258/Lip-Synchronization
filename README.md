# Lip-Synchronization

DreamTalk

Overview

DreamTalk is an expressive talking head generation system that utilizes Diffusion Probabilistic Models to create realistic lip-synced videos from audio and image inputs. It supports various emotional styles, enabling diverse expressions for a wide range of use cases, such as storytelling, virtual avatars, and educational tools.

Features

Audio-to-Lip Synchronization: Generate realistic lip movements synchronized with the provided audio input.

Emotional Styles: Apply different emotional styles to enhance expressiveness.

Multilingual Support: Preloaded audio samples in multiple languages.

Format Compatibility: Outputs high-quality MP4 videos with AAC audio encoding.

User-Friendly Interface: Gradio-based web interface for easy interaction.

Setup Instructions

Clone Repository

git clone -b dev https://github.com/camenduru/dreamtalk.git
cd dreamtalk

Download Pretrained Checkpoints

wget https://huggingface.co/camenduru/dreamtalk/resolve/main/damo/dreamtalk/checkpoints/denoising_network.pth -O checkpoints/denoising_network.pth
wget https://huggingface.co/camenduru/dreamtalk/resolve/main/damo/dreamtalk/checkpoints/renderer.pt -O checkpoints/renderer.pt

Install Dependencies

pip install -q yacs av gradio

Usage

Launch Interface

Run the script in a Python environment.

Access the Gradio interface through the generated link.

Upload an image and an audio file, or select from available presets.

Choose an emotional style.

Click Run to generate the video output.

Interface Elements

Image Upload: Upload a source image for lip-syncing.

Audio Input: Upload an audio file or select from the provided audio presets.

Emotional Style Dropdown: Choose from various predefined emotional styles.

Output Video: View and download the generated video.

Example Inputs

Images:

Cropped and uncropped images of faces.

Example paths: data/src_img/cropped/chpa5.png

Audio Samples:

Multilingual and noisy audio files.

Examples: acknowledgement_english.m4a, spanish1.wav

Emotional Styles:

Anger, happiness, sadness, etc.

Example: M030_front_happy_level3_001.mat

Output Format

Video format: MP4

Codec: libx264

Audio Codec: AAC
