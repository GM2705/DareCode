from googlesearch import search

# Define the search query
query = "crude oil OR brent oil OR natural gas OR unleaded gas OR heating oil site:"

# Define the list of websites to search on
websites = ["cnn.com", "reuters.com", "bloomberg.com"]

# Loop through each website and perform the search

with open('/Users/greigmann/Documents/code/ScrapedArticles.txt', 'w') as file:
    file.write("Scraped Articles:")
    file.write("\n\n")
    for website in websites:
        # Construct the search query for the current website
        website_query = query + website
        # Perform the search and get the top 5 results
        results = search(website_query, num_results=5)
        # Print out the search results
        for result in results:
            file.write(result)
            file.write("\n")
