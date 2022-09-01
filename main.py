import requests
import pandas as pd
import random 
import json
import os 


#globals
my_key=os.environ['api_key']

USERAGENTS=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/49.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0']

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"


def retrieve_data():
  params = {
    'access_key': my_key,
    'url': url
  }


  headers={
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'User-Agent':''.format(random.choice(USERAGENTS)),
    'referer': 'https://coinmarketcap.com/',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://coinmarketcap.com',
    'sec-ch-ua-platform': "Windows",
    'pragma': 'no-cache',
      }

  response = requests.get('http://api.scrapestack.com/scrape',params,headers=headers)
  #save total_count
  total_count = response.json()['data']['totalCount']

  #save response in an object 
  obj =response.json()

  print(json.dumps(obj['data']['cryptoCurrencyList'],indent=4))
  print(type(obj['data']['cryptoCurrencyList']))
  
  return obj

def localize_data(json_obj):
  """
  this is for testing purposes so that I can use a set of data w/out to make repeated requests for the same data
  """
  with open("myData.json", "w") as my_file:
    my_file.write(json.dumps(json_obj,indent=4))

def parse_data(obj):

  df = pd.DataFrame(obj['data']['cryptoCurrencyList'])

  #filter data
  df2= df.filter(['name','symbol','low24h','high24h','totalSupply','maxSupply','atl','ath','lastUpdated'])
  df2.index+=1

  df2.to_csv('crypto.csv',sep=",",encoding='utf-8')


if __name__=="__main__":

  """ This block of code is for testing purposes
  #localize_data(retrieve_data())
  with open('myData.json') as fp:
        data = json.load(fp)
        parse_data(data)
  """

  parse_data(retrieve_data())
