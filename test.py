# -*- coding: utf-8 -*-

from src.DataBase import DataBase
from src.CutWorld import CutWorld
from src.TextToAudio import TextToAudio
from src.Audio_Process import Audio_Process
from src.Gen_Video import Gen_Video

if __name__ == '__main__':
    text = """  
      全面开放基于文心大模型的AI能力，包括语音识别和文字识别等1397项场景化能力，智能创作平台、曦灵智能数字人平台、智能文档分析平台、智能对话定制平台UNIT及自主研发的视觉软硬一体产品度目等。
    """
    uuid = '515300'
    num = CutWorld().CutWorld(text, uuid)
    audio = TextToAudio().TextToAudio(text)
    # audio地址修改为本地音频的绝对路径
    beat_info = Audio_Process().Audio_Process(audio, num)
    Gen_Video().Gen_Video(beat_info, audio, uuid)
