import torch

from 手写数字界面.getNumber import ConvNet

def getN(image):
    # Device configuration
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    # Hyper parameters
    num_classes = 10
    model = ConvNet(num_classes).to(device)
    model.load_state_dict(torch.load('model.ckpt'))
    model.eval()
    images = image.to(device)
    outputs = model(images)
    return outputs[0]