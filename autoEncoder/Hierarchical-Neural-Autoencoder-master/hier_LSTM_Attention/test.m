function[]=test()
clear;

addpath('../misc');
n= gpuDeviceCount;
parameter.isGPU = 0;

if n>0 % GPU exists
    parameter.isGPU = 1;
    gpuDevice(2);
else
    print('no gpu ! ! ! ! !');
end

parameter.dimension=100;
parameter.alpha=0.1;  %learning rate
parameter.layer_num=4;  %number of layer
parameter.hidden=100;
parameter.lstm_out_tanh=0;
parameter.Initial=0.1;
parameter.dropout=0.2;  %drop-out rate
params.lstm_out_tanh=0;
parameter.isTraining=1;
parameter.CheckGrad=0;   %whether check gradient or not.
parameter.PreTrainEmb=0;    
%whether using pre-trained embeddings
parameter.update_embedding=1;
%whether update word embeddings
parameter.batch_size=16;
parameter.Source_Target_Same_Language=1;
%whether source and target is of the same language.
parameter.maxGradNorm=1;
parameter.clip=0;

parameter.lr=5;
parameter.read=0;

if parameter.Source_Target_Same_Language==1
    parameter.Vocab=25002; 
    %vocabulary size plus sentence-end and document-end
    parameter.sen_stop=parameter.Vocab-1;   %sentence-end
    parameter.doc_stop=parameter.Vocab;     %document-end
else
    parameter.SourceVocab=20;
    parameter.TargetVocab=20;
    parameter.stop=parameter.TargetVocab;
    parameter.Vocab=parameter.SourceVocab+parameter.TargetVocab;
end

if parameter.CheckGrad==1&parameter.dropout~=0
    parameter.drop_left=randSimpleMatrix([parameter.hidden,1])<1-parameter.dropout;
end
%alpha: learning rate for minibatch

parameter.nonlinear_gate_f = @sigmoid;
parameter.nonlinear_gate_f_prime = @sigmoidPrime;
parameter.nonlinear_f = @tanh;
parameter.nonlinear_f_prime = @tanhPrime;
[parameter]=ReadParameter(parameter);

test_source_file='../data/test_segment.txt';

while 1
    fd_test_source=fopen(test_source_file);
    [current_batch,End]=ReadData(fd_test_source,[],parameter,0);
    if End~=1 || (End==1&& length(current_batch.source_smallBatch)~=0)
        decode_greedy(parameter,current_batch,'a.txt');
    end
    if End==1
        break;
    end
end
end

function[parameter]=ReadParameter(parameter)
    % read parameters
    for ll=1:parameter.layer_num
        W_file=strcat('save_parameter/_Word_S',num2str(ll));
        parameter.Word_S{ll}=gpuArray(load(W_file));
        W_file=strcat('save_parameter/_Word_T',num2str(ll));
        parameter.Word_T{ll}=gpuArray(load(W_file));
        W_file=strcat('save_parameter/_Sen_S',num2str(ll));
        parameter.Sen_S{ll}=gpuArray(load(W_file));
        W_file=strcat('save_parameter/_Sen_T',num2str(ll));
        parameter.Sen_T{ll}=gpuArray(load(W_file));
    end
    parameter.Attention_W=gpuArray(load('save_parameter/_Attention_W'));
    parameter.Attention_U=gpuArray(load('save_parameter/_Attention_U'));
    parameter.vect=gpuArray(load('save_parameter/_v'));
    parameter.soft_W=gpuArray(load('save_parameter/_soft_W'));
end
