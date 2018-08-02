float function_sign(float num,int threshold)
{
	
	if(num >= 0)
	   return num;
	else
	   return 0;
	   	        
}

float*** activation(float*** image,int ch, int n_r,int n_c,float*** out)
{
	//float*** out;
	int i,j,k;
	out = (float***) realloc(out,ch*sizeof(float**));
	for(i=0;i<ch;i=i+1)
	{
		out[i] = (float**) realloc(out[i],n_r*sizeof(float*));
		for(j=0;j<n_r;j=j+1)
		{
			out[i][j] = (float*) realloc(out[i][j],n_c*sizeof(float));
			for(k = 0;k<n_c;k=k+1)
				out[i][j][k] = 0;
	    }   
	}
	
	for(i = 0;i<ch;i=i+1)
	{
		for(j=0;j<n_r;j=j+1)
		{
			for(k=0;k<n_c;k=k+1)
			{
				out[i][j][k] = function_sign(image[i][j][k],7);
			}
		}
	}
	return out;
}

float* activation_1d(int length, const float vec[length],float* out_vec)
{
	//float* out_vec;
	int i;
	out_vec = (float*) realloc(out_vec,length*sizeof(float));
	for(i=0;i<length;i=i+1)
	{
		out_vec[i] =  function_sign(vec[i],6);
	}
	return out_vec;
}
