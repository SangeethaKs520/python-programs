Sentence="Peter Piper picked a peck of pickled peppers \
A peck of pickled peppers Peter Piper picked"

word_dict = { }
for word in Sentence.split():
   if word not in word_dict:
       word_dict[word]=1
   else:
       word_dict[word]+=1
print(word_dict)