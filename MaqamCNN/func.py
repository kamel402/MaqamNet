import torch
def custom_collate(batch):
    data = [item[0:0] for item in batch]
    # Here is a reshape operation on my target
    target = [torch.reshape(item[1], (-1,)) for item in batch]
    data = torch.stack(data)
    target = torch.stack(target)
    return [data, target]
