from transformers import AutoTokenizer
from transformers import AutoModelForSeq2SeqLM


class Summarizer:
    def __init__(self, model_dir):
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)

    def summarize(self, text):
        inputs = self.tokenizer(text, return_tensors="pt").input_ids
        outputs = self.model.generate(inputs, min_length=50, max_length=200, do_sample=False)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)