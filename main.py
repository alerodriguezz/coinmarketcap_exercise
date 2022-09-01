import requests
import pandas
import random 

USERAGENTS=['Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2866.71 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931',
'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-HK) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5',
'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/49.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0']

print (random.choice(USERAGENTS))

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=3&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"



s=requests.Session()
s.headers.update({
  'Accept': '*/*',
  'User-Agent':''.format(random.choice(USERAGENTS)),
  'referer': 'https://www.google.com/',
  'accept-language': 'en-US,en;q=0.9',
  'origin': 'https://coinmarketcap.com',
  'sec-ch-ua-platform': "Windows",
  'pragma': 'no-cache',
    })

response = s.request("GET", url)

print(response.text)
 #save token 
total_count = response.json()['data']['totalCount']

print(json.dumps(response.json()['data'],indent=4))
