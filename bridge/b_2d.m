fid = fopen('test2D.txt','wt');% put file name here
array = rand(4,2);% put the fuckin array here
% run bassss
fprintf(fid,'{');
for i = 1 : size(array,1)
    fprintf(fid,'{');
    for j = 1 : size(array,2)
    if (j == size(array,2))  
       fprintf(fid,'%g ',array(i,j));
    else
        fprintf(fid,'%g,' ,array(i,j));
    end
    end
    if (i == size(array,1))  
       fprintf(fid,'}'); 
    else
        fprintf(fid,'},'); 
    end 
end
fprintf(fid,'};');