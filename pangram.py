def is_pangram(sentence):
    a = 'abcdefghijklmnopqrstuvwxys'
    if len(set(a)-set(sentence.lower())) == 0:	
	return True
    else:
	return False

    
