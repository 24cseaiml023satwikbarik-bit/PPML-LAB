inp=input("enter a paragraph:")
l=inp.split()
print("thenparagraph contains",len(l), "words")
count=0
for i in l:
    if i==i[::-1]:
        count+=1
print("palindrome=",count)
print("printing the words in reversed order:")
for i in l:
    print(i[::-1])