float* batch_norm(float* a,float* mean, float* variance, float*  affine_r,float* affine_c,int num)
{
	int i;
	float* out;
	out = (float*) malloc(num*sizeof(float));
 		
	for(i=0;i<num;i++)
	{
	    out[i] = (a[i] - mean[i])*affine_r[i]/variance[i] + affine_c[i];
	}
	return out;
}
