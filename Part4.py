#Module to obtain html code of the entered link
#Implementation of this module will be explained in Unit 4
#in details
def get_page(link):
    import urllib.request
    try:
        page = urllib.request.urlopen(link).read().decode('utf-8')
        return page
    except:
        return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

#This procedure allows elements to be added in the first
#parameter it takes and rejects any duplicate element that
#is already assigned to the first parameter.
def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#Procedure to collect all the links is known as depth first search
#It initially allows us to get all the last links from
#the webpages to be crawled. In other units, we will see how
#to change this type of search order as it is very inefficient
#way of crawling all the links. 
def crawl_web(seed, max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled and len(crawled) < max_pages:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

print(crawl_web("http://xkcd.com/353", 3))
