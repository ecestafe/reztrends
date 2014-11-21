reztrends
=========

There are two python files used for the manipulation of the review json.

===dataMan.py===

This takes the reviews in a hard coded json file name and assumming it follows the same format as the other data prints the top 10 highest and lowest rated businesses with their IDs.

===dataRes.py===

This takes in the reviews in a hard coded json file and goes through the top rated business found in dataMan.py. Prints the reviews for each business along with the top unigrams in all the reviews

I've also included the stop_word file used to remove stop words.
