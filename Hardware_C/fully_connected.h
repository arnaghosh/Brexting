float* fully_connect(int r,int c, const float image[c], const float weight[r][c],const float bias[r],float* out_image)
{
	int i,j;
	//float* out_image;
	out_image = (float*) realloc(out_image,r*sizeof(float));
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
