# Web-search
In this program we are going to Open a google page to search something

import webbrowser

user_term = input("Enter a search term: ").replace(" ", "+") 

webbrowser.open("https://www.google.com/search?q="+ user_term) 
