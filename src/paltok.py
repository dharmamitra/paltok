import sentencepiece as spm

class Paltok():
    def __init__(self, model_file="../models/pali_spm.model") -> None:
        self.model = spm.SentencePieceProcessor(model_file=model_file)