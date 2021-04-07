from utils import *
from models import ResNet50
from data_factory import CIFAR10DataPrep

import torch
import torch.nn as nn
import torch.optim as optim

import pickle

import json
# class Experiment()
    
# def __init__(self, experiment_config):
#     # load configs
#     self.experiment_config = experiment_config

def load_device(cuda_idx):
    device = torch.device("cuda:%s" %cuda_idx if torch.cuda.is_available() else "cpu")
    print(device)
    return device

def train(epoch, device, dataloader, model, criterion, optimizer):
    print('\nEpoch: %d' % epoch)
    model.train()

    train_loss = 0
    correct = 0
    total = 0

    for batch_idx, (inputs, targets) in enumerate(dataloader):
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        train_loss += loss.item()
        _, predicted = outputs.max(1)
        total += targets.size(0)
        correct += predicted.eq(targets).sum().item()

        progress_bar(batch_idx, len(dataloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                     % (train_loss/(batch_idx+1), 100.*correct/total, correct, total))


def validate(epoch, device, dataloader, model, criterion):
    global best_acc
    best_acc = -1
    model.eval()

    test_loss = 0
    correct = 0
    total = 0
    with torch.no_grad():
        for batch_idx, (inputs, targets) in enumerate(dataloader):
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)

            test_loss += loss.item()
            _, predicted = outputs.max(1)
            total += targets.size(0)
            correct += predicted.eq(targets).sum().item()

            progress_bar(batch_idx, len(dataloader), 'Loss: %.3f | Acc: %.3f%% (%d/%d)'
                         % (test_loss/(batch_idx+1), 100.*correct/total, correct, total))

    # Save checkpoint
    acc = 100.*correct/total
    if acc > best_acc:
        state = {
            'model': model.state_dict(),
            'acc': acc,
            'epoch': epoch,
        }
        if not os.path.isdir('../checkpoint'):
            os.mkdir('../checkpoint')
        torch.save(state, '../checkpoint/ckpt.pth')
        best_acc = acc

def main(config):
    # load config
    etl_config = config['etl']
    experiment_config = config['experiment']
    model_config = config['model']
    
    # pre-set parameters
    epochs = experiment_config['epochs']
    
    # load device
    device_use = load_device(experiment_config['cuda'])
    
    # creating dataloaders if necessary
    if not os.path.exists(os.path.join(etl_config['dataloader_dir'], "train_dataloader.pickle")):
        data_generator = CIFAR10DataPrep(etl_config)
        data_generator.prepare_dataloader()
    
    # load dataloaders
    with open(os.path.join(etl_config['dataloader_dir'], "train_dataloader.pickle"), "rb") as traindl:
        train_dataloader = pickle.load(traindl)
        
    with open(os.path.join(etl_config['dataloader_dir'], "train_dataloader.pickle"), "rb") as valdl:
        val_dataloader = pickle.load(valdl)
        
    with open(os.path.join(etl_config['dataloader_dir'], "train_dataloader.pickle"), "rb") as testdl:
        test_dataloader = pickle.load(testdl)

    # load model
    model = ResNet50(model_config)

    # load loss, optm, scheduler
    criterion = nn.CrossEntropyLoss()

    optimizer = optim.SGD(model.parameters(),
                          lr=model_config['lr'],
                          momentum=model_config['momentum'],
                          weight_decay = model_config['weight_decay'])

    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=200)

    for epoch in range(0, epochs):
        train(epochs, device_use, train_dataloader, model, criterion, optimizer)
        validate(epochs, device_use, val_dataloader, model, criterion)
        scheduler.step()
    validate(epochs, device, test_dataloader, model, criterion)

    
if __name__ == "__main__":
    with open('../config/experiment.json', 'r') as fh:
        config = json.load(fh)
    main(config)
    
    
    
    