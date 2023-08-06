"""simplemapper - simple frame -> embedding mapper."""

import torch


class FrameMapper:
    def __init__(self, model, device):
        self.model = model
        self.device = device

    def __call__(self, batch):
        with torch.no_grad():
            embeddings = self.model.encode_image(batch).cpu().detach().numpy()
        return embeddings
