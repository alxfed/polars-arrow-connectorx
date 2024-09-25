# -*- coding: utf-8 -*-
# Python
"""

"""
call_1 = {
  "type": "completion",
  "model": "text-davinci-003",
  "prompt": "The rock fell on the ground because it lost support and",
  "max_tokens": 256,
  "temperature": 0.5,
  "top_p": 1,
  "n": 1,
  "stream": False,
  "suffix": "That's why the rock fell on the ground.",
  "logprobs": None #,
  # "stop": "\n"
}
call_2 = {
  "type": "chat",
  "model": "gpt-3.5-turbo-0301",
  "messages": [
      {'role': 'user',
       'content': 'How much it 2 x 2?'},
      {'role': 'system',
       'content': 'Respond with a number, formatted in plain text.'},
      {'role': 'function',
       'content': '2'},
    ],
  "max_tokens": 256,
  "temperature": 0.5,
  "top_p": 1,
  "n": 1,
  "stream": False,
  "suffix": "That's why the rock fell on the ground.",
  "logprobs": None #,
  # "stop": "\n"
}
