# Exercise 01: Part One
I am keeping things simple for this first scraper. I am going to be sraping all the chart data from https://coinmarketcap.com/.

## Architecture
We will be using **requests** and **pandas** to create a end to end data pipeline. **requests** will retrieve and pandas will parse our data and display our data in a csv file.

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
To run...
```
python3 main.py
```
Output should be a csv file with the parsed data