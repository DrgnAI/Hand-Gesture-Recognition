import pandas as pd
import numpy as np

class DataLoader():
    def __init__(self, path_vid, path_labels, path_train=None, path_val=None, path_test=None):
        self.path_vid = path_vid
        self.path_labels = path_labels
        self.path_train = path_train
        self.path_val = path_val
        self.path_test = path_test
        self.get_labels(path_labels)
        
        if self.path_train:
            self.train_df = self.load_video_labels(self.path_train)
        if self.path_val:
            self.val_df = self.load_video_labels(self.path_val)
        if self.path_test:
            self.test_df = self.load_video_labels(self.path_test, mode="input")
    
    
    def get_labels(self, path_labels):
        self.labels_df = pd.read_csv(path_labels, names=['label'])
        #extract labels from dataframe
        self.labels = [str(label[0]) for label in self.labels_df.values]
        #print(self.labels)
        self.n_labels = len(self.labels)
        #print(self.n_labels)
        #create dictionaries to convert label to int and backwards
        self.label_to_int = dict(zip(self.labels, range(self.n_labels)))
        #print(self.label_to_int)
        self.int_to_labels = dict(enumerate(self.labels))
        #print(self.int_to_labels)

        




    def load_video_labels(self, path_subset, mode="label"):
        if mode == "input":
            # For test.csv, which has only video IDs
            df = pd.read_csv(path_subset, names=["video_id"])
        elif mode == "label":
            # For train.csv, validation.csv, and test-answers.csv, which have video IDs and labels
            df = pd.read_csv(path_subset, sep=';', names=["video_id", "label"])
            df = df[df.label.isin(self.labels)]
        
        print(df)
        return df