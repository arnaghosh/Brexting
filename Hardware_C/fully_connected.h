
float* fully_connect(float* image,float** weight,float* bias, int r,int c)
{
	int i,j;
	float* out_image;
	out_image = (float*) malloc(r*sizeof(float));
	for(i=0;i<r;i= i+1)
	{
		out_image[i] = bias[i];
		for(j=0;j<c;j=j+1)
		{
			out_image[i] += image[j]*weight[i][j];
		}
	}
	return out_image;
}


