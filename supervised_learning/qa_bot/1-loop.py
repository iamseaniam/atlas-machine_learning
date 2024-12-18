#!/usr/bin/env python3
"""Documentation"""
import tensorflow_hub as hub
from transformers import BertTokenizer
import tensorflow as tf



def question_answer(question, reference):
    """
    documentation
    """
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


def main():
    """Loop to take input from the user and provide answers until an exit command is received."""
    reference = """This is a placeholder reference document that the model will use to find answers."""
    exit_commands = ["exit", "quit", "goodbye", "bye"]

    while True:
        user_input = input("Q: ").strip()
        if user_input.lower() in exit_commands:
            print("A: Goodbye")
            break

        answer = question_answer(user_input, reference)
        if answer:
            print(f"A: {answer}")
        else:
            print("A: I don't know the answer to that question.")


if __name__ == "__main__":
    main()
