# -*- coding: utf-8 -*-
"""Lip Synchronization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/107UzH8ughW3Uqa2nfPHRkqk3SU5auKDT
"""

# Commented out IPython magic to ensure Python compatibility.
# %cd /content
!git clone -b dev https://github.com/camenduru/dreamtalk
# %cd /content/dreamtalk

!wget https://huggingface.co/camenduru/dreamtalk/resolve/main/damo/dreamtalk/checkpoints/denoising_network.pth -O /content/dreamtalk/checkpoints/denoising_network.pth
!wget https://huggingface.co/camenduru/dreamtalk/resolve/main/damo/dreamtalk/checkpoints/renderer.pt -O /content/dreamtalk/checkpoints/renderer.pt

!pip install -q yacs av gradio

# https://huggingface.co/spaces/fffiloni/dreamtalk/blob/main/app.py modified

import gradio as gr
import subprocess
from moviepy.editor import VideoFileClip
import datetime

def convert_to_mp4_with_aac(input_path, output_path):
    video = VideoFileClip(input_path)
    video.write_videofile(output_path, codec="libx264", audio_codec="aac")
    return output_path

def check_file_exists(file_path, audio_list):
    return file_path in audio_list

def load_audio(audio_listed):
    if audio_listed is None:
        return None
    else:
        return f"data/audio/{audio_listed}"

def execute_command(command: str) -> None:
    subprocess.run(command, check=True)

def infer(audio_input, image_path, emotional_style):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_name = f"lipsynced_result_{timestamp}"
    command = [
        f"python",
        f"inference_for_demo_video.py",
        f"--wav_path={audio_input}",
        f"--style_clip_path=data/style_clip/3DMM/{emotional_style}",
        f"--pose_path=data/pose/RichardShelby_front_neutral_level1_001.mat",
        f"--image_path={image_path}",
        f"--cfg_scale=1.0",
        f"--max_gen_len=30",
        f"--output_name={output_name}"
    ]

    execute_command(command)
    input_file = f"output_video/{output_name}.mp4"
    output_file = f"{output_name}.mp4"
    result = convert_to_mp4_with_aac(input_file, output_file)
    return result

css="""
#project-links{
    margin: 0 0 12px !important;
    column-gap: 8px;
    display: flex;
    justify-content: center;
    flex-wrap: nowrap;
    flex-direction: row;
    align-items: center;
}
"""
with gr.Blocks(css=css) as demo:
    with gr.Column(elem_id="col-container"):
        gr.HTML("""
        <h2 style="text-align: center;">DreamTalk</h2>
        <p style="text-align: center;">When Expressive Talking Head Generation Meets Diffusion Probabilistic Models</p>
        """)
        with gr.Row():
            with gr.Column():
                image_path = gr.Image(label="Image", type="filepath", sources=["upload"])
                audio_input = gr.Audio(label="Audio input", type="filepath", sources=["upload"], value="data/audio/acknowledgement_english.m4a")
                with gr.Row():
                    audio_list = gr.Dropdown(
                        label="Choose an audio (optional)",
                        choices=[
                            "German1.wav", "German2.wav", "German3.wav", "German4.wav",
                            "acknowledgement_chinese.m4a", "acknowledgement_english.m4a",
                            "chinese1_haierlizhi.wav", "chinese2_guanyu.wav",
                            "french1.wav", "french2.wav", "french3.wav",
                            "italian1.wav", "italian2.wav", "italian3.wav",
                            "japan1.wav", "japan2.wav", "japan3.wav",
                            "korean1.wav", "korean2.wav", "korean3.wav",
                            "noisy_audio_cafeter_snr_0.wav", "noisy_audio_meeting_snr_0.wav", "noisy_audio_meeting_snr_10.wav", "noisy_audio_meeting_snr_20.wav", "noisy_audio_narrative.wav", "noisy_audio_office_snr_0.wav", "out_of_domain_narrative.wav",
                            "spanish1.wav", "spanish2.wav", "spanish3.wav"
                            ],
                        value = "acknowledgement_english.m4a"
                    )
                    audio_list.change(
                        fn = load_audio,
                        inputs = [audio_list],
                        outputs = [audio_input]
                    )
                    emotional_style = gr.Dropdown(
                        label = "emotional style",
                        choices = [
                            "M030_front_angry_level3_001.mat",
                            "M030_front_contempt_level3_001.mat",
                            "M030_front_disgusted_level3_001.mat",
                            "M030_front_fear_level3_001.mat",
                            "M030_front_happy_level3_001.mat",
                            "M030_front_neutral_level1_001.mat",
                            "M030_front_sad_level3_001.mat",
                            "M030_front_surprised_level3_001.mat",
                            "W009_front_angry_level3_001.mat",
                            "W009_front_contempt_level3_001.mat",
                            "W009_front_disgusted_level3_001.mat",
                            "W009_front_fear_level3_001.mat",
                            "W009_front_happy_level3_001.mat",
                            "W009_front_neutral_level1_001.mat",
                            "W009_front_sad_level3_001.mat",
                            "W009_front_surprised_level3_001.mat",
                            "W011_front_angry_level3_001.mat",
                            "W011_front_contempt_level3_001.mat",
                            "W011_front_disgusted_level3_001.mat",
                            "W011_front_fear_level3_001.mat",
                            "W011_front_happy_level3_001.mat",
                            "W011_front_neutral_level1_001.mat",
                            "W011_front_sad_level3_001.mat",
                            "W011_front_surprised_level3_001.mat"
                        ],
                        value = "M030_front_neutral_level1_001.mat"
                    )
                gr.Examples(
                    examples = [
                        "data/src_img/uncropped/face3.png",
                        "data/src_img/uncropped/male_face.png",
                        "data/src_img/uncropped/uncut_src_img.jpg",
                        "data/src_img/cropped/chpa5.png",
                        "data/src_img/cropped/cut_img.png",
                        "data/src_img/cropped/f30.png",
                        "data/src_img/cropped/menglu2.png",
                        "data/src_img/cropped/nscu2.png",
                        "data/src_img/cropped/zp1.png",
                        "data/src_img/cropped/zt12.png"
                    ],
                    inputs=[image_path],
                    examples_per_page=5
                )
                with gr.Row():
                    gr.ClearButton([audio_input, image_path, audio_list])
                    run_btn = gr.Button("Run", elem_id="run-btn")
            with gr.Column():
                output_video = gr.Video(format="mp4")
                gr.HTML("""
                <p id="project-links" align="center">
                  <a href='https://dreamtalk-project.github.io/'><img src='https://img.shields.io/badge/Project-Page-Green'></a> <a href='https://arxiv.org/abs/2312.09767'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a> <a href='https://youtu.be/VF4vlE6ZqWQ'><img src='https://badges.aleen42.com/src/youtube.svg'></a>
                </p>
                <img src="https://github.com/ali-vilab/dreamtalk/raw/main/media/teaser.gif" style="margin: 0 auto;border-radius: 10px;" />
                """)

    run_btn.click(
        fn = infer,
        inputs = [audio_input, image_path, emotional_style],
        outputs = [output_video]
    )

demo.queue().launch(inline=False, share=True, debug=True)