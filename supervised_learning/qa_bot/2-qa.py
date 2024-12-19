#!/usr/bin/env python3
import tensorflow_hub as hub
from transformers import BertTokenizer
import numpy as np
import re


def question_answer(question, reference):
    """ Documentation """
    try:
        tokenizer = BertTokenizer.from_pretrained('bert-large-uncased-whole-word-masking-finetuned-squad')
        model = hub.load('https://tfhub.dev/see--/bert-uncased-tf2-qa/1')

        inputs = tokenizer(question, reference, return_tensors='np', truncation=True, max_length=512, padding=True)

        input_ids = inputs['input_ids']
        input_mask = inputs['attention_mask']
        segment_ids = inputs['token_type_ids']

        outputs = model([input_ids, input_mask, segment_ids])
        start_scores, end_scores = outputs[0][0], outputs[1][0]

        start_index = np.argmax(start_scores)
        end_index = np.argmax(end_scores)

        if start_index >= len(input_ids[0]) or end_index >= len(input_ids[0]) or start_index > end_index:
            return None

        tokens = tokenizer.convert_ids_to_tokens(input_ids[0])
        answer = tokens[start_index:end_index + 1]

        answer = tokenizer.convert_tokens_to_string(answer)
        answer = answer.replace('[CLS]', '').replace('[SEP]', '').strip()

        return answer if answer else None
    except Exception as e:
        print(f"Error during question answering: {e}")
        return None

def answer_loop(reference):
    """ documentation """
    print("Ask your questions (type 'exit', 'quit', 'goodbye', or 'bye' to end)")
    while True:
        user_input = input("Q: ").strip()
        if user_input.lower() in {'exit', 'quit', 'goodbye', 'bye'}:
            print("A: Goodbye")
            break

        answer = question_answer(user_input, reference)
        if answer:
            print(f"A: {answer}")
        else:
            print("A: Sorry, I do not understand your question.")

if __name__ == "__main__":
    with open('ZendeskArticles/PeerLearningDays.md') as f:
        reference = f.read()
    answer_loop(reference)
