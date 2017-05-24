#Module to obtain html code of the entered link
#Implementation of this module will be explained in Unit 4
#in details
import urllib.request

def get_page(link):
    try:
        page = urllib.request.urlopen(link).read().decode('utf-8')
        return page
    except:
        return ""
