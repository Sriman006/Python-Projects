
words = set()

start = "<"
end = ">"



with open ("story.txt", "r") as f:
    story = f.read()
    print(story)

for i, char in enumerate(story):
    
    if char == "<" :
       start_of_words = i
    #    print(start_of_words)   

    if char ==  end and start_of_words !=  -1:
        print(i)
        word = story[start_of_words:i]
        words.add(word)  

print(words)         
       
       
       
       
       
       