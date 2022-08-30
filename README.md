# Exercise 01: Part One
I am keeping things simple for this first scraper. I am going to be sraping all the chart data from https://coinmarketcap.com/.

## Architecture
We will be using **scrapy** and **sql** to create a end to end data pipeline. **scrapy** will retrieve and parse the data and **sql** will be our database. 

## Lets get started...
*We will be working in the terminal for this first part.*
I recommend running this in a python virtual environment. This can be done using virtualenv or the virtual environment library of your choice.

To start a virtual environment using virtualenv type these commands in your terminal.
To instantiate your environment...

```
virtualenv venv
```
To activate it...
```
. venv/bin/activate
```
Now that we have our environment set up we can start. As always we import we our libraries. We will primarily be using scrapy so we need to run the following command in our terminal.

```
pip3 install -r requirements.txt
```

make sure that you cd into the scrapy directory person_case
```
cd person_case
```
*Optional:* We can verify that we are in the right directory by using the command..
`tree`

once you are in, run the command
```
scrapy crawl <insert name of crawler here>
```

use this command to see a visual of the data that was pulled 
```
scrapy crawl cases -O <name of output file along with the filetype of you choice e.g sample.json, sample.csv>
```
