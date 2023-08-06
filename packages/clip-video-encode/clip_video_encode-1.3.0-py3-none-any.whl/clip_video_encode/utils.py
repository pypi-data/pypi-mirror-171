"""clip-video-encode utils."""
from torch.utils.data import Dataset, DataLoader


class HelperDataset(Dataset):
    """Helper dataset that preprocesses frames"""

    def __init__(self, imgs, preprocess):
        super().__init__()
        self.imgs = imgs
        self.preprocess = preprocess

    def __len__(self):
        return len(self.imgs)

    def __getitem__(self, ind):
        return self.preprocess(self.imgs[ind])


def block2dl(frames, preprocess, bs, n_work):
    ds = HelperDataset(frames, preprocess)
    return DataLoader(
        ds,
        batch_size=bs,
        shuffle=False,
        num_workers=n_work,
    )
