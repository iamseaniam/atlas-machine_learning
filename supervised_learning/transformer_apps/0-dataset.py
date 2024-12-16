#!/usr/bin/env python3
"""Documentation"""
import transformers
import tensorflow_datasets as tfds


class Dataset:
    """Documentation"""

    def __init__(self):
        """Documentation"""

        self.data_train = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split='train',
            as_supervised=True
            )

        self.data_valid = tfds.load(
            'ted_hrlr_translate/pt_to_en',
            split='validation',
            as_supervised=True
            )

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)


    def tokenizse_dataset(self, data):
        """Documentation"""

        PortBase = []
        EngBase = []

        for Eng, Port in data:
            EngBase.append(
                Eng.numpy().decode("utf-8"))
            PortBase.append(
                Port.numpy().decode("utf-8"))

        def Eng_itorrater():
            """documentation"""
            for Eng in EngBase:
                yield Eng

        def Port_iterator():
            """documentation"""
            for Port in PortBase:
                yield Port

        tokenizer_port = transformers.BertTokenizerFast.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )

        Eng_tokenizer = transformers.BertTokenizerFast.from_pretrained(
            "bert-base-uncased"
        )

        # ? what is vocab_size doing here
        vocab_size = 2**13

        Eng_model_trained = Eng_tokenizer.train_new_from_iterator(
            text_iterator=Eng_itorrater(),
            vocab_size=vocab_size
        )
        Port_model_trained = tokenizer_port.train_new_from_iterator(
            text_iterator=Port_iterator(),
            vocab_size=vocab_size
        )

        return Eng_model_trained, Port_model_trained
