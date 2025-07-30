import argparse
from moviepy.editor import VideoFileClip        # moviepy==2.0.0.dev2
from pathlib import Path

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
    input_file = r"E:\learning\minutes\downloads\test_audios\1.mp4"
    input_file = str(Path(input_file))

    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="从MP4视频中提取音频")
    parser.add_argument("input", help="输入的MP4视频文件路径")
    parser.add_argument("-o", "--output", help="输出的MP3音频文件路径", default=None)
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 确定输出文件路径
    if args.output:
        output_file = args.output
    else:
        # 如果未指定输出文件名，使用输入文件名并替换扩展名
        import os
        base_name = os.path.basename(args.input)
        file_name, _ = os.path.splitext(base_name)
        output_file = f"{file_name}.mp3"
    
    # 执行音频提取
    extract_audio(args.input, output_file)    