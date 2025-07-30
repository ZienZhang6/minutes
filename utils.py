import datetime
from typing import List
import soundfile
import os
from pathlib import Path

def convert_to_wav(in_filename: str) -> str:
    """Convert the input audio file to a wave file"""
    in_filename = str(Path(in_filename))  # Ensure the path is a string
    
    # 将win路径
    base_dir = Path(in_filename)
    # print(base_dir.parent)
    # print(base_dir.name)
    # print(base_dir.stem)
    # print(base_dir.suffix)

    out_filename = base_dir.parent / (base_dir.stem + ".wav")

    try:
        _ = os.system(f'ffmpeg -y -i "{in_filename}" -acodec pcm_s16le -ac 1 -ar 16000 "{out_filename}"')
    except:
        print(f"Error converting {in_filename} to wav")
        return None
    speech, _ = soundfile.read(out_filename)
    print(f"load speech shape {speech.shape}")
    return speech



def chunk_strings(input_list: List[str], output_chunk_length: int) -> List[str]:
    output_list, chunk_idx = [], [0]
    current_chunk = ""
    
    for idx, string in enumerate(input_list):
        if len(current_chunk) + len(string) + 1 <= output_chunk_length:
            if current_chunk:
                current_chunk += " " + string
            else:
                current_chunk = string
        else:
            output_list.append(current_chunk)
            current_chunk = string
            chunk_idx.append(idx)
            
    if current_chunk:
        output_list.append(current_chunk)
    
    return output_list, chunk_idx


if __name__ == '__main__':
    in_filename = r'E:\learning\minutes\downloads\test_audios\e114.mp3'

    speech = convert_to_wav(in_filename)