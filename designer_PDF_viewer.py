def designerPdfViewer(h, word):
    b=list()
    s=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',0]
    for i in range(len(word)):
        for j in range(len(s)):
            if(word[i]==s[j]):
                # print(word[i])
                b.append(h[j])
    return max(b)*len(word)

h = [1,3,1,3,1,4,1,3,2,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5]
word = input("Enter a word : ")
result = designerPdfViewer(h, word)
print("The selection area for this word is:",result,"mm square")
