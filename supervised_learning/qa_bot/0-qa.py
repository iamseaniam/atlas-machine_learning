#!/usr/bin/env python3
"""Documentation"""
import tensorflow as tf
import tensorflow_hub as hub
from transformers import BertTokenizer


def question_answer(question, reference):
    """documentation"""
    try:
        tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        model = hub.load('https://tfhub.dev/see--/bert-uncased-tf2-qa/1')

        inputs = tokenizer(question, reference, return_tensors='tf')

        outputs = model([inputs['input_ids'], inputs['attention_mask']])
        
        start_logits, end_logits = outputs['start_logits'], outputs['end_logits']

        start_index = tf.argmax(start_logits, axis=1).numpy()[0]
        end_index = tf.argmax(end_logits, axis=1).numpy()[0]

        tokens = inputs['input_ids'].numpy()[0][start_index:end_index + 1]
        answer = tokenizer.decode(tokens)

        return answer if answer else None
    except Exception as e:
        print(f"Error during question answering: {e}")
        return None
