#!/usr/bin/python3

from NaiveBayesClassifier import NaiveBayesClassifier
from ClassifierEvaluator import ClassifierEvaluator

if __name__ == "__main__":
   evaluator = ClassifierEvaluator(NaiveBayesClassifier())
   evaluator.evaluate()
   print("Accuracy : {0}".format(evaluator.accuracy()))   
   print("Precision : {0}".format(evaluator.precision()))
   print("Recall : {0}".format(evaluator.recall()))
   print("F-Measure : {0}".format(evaluator.f_measure()))
