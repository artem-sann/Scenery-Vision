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
        self.num_sequences = 3
        self.checkpoint = "sberbank-ai/ruT5-base"
        self.tokenizer = T5Tokenizer.from_pretrained(self.checkpoint)
        self.name_model = "models/t5"
        self.model = T5ForConditionalGeneration.from_pretrained(self.name_model)
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

        parsed_json = self.parse(json)
        test_columns = ['input_ids', 'attention_mask']
        dataset_little_test = Dataset.from_pandas(pd.DataFrame(data={"input_text": parsed_json}))
        tokenized_test = dataset_little_test.map(add_eos_to_examples)
        tokenized_test = tokenized_test.map(convert_to_features, batched=True)
        tokenized_test.set_format(type='torch', columns=test_columns)

        outs = self.model.generate(
            input_ids=tokenized_test['input_ids'].to(device),
            attention_mask=tokenized_test['attention_mask'].to(device),
            max_length=256,
            do_sample=True,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            num_return_sequences=self.num_sequences
        )
        decode_outs = [self.tokenizer.decode(ids, skip_special_tokens=True).strip() for ids in outs]
        return [{"Описание": decode_outs[i * self.num_sequences: i * self.num_sequences + self.num_sequences]} for i in
                 range(len(parsed_json))]

    def parse(self, json):
        results = []
        for unit in json:
            result = []
            for key1 in unit.keys():
                if isinstance(unit[key1], list):
                    dict_data = unit[key1]
                    for el_dict in dict_data:
                        dict_results = []
                        if isinstance(el_dict, str):
                            dict_results.append(el_dict)
                            continue
                        for key2 in el_dict.keys():
                            dict_results.append(f"{key2}: {el_dict[key2]}")
                        string = "\n".join(dict_results)
                        result.append(f"{key1}: {string}")
                else:
                    result.append(f"{key1}: {unit[key1]}")
            results.append("</s>".join(result))
        return results
