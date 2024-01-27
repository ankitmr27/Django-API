from urllib.parse import quote
from bs4 import BeautifulSoup
import requests
from MatchingWords import find_matching_device 
from secret import search_url
from dateExtract import extract_date_from_text
from summerizer import summarize_text_with_bert
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from sensitivityAnalysis import getSentiment

def getReview(word):
  # URL encode the string
  #word = "dell inspiron 15"
  encoded_string = quote(word)
  url = search_url + encoded_string

  response = requests.get(url)

  print(response.status_code)
  # print(response.text)

  soup = BeautifulSoup(response.text, 'lxml')
  #print(soup.prettify())
  #getting all the links of the search results
  links = soup.find_all('a', class_='rvw-title')
   
  # for link in links:
  #     print(link.text)
  #     print(link['href'])
  # gadgetUrl = links[0]['href']

  #finding matching percentage of the search results with user input
  search_results = [link.text for link in links]
  best_match = find_matching_device(word, search_results)
  #print(best_match) 
  #sorting results based on their matching percentage with user input with limit of 5
  best_match = sorted(best_match, key=lambda x: -x[1])[:5]
  #print(best_match)
  if(best_match.__len__()==0):
    return {'error':'No matching device found'}
  flag = False
  for result in best_match:
    if flag:
      break
    else:
      for link in links: 
        if result[0] == link.text:
          print(link.text)
          response = requests.get(link['href'])
          soup = BeautifulSoup(response.text, 'lxml')
          flag = True
          break

  reviews = soup.find_all('div', class_='_cmttxt _wwrap')[:5]
  review_text = [element.get_text(strip=True) for element in reviews]
  #used ThreadPoolExecutor for parallel excution of revies
  pros = ""
  cons = ""
  for review in review_text:
    sentiment = getSentiment(review)
    if "POSITIVE" == sentiment:
      pros = review + ' '
    if "NEGATIVE" == sentiment:
      cons = review + ' '
  pros = summarize_text_with_bert(pros)
  cons = summarize_text_with_bert(cons)   
  with ThreadPoolExecutor(max_workers=3) as executor:
    # Submit tasks to the executor
    tasks = [executor.submit(summarize_text_with_bert, doc) for doc in review_text]

    # Wait for all tasks to complete and retrieve results
    review_text = [task.result() for task in tasks]
  review_filtered = [element for element in review_text if element != ""]
  review_filtered_emotions = [{"review":review,"sentiment":getSentiment(review)} for review in review_filtered]
  # review_text = [summarize_text_with_bert(text) for text in review_text]
  # print("Review data:\n")
  #print(review_text)
  # print('')
  summary = soup.find_all('div', class_='_inrcntr _shrinkjs')
  summary_text = [element.get_text(strip=True) for element in summary]
  summary_text = summarize_text_with_bert(summary_text[0])
  # print(summary_text)
  # print("Summary data:\n")
  # print('')
  publish_date = soup.find('ul', class_='_flx _pdinfo')
  li_tags = publish_date.find_all('li')
  date_text = [element.get_text(strip=True) for element in li_tags[-1]][1]
  # print("Date data:\n")
  date = extract_date_from_text(date_text)
  return {
    'publish_date':date,
    'summary_text':summary_text,
    'pros':pros,
    'cons':cons,
    'review_text':review_filtered_emotions
    }


# print(datetime.now())
# print(getReview("Poco F1"))
# print(datetime.now())


#Poco X2 Realme C2 Dell Inspiron 15 Poco F1 Realme GT
