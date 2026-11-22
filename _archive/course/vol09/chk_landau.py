import numpy as np
def frame(k,al,be,X,Y,J=6):
    fs=[]
    for rho in range(k):
        n0=rho+be/(2*np.pi)
        u=np.zeros_like(X,dtype=complex)
        for j in range(-J,J+1):
            n=n0+j*k
            c=np.exp(1j*j*al)*np.exp(-2*np.pi*n0*j-np.pi*k*j*j)
            u+=c*np.exp(n*X-k*X**2/(4*np.pi))*np.exp(1j*n*Y)
        u*=np.exp(-1j*(al*X+be*Y)/(2*np.pi))
        fs.append(u)
    return np.array(fs)
def check_bc(k,al,be):
    # u (untwisted gauge) quasi-periodicity & dbar
    x=np.array([[0.7]]);y=np.array([[1.3]])
    def u(xx,yy,rho):
        n0=rho+be/(2*np.pi); s=0
        for j in range(-8,9):
            n=n0+j*k; c=np.exp(1j*j*al)*np.exp(-2*np.pi*n0*j-np.pi*k*j*j)
            s+=c*np.exp(n*xx-k*xx**2/(4*np.pi))*np.exp(1j*n*yy)
        return s
    r=[]
    for rho in range(k):
        a=u(x+2*np.pi,y,rho); b=np.exp(1j*k*y+1j*al)*u(x,y,rho)
        c=u(x,y+2*np.pi,rho); d=np.exp(1j*be)*u(x,y,rho)
        r.append(max(abs(a-b)[0,0],abs(c-d)[0,0]))
    return max(r)
def chern(k,N=14,Nx=160,Ny=96):
    x=np.linspace(0,2*np.pi,Nx,endpoint=False);y=np.linspace(0,2*np.pi,Ny,endpoint=False)
    X,Y=np.meshgrid(x,y,indexing='ij')
    w=1/(Nx*Ny)
    F={}
    for a in range(N+1):
        for b in range(N+1):
            f=frame(k,2*np.pi*a/N,2*np.pi*b/N,X,Y).reshape(k,-1)
            G=(f.conj()@f.T)*w
            L=np.linalg.cholesky(G)   # G = L L^*
            # orthonormal frame: e = L^{-1} f  (rows)
            f=np.linalg.solve(L,f)
            F[(a,b)]=f
    def link(p,q):
        M=(F[p].conj()@F[q].T)*w
        d=np.linalg.det(M); return d/abs(d)
    tot=0
    for a in range(N):
        for b in range(N):
            z=link((a,b),(a+1,b))*link((a+1,b),(a+1,b+1))*link((a+1,b+1),(a,b+1))*link((a,b+1),(a,b))
            tot+=np.angle(z)
    return tot/(2*np.pi)
if __name__=="__main__":
    for k in (1,2,3):
        print("k",k,"bc residual",check_bc(k,0.9,2.1),"Chern",chern(k))
