import csv

class Bucket:
    def __init__(self,capacity):
        self.capacity = capacity
        self.ld = 1
        self.records = []
        self.overflow = None

class ExtendibleHash:

    def __init__(self, num_buckets, num_capacity):
        self.num_buckets = num_buckets
        self.gd = 1
        self.buckets = []


        for i in range(num_buckets):
            self.buckets.append(Bucket(num_capacity))

    

        
