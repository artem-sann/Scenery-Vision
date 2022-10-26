from abc import ABC, abstractmethod

import pandas as pd
from datasets import Dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration

from utils import device


class Model(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def generate(self, inputs):
        pass


class ModelRuT5(Model):
    def __init__(self):
        super().__init__()
        self.checkpoint = "sberbank-ai/ruT5-base"
        self.tokenizer = T5Tokenizer.from_pretrained(self.checkpoint)
        self.name_model = "/api/models/t5_e43"
        self.model = T5ForConditionalGeneration.from_pretrained("models/t5_e43")
        self.model.to(device)

    def generate(self, json):
        def add_eos_to_examples(example):
            example['input_text'] = 'Описать:  %s </s>' % (example['input_text'])
            return example

        def convert_to_features(example_batch):
            input_encodings = self.tokenizer.batch_encode_plus(
                example_batch['input_text'], pad_to_max_length=True, max_length=165
            )
            encodings = {
                'input_ids': input_encodings['input_ids'],
                'attention_mask': input_encodings['attention_mask'],
            }
            return encodings

        test_columns = ['input_ids', 'attention_mask']
        dataset_little_test = Dataset.from_pandas(pd.DataFrame(data={"input_text": self.parse(json)}))
        tokenized_test = dataset_little_test.map(add_eos_to_examples)
        tokenized_test = tokenized_test.map(convert_to_features, batched=True)
        tokenized_test.set_format(type='torch', columns=test_columns)

        outs = self.model.generate(
            input_ids=tokenized_test['input_ids'].to(device),
            attention_mask=tokenized_test['attention_mask'].to(device),
            max_length=165)
        return [{"Описание": self.tokenizer.decode(ids, skip_special_tokens=True).strip()} for ids in outs]

    def parse(self, json):
        results = []
        for unit in json:
            result = []
            for key1 in unit.keys():
                if isinstance(unit[key1], list):
                    dict_data = unit[key1]
                    for el_dict in dict_data:
                        dict_results = []
                        for key2 in el_dict.keys():
                            dict_results.append(f"{key2}: {el_dict[key2]}")
                        result.append("\n".join(dict_results))
                else:
                    result.append(f"{key1}: {unit[key1]}")
            results.append("</s>".join(result))
        return results
