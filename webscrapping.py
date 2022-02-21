from bs4 import BeautifulSoup
import requests

##Get a list of pages in the newsletter archive
##Get the html from the newsletter archive page. I picked a random archive page from the internet just for demonstration purposes.
URL = "https://www.comnetwork.org/newsletter-archive/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
for a_href in soup.find_all("a", href=True):
    print(a_href["href"])

##Since there are going to be more than just newsletter links in the newsletter-archive, I just printed them all out and pasted them into vim(but you can use any text editor). Then I deleted anything that didn’t look like a newsletter link.
##There are better ways of doing this. You could instead append to a list in python if you knew what the newsletter links started with. But at this point I figured it would be faster to do the work manually.
##I noticed that all the newsletter pages started with mailchi.mp.
##So I deleted everything else and added quotes around the links and a comma after the links.
##When I was done I pasted the links back into python.
##Now I had a list of the newsletter links. Here is a sample:

archive_links = ["http://mailchi.mp/4bd5002a15e1/february2018", "http://mailchi.mp/comnetwork/16may2018"].

##Get all the links from all the pages
##The last step is to get all the links on all of those newsletter pages and save them to a text file.

for link in archive_links:
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    for a_href in soup.find_all("a", href=True):
        with open("newsletter_links.txt", "a") as linkfile:
            linkfile.write(a_href["href"]+"\n")

##Use a for loop to go through the list. Get the html from each page. Find all the links. And write them to a text file.
##Notice that I use with open to write the text file. The with is recommended because it automatically closes the file when it is done. There is an “a” in the open because I am appending each link and not overwriting. The “\n” is the new line character. It puts each link on a separate line.
##At this point newsletter_links.txt if filled with all the links from all the newsletters, including stuff that I didn’t need. So I went into the text file. Sorted the links. And deleted anything that I didn’t want.