def title_proocessing(titleandauthor): #タイトルと作者名を分割する
    titleandauthor = titleandauthor.replace(' ', '')
    for tmp in range(0,len(titleandauthor)):
        
        if titleandauthor[tmp] == "/":
            title = titleandauthor[0:tmp]
            author = titleandauthor[tmp+1:len(titleandauthor)].replace('著', '').replace('訳', '')
            # print(title)
            # print(author)
            return title,author
