import argparse
from moviepy.editor import VideoFileClip        # moviepy==2.0.0.dev2
from pathlib import Path
import glob

def extract_audio(input_file, output_file):
    """
    从MP4视频文件中提取音频并保存为MP3文件
    
    参数:
    input_file (str): 输入的MP4视频文件路径
    output_file (str): 输出的MP3音频文件路径
    """
    try:
        # 加载视频文件
        video = VideoFileClip(input_file)
        
        # 提取音频
        audio = video.audio
        
        # 保存音频
        audio.write_audiofile(output_file)
        
        # 关闭资源
        audio.close()
        video.close()
        
        print(f"成功从 '{input_file}' 提取音频到 '{output_file}'")
        
    except Exception as e:
        print(f"提取音频时出错: {e}")


if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="从MP4视频中提取音频")
    parser.add_argument("-i", "--input_dir", help="输入的MP4视频文件所在目录", default=r"E:\learning\minutes\downloads\test_audios")
    parser.add_argument("-o", "--output_dir", help="输出的MP3音频文件所在目录", default=None)
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 确定输出目录
    if args.output_dir:
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = Path(args.input_dir)
    
    # 获取所有MP4文件路径
    mp4_files = glob.glob(str(Path(args.input_dir) / "*.mp4"))
    
    for input_file in mp4_files:
        input_path = Path(input_file)
        # 生成输出文件路径
        output_file = str(output_dir / f"{input_path.stem}.mp3")
        # 执行音频提取
        extract_audio(input_file, output_file)     