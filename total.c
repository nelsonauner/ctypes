int total(double *x, int n);
int total(double *x, int n){
	int i;
	double count = 0;
	for (i = 0;i<n;i++){
		count += x[i];
	}
	return count;
}
