import os
import random
from os.path import join
import numpy as np
import torch.multiprocessing
from scipy.io import loadmat
from PIL import Image
from torchvision.transforms.functional import to_pil_image
from torch.utils.data import Dataset


class Urban1960SatSS(Dataset):
    def __init__(self, transforms, split, root, datafrom = 'image'):
        super(urbanss, self).__init__()
        self.split = split
        self.root = root
        self.transform = transforms
        self.datafrom = datafrom
        split_files = {
            "train": ["labelled_train.txt"],
            # "train": ["unlabelled_train.txt"],
            "val": ["labelled_val.txt"],
            "train+val": ["labelled_train.txt", "labelled_val.txt"],
            "test": ["labelled_test.txt"],
            "all": ["all.txt"],
            "compare": ["draw_test.txt"]
        }
        assert self.split in split_files.keys()

        self.files = []
        for split_file in split_files[self.split]:
            with open(join(self.root, split_file), "r") as f:
                self.files.extend(fn.rstrip() for fn in f.readlines())

    def __getitem__(self, index):
        image_id = self.files[index]
        img = Image.open(join(self.root, self.datafrom, image_id + ".png"))
        label = Image.open(join(self.root, "mask_gt", image_id + ".png"))
        
        img, label = self.transform(img, label)
        return img, label, image_id

    def __len__(self):
        return len(self.files)
    
