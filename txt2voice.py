#encoding: utf-8
'''
gtts是调用translate.google.com的API接口，把文字转换为MP3格式文件输出。
但必须在打开VPN的情况下才能调试。
lang = 'en'表示转换为英文语音；'zh-tw'表示转换为中文语音。
当需要转换中文语音时，需要在Python27\Lib\site-packages目录下创建
sitecustomize.py：
import sys
reload(sys)
sys.setdefaultencoding('utf8')
'''
from gtts import gTTS

txt2voice = gTTS(text='how are you, where are you go?', lang='en')
txt2voice.save('txt2voice_english.mp3')

txt2voice_2 = gTTS(text= '你好吗,有什么事情需要帮助吗',lang='zh-tw')
txt2voice_2.save('txt2voice_chinese.mp3')

