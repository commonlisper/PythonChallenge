import sys

if len(sys.argv) < 3:
  print("Usage: active_NewTask2.py <file_to_open> <result_file_to_write>")
  exit()

f = open(sys.argv[1], 'r', encoding='utf-8')
str_from_file = f.read()
f.close()

def transform(text, len_to_transform, special_characters):
  word = ''
  result_text = ''  
  
  for s in text:
    if s in special_characters:
        if word and len(word) > len_to_transform:
          result_text += word[0].upper() + word[1:]
        else:
          result_text += word
          
        word = ''
        result_text += s
    else:
      word += s
      
  return result_text

result = transform(str_from_file, 6, [',', '.', '!', ' '])
print(result)

f = open(sys.argv[2], 'w', encoding='utf-8')
f.write(result)
f.close()

