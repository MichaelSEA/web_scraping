import requests
from lxml import html

url = 'https://www.datawhatnow.com'

def get_parsed_page(url):
    '''Return the content of the website or the given url in
    a parsed lxml format that is easy to query'''


    response = requests.get(url)
    parsed_page = html.fromstring(response.content)
    return parsed_page


parsed_page = get_parsed_page(url)

# print the website's title
print(f"{parsed_page.xpath('//h1/a/text()')}")  # ['Data, what now?']


# print post names
print(f"{parsed_page.xpath('//h2/a/text()')}")
# Output
# ['SimHash for question deduplication',
#  'Feature importance and why it’s important']

post_urls = parsed_page.xpath('//h2//a/@href')
for post_url in post_urls:
    print('Post url:', post_url)

    parsed_post_page = get_parsed_page(post_url)
    paragraph_title_xpath = '//div[@class="entry-content"]/h3/text()'
    paragraph_titles = parsed_post_page.xpath(paragraph_title_xpath)
    paragraph_titles = map(lambda x: ' \n  ' + x, paragraph_titles)
    print(''.join(paragraph_titles) + '\n')

