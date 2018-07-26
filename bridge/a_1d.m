fid = fopen('test1D.txt','wt'); % put file name here
array = rand(4,1); % input array here
% run bassss

fprintf(fid,'{');
for i = 1 : size(array,1)
    if (i == size(array,1))  
       fprintf(fid,'%g ' ,array(i));
    else
        fprintf(fid,'%g,' ,array(i)); 
    end 
end
fprintf(fid,'};');
