#!/usr/bin/python3

from math import log
from os import listdir
from Word import Word


class NaiveBayesClassifier:
   
   def __init__(self):
      self.ham_keywords = set()
      self.spam_keywords = set()
      self.feature_repository = []
      self.ham_probability = 0.0
      self.spam_probability = 0.0
      self.number_of_ham_messages = 0
      self.number_of_spam_messages = 0
      
      
      
   def load_keywords(self):
      with open("../resources/hamKeywords.txt", "r") as ham:
         for line in ham:
            self.ham_keywords.add(line.strip())
            
      with open("../resources/spamKeywords.txt", "r") as spam:
         for line in spam:
            self.spam_keywords.add(line.strip())
   
   
   
   def classify(self, message):
      ham_sum = 0.0
      spam_sum = 0.0
      
      words = {}
      
      msgWords = message.split()
      
      for word in msgWords:
         
         if not word in words:
            words[word] = 1
         else:
            words[word] += 1
            
      for f in self.feature_repository:
         word_frequency = 0 if f.word not in words else words[f.word]
         ham_sum += (word_frequency * log(f.hamProbability, 2))
         spam_sum += (word_frequency * log(f.spamProbability, 2))
      
      ham_sum += log(self.ham_probability, 2)
      spam_sum += log(self.spam_probability, 2)
      
      return ham_sum >= spam_sum
   
   
   
   def compute_probabilities(self):
      N_ham  = sum([w.inHam for w in self.feature_repository])
      N_spam = sum([w.inSpam for w in self.feature_repository])
      
      length = len(self.feature_repository)
      
      for f in self.feature_repository:
         f.compute_ham_probability(length, N_ham)
         f.compute_spam_probability(length, N_spam)
   
   
   
   def train(self, ham_files_path, spam_files_path):
      self.load_keywords()
      
      self.train_ham(ham_files_path)
      self.train_spam(spam_files_path)
      
      total = self.number_of_ham_messages + self.number_of_spam_messages
      self.ham_probability = float(self.number_of_ham_messages) / float(total) 
      self.spam_probability = float(self.number_of_spam_messages) / float(total)
      
      self.compute_probabilities()
   
   
   
   def train_ham(self, ham_files_path):
      files = listdir(ham_files_path)
      self.number_of_ham_messages = len(files)
      
      for f in files:
         
         with open(ham_files_path + "/" + f, "r") as ham_file:
            
            for line in ham_file.readlines():
               words = line.split()
               
               for word in words:
                  
                  if word in self.ham_keywords:
                     w = Word(word)
                                 
                     if not w in self.feature_repository:
                        w.inHam += 1   
                        self.feature_repository.append(w)
                     else:   
                        self.feature_repository[self.feature_repository.index(w)].inHam += 1
   
   
   def train_spam(self, spam_files_path):
      files = listdir(spam_files_path)
      self.number_of_spam_messages = len(files)
      
      for f in files:
         
         with open(spam_files_path + "/" + f, "r") as spam_file:
            
            for line in spam_file.readlines():
               words = line.split()
               
               for word in words:
                  
                  if word in self.spam_keywords:
                     w = Word(word)
                     
                     if not w in self.feature_repository:
                        w.inSpam += 1
                        self.feature_repository.append(w)
                     
                     else:   
                        self.feature_repository[self.feature_repository.index(w)].inSpam += 1
