fid = fopen('test3D.txt','wt'); % put file name here
array = rand(4,2,3); % input array here
% run bassss

fprintf(fid,'{');
for i = 1 : size(array,1)
    fprintf(fid,'{');
    for j = 1 : size(array,2)
        fprintf(fid,'{');
        for k = 1 : size(array,3)
            if (k == size(array,3))  
                fprintf(fid,'%g ',array(i,j,k));
            else
                fprintf(fid,'%g,' ,array(i,j,k));
            end
        end
        
    if (j == size(array,2))  
       fprintf(fid,'}'); 
    else
        fprintf(fid,'},'); 
    end 
    
    end
    
    if (i == size(array,1))  
       fprintf(fid,'}'); 
    else
        fprintf(fid,'},'); 
    end 
end
fprintf(fid,'};');
