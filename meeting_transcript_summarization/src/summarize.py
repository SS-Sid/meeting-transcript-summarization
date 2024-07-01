from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM


class Summarizer:
    def __init__(self, model_dir):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

    def summarize(self, text, max_new_tokens=100):
        inputs = self.tokenizer(text, return_tensors="pt").input_ids
        outputs = self.model.generate(inputs, max_new_tokens=max_new_tokens, do_sample=False)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


def read_transcript(file_path):
    with open(file_path, 'r') as file:
        transcript = file.read()
    return transcript