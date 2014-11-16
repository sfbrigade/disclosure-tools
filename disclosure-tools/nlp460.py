from textblob import TextBlob


def shared_noun_phrases (strA, strB):
	listA = TextBlob(strA).noun_phrases
	listB = TextBlob(strB).noun_phrases
	#return shared noun phrases
	return (list(set(listA) & set(listB)))


