import numpy as np
import pyperclip
import textwrap

#貼上內容
text = '''


'''

#範例else：
# text = '''
# 123
# 3@1 41
# 456

# '''

#範例if：
# text = '''
# ['貼上內容',
# '123',
# '3@141',
# '456']

# '''

# text = ["'123'"]
# text = ["123"]
# text = ['123','456']

# for x in text:
# 	if "'" in x[0]:
# 		x = x[1:]
# 	if "'" in x[-1]:
# 		x = x[:-1]
# 	print(x)

# for x in text:
# 	if "'" in x[0]:
# 		x = x[1:]
# 	if "'" in x[-1]:
# 		x = x[:-1]

# text = [ (x[1:] if "'" in x[0] else x) \
#  (x[:-1] if "'" in x[-1] else x) for x in text ]

# text = [ x[1:] if "'" in x[0] else x \
#  x[:-1] if "'" in x[-1] else x for x in text ]
# print(text)

# q=q


# 開始解析text
text2 = text
text = text.replace("\n","")
if ("[" in text[0]) & ("]" in text[-1]): #list轉row
# if "["在第一個和"]"在最後一個: #list轉row
	#print("if: list轉row")
	text = text.replace("[","").replace("]","")
	text = text.split(",")
	ALL_text = []
	# print(text)
	# text = [ x for x in text if "'" in x[0]]
	for x in text:
		if "'" in x[0]:
			x = x[1:]
		if "'" in x[-1]:
			x = x[:-1]
		ALL_text.append(x)
	ALL_text = '\n'.join(ALL_text)
	# print(test)
	pyperclip.copy(ALL_text)
else: #row轉list
	#print("else: row轉list")
	ALL_list = text2.split('\n')
	ALL_list = [x for x in ALL_list if len(x)!=0 ]
	# print(ALL_list)
	pyperclip.copy(str(ALL_list))