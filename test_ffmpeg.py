
import os
import soundfile
import subprocess

# 安装 FFmpeg 并配置环境变量
# https://zhuanlan.zhihu.com/p/692019886

# Check if FFmpeg is installed and print version information

try:
    result = subprocess.run(['ffmpeg', '-version'], capture_output=True, text=True)
    print("FFmpeg 版本信息：")
    print(result.stdout)
except FileNotFoundError:
    print("未找到 FFmpeg，请检查安装和 PATH 配置。")

# Convert MP3 to WAV using FFmpeg
in_filename = r'E:\\learning\\minutes-main\\downloads\\test_audios\\e114.mp3'
out_filename = r'E:\\learning\\minutes-main\\downloads\\test_audios\\e114.wav'
_ = os.system(f"ffmpeg -y -i '{in_filename}' -acodec pcm_s16le -ac 1 -ar 16000 '{out_filename}'")

speech, _ = soundfile.read(out_filename)