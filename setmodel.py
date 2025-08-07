import torch

ckpt = torch.load("/home/tatan/CodeScore/epoch%3D8-step%3D299583-val_pearson%3D0.739.ckpt", map_location="cuda:0")
torch.save(ckpt, "/home/tatan/CodeScore/feed_foward.ckpt")
