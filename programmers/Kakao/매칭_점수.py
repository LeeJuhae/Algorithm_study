import re

def solution(word, pages):
    answer = 0
    word = word.lower()
    link_p = re.compile('<a href.*>')

    word_p = re.compile('(?<!'+word+')'+word+'(?!'+word+')')
    meta_tag_p = re.compile('<meta property=.*content=.*/>')
    head_p = re.compile('<head>.*</head>', re.DOTALL)
    body_p = re.compile('<body>.*</body>', re.DOTALL)
    pages_info = dict()
    out_links = dict()
    scores = [-1] * len(pages)
    
    for idx, page in enumerate(pages):
        links = []
        page = page.lower()
        
        head = head_p.findall(page)
        body = body_p.findall(page)
        print(body)
        
        #words_in_page = word_p.findall(page)
        words_in_page = word_p.findall(body[0])
        basic_score = len(words_in_page)
        
        #tough_links = link_p.findall(page)
        tough_links = link_p.findall(body[0])
        #meta_tag = meta_tag_p.findall(page)
        meta_tag = meta_tag_p.findall(head[0])
        url = meta_tag[0][meta_tag[0].find("https://"):-3]
        for tough_link in tough_links:
            link = tough_link.split("\"")[1].split("\"")[0]
            links.append(link)
            if link not in out_links.keys():
                out_links[link] = [url]
            else:
                out_links[link].append(url)
        pages_info[url] = [idx, links, basic_score]
    
    for url, info in pages_info.items():
        link_score = 0
        if url in out_links.keys():
            for out_link in out_links[url]:
                link_score += pages_info[out_link][2] / len(pages_info[out_link][1])
        scores[info[0]] = info[2] + link_score
        
    return scores.index(max(scores))
