fid = fopen('test4DnewAF.txt','wt'); % put file name here
array1 = Weights.Layer1; 
array = permute(array1,[4 3 2 1]);
% run bassss

fprintf(fid,'{');
for i = 1 : size(array,1)
    fprintf(fid,'{');
    for j = 1 : size(array,2)
        fprintf(fid,'{');
        for k = 1 : size(array,3)
            fprintf(fid,'{');
            for l = 1 : size(array,4)
                if (k == size(array,4))  
                    fprintf(fid,'%g ',array(i,j,k,l));
                else
                    fprintf(fid,'%g,' ,array(i,j,k,l));
                end
            end 
            if (k == size(array,3))  
                fprintf(fid,'}'); 
            else
                fprintf(fid,'},'); 
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
