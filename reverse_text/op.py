text = open('text.txt', 'r', encoding="utf-8").read()
text_reversed = ''
word_reversed = ''
line_start = 0
line_end = text.index('\n')
while text[line_end] != '#':
	for i in range(line_end, line_start - 1, -1):
		text_reversed += text[i]
	text_reversed += ' '
	line_start = line_end + 1
	if text[line_end + 2:].index('\n') == 0:
		break
	else:
		line_end = line_end + 1 + text[line_end + 2:].index('\n')
# file = open("copy.txt", "w", encoding="utf-8")
# file.write(text_reversed)
# file.close()
print(text_reversed.count(' ') + 1)