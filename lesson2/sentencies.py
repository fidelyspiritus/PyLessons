sent = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for id, word in enumerate(sent):
    sign = ""
    if word[0] == "-" or word[0] == "+":
        sign = word[0]
        word = word[1:]
    if word.isdigit():
        if int(word) < 10: sent[id] = '"' + sign + '0' + word + '"'
        else: sent[id] = '"' + sign + word + '"'

print(' '.join(sent))
