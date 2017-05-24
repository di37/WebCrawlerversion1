
#Part of a html code of a webpage assigned as string that include a hyperlink
#or link

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

#To find hypertext reference tag to which a link is assigned
start_link = page.find('<a href=')
#Allows to find position of the beginning statement of a link
start_quote = page.find('"', start_link)
#Allows to find position of the ending statement of a link
end_quote = page.find('"', start_quote + 1)
#Extracts the first link from a webpage
url = page[start_quote+1:end_quote]
print (url)
