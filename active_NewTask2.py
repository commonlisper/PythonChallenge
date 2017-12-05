import sys

if len(sys.argv) < 3:
  print("Usage: active_NewTask2.py <file_to_open> <result_file_to_write>")
  exit()

def transform(text, len_to_transform, special_characters):
  word = ''
  result_text = ''  
  
  for char in text:
    if char in special_characters:
        if word and len(word) > len_to_transform:
          result_text += word[0].upper() + word[1:]
        else:
          result_text += word
          
        word = ''
        result_text += char
    else:
      word += char
      
  return result_text

result = ''

with open(sys.argv[1], 'r', encoding='utf-8') as file:
  result = transform(file.read(), 6, [',', '.', '!', ' '])

print(result)

with open(sys.argv[2], 'w', encoding='utf-8') as file:
  file.write(result)

