import sys, os

import praw

import redditAPI, twitterAPI

def searchHandle(query, apiSelectArray, reddit_Subreddits, twitterDate, twitterLocation, twitterRadius):

	redditResults = ""
	twitterResults = ""

	print(apiSelectArray)

	#Logic chunk to call the selected social media sites API's with optional parameters for advanced search refining.
	if 'reddit' in apiSelectArray:

		redditResults = redditAPI.search(query, reddit_Subreddits)

	if 'twitter' in apiSelectArray:

		#Reformats boolean NOT to - for Twitter.
		if("NOT " in query):
			query = query.replace("NOT ", "-")

		if(twitterRadius != ""):
			twitterRadius = twitterRadius+"mi"

		twitterResults = twitterAPI.search(query, twitterDate, twitterLocation, twitterRadius)

	# print(twitterResults)
	# print(redditResults)
	return redditResults, twitterResults