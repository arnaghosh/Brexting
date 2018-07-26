fid = fopen('test4D.txt','wt'); % put file name here
A = rand(4,2,2,3); 

fprintf(fid,'{');
s = [''];
for a=1:size(A,1)
s=[s '{'];
for i=1:size(A,2)
s =[s '{'];
for j=1:size(A,3)
s = [s '{'];
for k=1:size(A,4)
s =[s num2str(A(i,j,k))];
if k~=size(A,4) s=[s ',']; end
end
s=[s '}'];
if j~=size(A,3) s=[s ',']; end
end
s=[s '}'];
if i~=size(A,2) s=[s ',']; end
end
s=[s '}'];
if a~=size(A,1) s=[s ',']; end
end

fprintf(fid,s);
fprintf(fid,'}');
fprintf(fid,';');
