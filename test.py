from tools.audio.tts_selector import TTSSelector

result = TTSSelector().execute({
    "preferred_provider": "doubao",
    "text": "你好，这是一段豆包语音合成测试。",
    "output_path": "projects/test/audio/doubao_sample.mp3",
    # voice_id 可选，不传则使用 .env 中的 DOUBAO_SPEECH_VOICE_TYPE
    # "voice_id": "zh_female_vv_uranus_bigtts",
    "speech_rate": 0,        # 0 为正常语速，100 为 2 倍速，-50 为 0.5 倍速
    "enable_timestamp": True # 生成逐字时间戳，方便后续做字幕
})

print("生成成功：", result)