// Dense Gauss-Jordan mod p (p < 2^31). In-place RREF of R x C row-major uint32 matrix. Returns rank; piv[] = pivot columns.
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
static uint64_t pw(uint64_t a,uint64_t e,uint64_t p){uint64_t r=1;a%=p;while(e){if(e&1)r=r*a%p;a=a*a%p;e>>=1;}return r;}
int rref_mod(uint32_t*A,int R,int C,uint32_t p,int*piv){
  int r=0;
  for(int c=0;c<C&&r<R;c++){
    int s=-1;for(int i=r;i<R;i++) if(A[(size_t)i*C+c]){s=i;break;}
    if(s<0) continue;
    if(s!=r){for(int j=0;j<C;j++){uint32_t t=A[(size_t)s*C+j];A[(size_t)s*C+j]=A[(size_t)r*C+j];A[(size_t)r*C+j]=t;}}
    uint64_t iv=pw(A[(size_t)r*C+c],p-2,p);
    uint32_t*pr=A+(size_t)r*C;
    for(int j=c;j<C;j++) pr[j]=(uint64_t)pr[j]*iv%p;
    // collect nonzero columns of pivot row
    int *nz=malloc(sizeof(int)*C);int nn=0;for(int j=c;j<C;j++) if(pr[j]) nz[nn++]=j;
    for(int i=0;i<R;i++){ if(i==r) continue; uint32_t*pi=A+(size_t)i*C; uint64_t f=pi[c]; if(!f) continue; f=p-f;
      for(int k=0;k<nn;k++){int j=nz[k]; pi[j]=(pi[j]+f*pr[j])%p;} }
    free(nz);
    piv[r]=c;r++;
  }
  return r;
}
