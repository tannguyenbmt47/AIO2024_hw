import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        return torch.exp(data) / torch.sum(torch.exp(data))


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, data):
        c = max(data)

        return torch.exp(data - c) / torch.sum(torch.exp(data - c))


if __name__ == "__main__":

    data = torch.Tensor([1, 2, 3])

    # Sử dụng Softmax
    softmax = Softmax()
    output = softmax(data)
    print(output)

    # Sử dụng SoftmaxStable
    softmax_stable = softmax_stable()
    output_stable = softmax_stable(data)
    print(output_stable)
