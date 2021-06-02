from requests_html import HTML, HTMLSession
import csv


def get_data_from_session(url):
    csv_file = open('python_github.csv', 'w')#writes the data into 'python_github.csv', you can name it whatever u want
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Name', 'Description', 'Link'])
    session = HTMLSession()
    r = session.get(url)
    articles = r.html.find('article')
    for article in articles:#for loop, to loop over every article on the page, aka looping over all the repos
        headline = article.find('.text-normal', first=True).text #find the class .text-normal
        headline_u = headline.split("/")[0]#removes the / after the name of the repo, more organized
        print("Python Github repo name: ", headline_u)

        description = article.find('p', first=True).text#find paragraph tag
        print("Description: ", description)

        try: 
            link = article.find('a', first=True).attrs['href']#try the a tag, and get href attribute, which has a link
            #print(link)
            link_id = link.split('%2F')[1:3]#remove %2F from link, and keep only the second and last
            #print(link_id)
            final_link = "/" #starts off with just this
            final_link = final_link.join(link_id)#then we join the link_id, from the previous step, which has 2 words in a list, and joins it together between the "/"
            #print(final_link) 
            gh_link = f'https://github.com/{final_link}' #the href final_link, will now fianlly be added to the github base link, to create proper urls
        except Exception as e:
            gh_link = None

        print("Github repo link: ", gh_link)
        print()
        #adding the scraped data from the for loop into the csv file
        csv_writer.writerow([headline_u, description, gh_link])

    csv_file.close()    



def main():
    url = 'https://github.com/trending/python?since=daily'
    get_data_from_session(url)

    
if __name__ == '__main__':
    main()
