import numpy

from enum import Enum

# Define the Enum to 
class Tag(Enum):
    Feature = 1
    Bug = 2
    Documentation = 3
    Test = 4

class Status(Enum):
    Backlog = 1
    Working = 2
    Review = 3
    Done = 4

class Job(Enum):
    Working = 1
    Review = 2

class Issue:
    def __init__(self, status, job, tag):
        self.points = 0
        self.status = status # can also be array
        self.job = job
        self.tag_array = tag

    def calculate_points(self):
        for tag in self.tag_array:
          if tag == Tag.Feature:
              self.points += 100
          if tag == Tag.Bug:
              self.points += 120
          if tag == Tag.Documentation:
              self.points += 150
          if tag == Tag.Test:
              self.points += 150
        if self.job == Job.Working:
          self.points *= 1.2

    


