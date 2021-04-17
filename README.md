# Analytica House Case Study

Simple web scraper

Only the endpoints with products in them, since this is a report of products.
https://docs.google.com/spreadsheets/d/1a1da53hBBBRMzjqWhxSETPW821DdYhmUGVmg0KfEGBw/edit?usp=sharing

## Description / Q&A

* python for web scraper, requests for... request purposes, BeautifulSoup as the scraper itself, pandas for reading the xlsx file, AppScript to send the email,
* sorting the percentages was a challange because for whatever reason there would be an invisible ' char in every single cell (only shows up when I click on the cell), so I had to manually format that column to percentage even though it was the right. getting the product code was another challenge, I managed to get %98 correct, but there are a few (~10) I couldn't manage to scrape.
* I learned to use a basic scraper, along with google sheets api and a really interesting product, appscript. It's a really powerful tool.
* Answers to additional questions
   * Multiprocessing can be used to send multiple processes at the same time
   * A scheduler can be used to run a task periodically, alternatively we can use [this](https://cloud.google.com/blog/products/application-development/how-to-schedule-a-recurring-python-script-on-gcp) 
   * From my understanding, an API is a tool for two parties to communicate with each other without having to know exactly how their infrastructure is built. Basically, you can think of it a set of protocols and documentations.