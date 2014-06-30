#!/usr/bin/python3

from NaiveBayesClassifier import NaiveBayesClassifier
from os import listdir

class ClassifierEvaluator:
   
   def __init__(self, nbc):
      
      #The naive bayes classifier object.
      self.nbc = nbc
      
      self.number_of_messages_tested = 0
      self.true_positives = 0
      self.true_negatives = 0
      self.false_positives = 0
      self.false_negatives = 0
      
      
   def evaluate(self):
      print("Started training process. Please wait...")
      self.nbc.train("../resources/lingMessages", "../resources/spamMessages")
      print("Training process ended.")
      
      print("Started classification process. Please wait...")
      self.classify("../resources/testMessages")
      print("Classification process ended.")
      
      
   def classify(self, test):
      files = [f for f in listdir(test)]
      self.number_of_messages_tested = len(files)
      
      for f in files:
         
         with open(test + "/" + f, "r") as test_file:
            msg = ""
            
            for line in test_file.readlines():
               msg += line + "\n"
               
            result = self.nbc.classify(msg)
            
            if("spm" in f and not result):
               self.true_positives += 1
            elif("spm" in f and result):
               self.false_negatives +=1
            elif("spm" not in f and result):
               self.true_negatives += 1
            elif("spm" not in f and not result):
               self.false_positives += 1
               
               
   def accuracy(self):
      return 0.0 if float(self.number_of_messages_tested) == 0.0 else\
      float(self.true_positives + self.true_negatives) / float(self.number_of_messages_tested)
   
   
   def precision(self):
      return 0.0 if (self.true_positives + self.false_positives) == 0 else\
      float(self.true_positives) / float(self.true_positives + self.false_positives)
      
   def recall(self):
      return 0.0 if (self.true_positives + self.false_negatives) == 0 else\
      float(self.true_positives) / float(self.true_positives + self.false_negatives)
      
   def f_measure(self):
      return 0.0 if float(self.precision() + self.recall()) == 0.0 else\
      (2 * self.precision() * self.recall()) / (self.precision() + self.recall())
               
            
            
