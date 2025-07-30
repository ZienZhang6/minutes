

from models.vad import OnnxWrapper
import sherpa_onnx
from models.asr import transcribe_with_vad
from models.llm import load_llm
from utils import convert_to_wav
from summarize import summarize_contents_and_titles, load_from_transcripts
import soundfile
from pathlib import Path
import argparse
from tqdm import tqdm
def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--paraformer",
        default="./downloads/paraformer",
        type=str,
        help="Path to the directory of paraformer model.onnx and tokens.txt",
    )

    parser.add_argument(
        "--vad",
        default="./downloads/vad/silero_vad.onnx",
        type=str,
        help="Path to the silero_vad.onnx file",
    )

    parser.add_argument(
        "--llm_name_or_path",
        default="/mnt/samsung-t7/yuekai/llm/models/chatglm-6b",
        type=str,
        help="Path to the llm model directory, or the name of the model in huggingface. 'openai' to use the chatgpt model.",
    )

    parser.add_argument(
        "--num-threads",
        type=int,
        default=1,
        help="Number of threads for asr computation",
    )

    parser.add_argument(
        "--wav",
        type=str,
        # 修改默认值为目录路径
        default=r"E:\learning\minutes\downloads\test_audios",
        help="The directory containing input sound files to decode. "
    )

    parser.add_argument(
        "--summarization_prompt_template",
        type=str,
        default="""用一句话总结下面的会议:\n\n{text}\n\n 要求：1.非常简短。\n2.不要出现“会议”等字眼。\n总结：""",
        help="The template for summarization prompt. {text} will be replaced by the text to be summarized."
    )

    parser.add_argument(
        "--title_prompt_template",
        type=str,
        default="为下面文字生成标题:\n{text}\n要求:\n1.不超过十个字。\n2.非常非常简短 \n 标题：",
        help="The template for title prompt. {text} will be replaced by the text to be summarized."
    )

    parser.add_argument(
        "--output",
        type=str,
        default="./out.txt",
        help="The output file."
    )
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()

    token_file = str(Path(args.paraformer) / "tokens.txt")
    paraformer_file = str(Path(args.paraformer) / "model.onnx")
    recognizer = sherpa_onnx.OfflineRecognizer.from_paraformer(
        paraformer=paraformer_file,
        tokens=token_file,
        num_threads=2,
        sample_rate=16000,
        feature_dim=80,
        decoding_method="greedy_search",
        debug=False,
    )
    vad_model = OnnxWrapper(args.vad)
   

    ## 转换音频文件并进行语音识别
    audio_dir = Path(args.wav)
    # 遍历目录下所有 .mp3 文件
    for audio_file in tqdm(audio_dir.glob("*.mp3")):
        print(f"Started processing {audio_file}!")
        wav = convert_to_wav(str(audio_file))
        print(f"Audio file {audio_file} converted to wav!")

        # 进行语音识别
        print(f"Transcribing audio file {audio_file}...")       
        output_file = str(audio_file.parent) + f"\\{audio_file.stem}.txt"
        results = transcribe_with_vad(recognizer, vad_model, wav, output_file=output_file)
        print(f"Transcription of {audio_file} finished!")


