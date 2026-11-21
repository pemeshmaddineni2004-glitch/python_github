import random
names=['apple','banana','amla','carrot']
lives=6
generate_word=random.choice(names)
print(generate_word)
display=[]
for i in generate_word:
    display+= '_'
print(display)
k=False
while not k:
   aletter=input('enter a letter: ').lower()
   for position in range(len(generate_word)):
       j=generate_word[position]
       if(j==aletter):
        display[position]=aletter
   print(display)
   if aletter not in generate_word:
      lives-=1
      print('lives left',lives)
      if lives==0:
       k=True
       print('you lose')
   if '_' not in display:
      k=True
      print('you win')
   