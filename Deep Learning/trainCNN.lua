require 'nn';
require 'image';
require 'optim';
require 'gnuplot';
require 'cutorch';
require 'cunn';
require 'hdf5';

model = require 'model.lua';
model:cuda();

file = hdf5.open('AllTrials.h5','r')
data = file:read('/home/TF'):all()
data = data:transpose(1,3):contiguous()
data = data:resize(data:size(1),1,data:size(2),data:size(3));
Labels = file:read('/home/Y'):all();
print(#data, #Labels);
print(Labels:min(),Labels:max())

trainPortion = 0.8;

print("data loading done =====>")

indices = torch.randperm(data:size(1)):long()
--indices = torch.linspace(1,data:size(1),data:size(1)):long()

trainData = data:index(1,indices:sub(1,(trainPortion*indices:size(1))))
trainLabels = Labels:index(1,indices:sub(1,(trainPortion*indices:size(1))))
testData = data:index(1,indices:sub((trainPortion*indices:size(1)+1), indices:size(1)))
testLabels = Labels:index(1,indices:sub((trainPortion*indices:size(1)+1), indices:size(1)))
indices = nil;

print(trainData:mean(),trainData:std())
print(testData:mean(),testData:std())

trainData:add(-trainData:mean())
trainData:div(trainData:std())
testData:add(-testData:mean())
testData:div(testData:std())

print(trainData:mean(),trainData:std())
print(testData:mean(),testData:std())

N = trainData:size(1)
N1 = testData:size(1)
local theta,gradTheta = model:getParameters()
criterion = nn.ClassNLLCriterion():cuda()

local x,y;
local feval = function(params)
    if theta~=params then
        theta:copy(params)
    end
    gradTheta:zero()
    out = model:forward(x)
    --print(#out1,#out,#y)
    local loss = criterion:forward(out,y)
    local gradLoss = criterion:backward(out,y)
    model:backward(x,gradLoss)

    return loss, gradTheta
end

batchSize = 25

indices = torch.randperm(trainData:size(1)):long()
trainData = trainData:index(1,indices)
trainLabels = trainLabels:index(1,indices)

epochs = 100
teAccuracy = 0
print('Training Starting')
local optimParams = {learningRate = 0.02, learningRateDecay = 0.002, weightDecay = 0.002}
local _,loss
local losses = {}
for epoch=1,epochs do
    collectgarbage()
    model:training()
    print('Epoch '..epoch..'/'..epochs)
    for n=1,N-batchSize, batchSize do
        x = trainData:narrow(1,n,torch.floor(batchSize*trainPortion)):cuda()
        y = trainLabels:narrow(1,n,torch.floor(batchSize*trainPortion)):cuda()
        _,loss = optim.adam(feval,theta,optimParams)
        losses[#losses + 1] = loss[1]
    end
    local plots={{'Training Loss', torch.linspace(1,#losses,#losses), torch.Tensor(losses), '-'}}
    gnuplot.pngfigure('Training.png')
    gnuplot.plot(table.unpack(plots))
    gnuplot.ylabel('Loss')
    gnuplot.xlabel('Batch #')
    gnuplot.plotflush()
    indices = torch.randperm(trainData:size(1)):long()
    trainData = trainData:index(1,indices)
    trainLabels = trainLabels:index(1,indices)
    if (epoch%5==0) then
    	model:evaluate()
        N1 = testData:size(1)
        teSize = N1
        correct = 0
        class_perform = {0,0,0,0}
        class_size = {0,0,0,0}
        classes = {'1','2','3','4'}
        for i=1,N1 do
            local groundtruth = testLabels[i]
            if groundtruth<0 then groundtruth=2 end
            local example1 = torch.Tensor(1,1,9,257);
            example1[1] = testData[i]
            class_size[groundtruth] = class_size[groundtruth] +1
            local prediction = model:forward(example1:cuda())
            local confidences, indices = torch.sort(prediction, true)  -- true means sort in descending order
            if groundtruth == indices[1][1] then
            --if testLabels[i]*prediction[1][1] > 0 then
                correct = correct + 1
                class_perform[groundtruth] = class_perform[groundtruth] + 1
            end
            collectgarbage()
        end
        print("Overall correct " .. correct .. " percentage correct" .. (100*correct/teSize) .. " % ")
        if correct>=teAccuracy then
            teAccuracy=correct
            torch.save('model_S1.t7',model)
            for i=1,#classes do
               print(classes[i], 100*class_perform[i]/class_size[i] .. " % ")
            end
        end
    end
end

model = nil;
x = nil;
collectgarbage()
--torch.save('lsm_model.t7',model)
model = torch.load('model_S1.t7')
model:evaluate()

N = testData:size(1)
teSize = N
print('Testing accuracy')
correct = 0
class_perform = {0,0,0,0}
class_size = {0,0,0,0}
classes = {'1','2','3','4'}
for i=1,N1 do
    local groundtruth = testLabels[i]
    if groundtruth<0 then groundtruth=2 end
    local example1 = torch.Tensor(1,1,9,257);
    example1[1] = testData[i]
    class_size[groundtruth] = class_size[groundtruth] +1
    local prediction = model:forward(example1:cuda())
    local confidences, indices = torch.sort(prediction, true)  -- true means sort in descending order
    if groundtruth == indices[1][1] then
    --if testLabels[i]*prediction[1][1] > 0 then
        correct = correct + 1
        class_perform[groundtruth] = class_perform[groundtruth] + 1
    end
    collectgarbage()
end
print("Overall correct " .. correct .. " percentage correct" .. (100*correct/teSize) .. " % ")
for i=1,#classes do
   print(classes[i], 100*class_perform[i]/class_size[i] .. " % ")
end