# In this program we are going to Open a google page to search something

import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+") # Replace spaces with + like in the link when ypu search

webbrowser.open("https://www.google.com/search?q="+ user_term) # open function expect an url as a string

