float* batch_norm(int num, const float a[num],const float mean[num], const float variance[num], const float affine_r[num],const float affine_c[num])
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
