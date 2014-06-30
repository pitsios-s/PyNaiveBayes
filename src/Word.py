#!/usr/bin/python3

#Every instance of this class, represents a single word found in a message.
class Word:

   def __init__(self, word):
      #The word itself.
      self.word = word
      
      #The number of times the word was found in a collection of ham messages.
      self.inHam = 0
      
      #The number of times the word was found in a collection of spam messages.
      self.inSpam = 0
      
      #P(word|ham)
      self.hamProbability = 0
      
      #P(word|spam)
      self.spamProbability = 0
   
      
   def compute_ham_probability(self, number_of_keywords, my_sum):
      #P(t | ling) = [1 + N(t, ling)] / [m + N(ling)]
      self.hamProbability= ( float( (1 + self.inHam) ) / float( (number_of_keywords + my_sum) ) )
	   
	   
   def compute_spam_probability(self, number_of_keywords, my_sum):
      #P(t | spam) = [1 + N(t, spam)] / [m + N(spam)]
      self.spamProbability= ( float( (1 + self.inSpam) ) / float( (number_of_keywords + my_sum) ) )
		
		
   def __eq__(self, other):
      return isinstance(other, self.__class__) and (other.word.lower()  == self.word.lower())
      
   def __hash__(self):
      return self.word.__hash__()
