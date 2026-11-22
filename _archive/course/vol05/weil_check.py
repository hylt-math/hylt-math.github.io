import numpy as np, itertools, math
rng=np.random.default_rng(1)
def run(n):
    m=2*n  # generators: eps_1,eta_1,eps_2,eta_2,...  index 2j, 2j+1
    N=1<<m
    def wedge(a,b):
        out=np.zeros(N,dtype=complex)
        for I in np.nonzero(a)[0]:
            for J in np.nonzero(b)[0]:
                if I&J: continue
                # sign: count pairs (i in I, j in J) with i>j
                s=0
                for j in range(m):
                    if J>>j&1:
                        s+=bin(I>>(j+1)).count('1')
                out[I|J]+=a[I]*b[J]*(-1)**s
        return out
    def gen(i):
        v=np.zeros(N,dtype=complex); v[1<<i]=1; return v
    e=[(gen(2*j)+1j*gen(2*j+1))/np.sqrt(2) for j in range(n)]
    f=[(gen(2*j)-1j*gen(2*j+1))/np.sqrt(2) for j in range(n)]
    one=np.zeros(N,dtype=complex); one[0]=1
    omega=sum(1j*wedge(e[j],f[j]) for j in range(n))
    # check omega = sum eps_j eta_j
    om2=sum(wedge(gen(2*j),gen(2*j+1)) for j in range(n))
    assert np.allclose(omega,om2)
    full=N-1
    # Hodge star on monomials: eps_I ^ *eps_I = vol = gen0^gen1^...^gen(m-1)
    star=np.zeros((N,N),dtype=complex)
    for I in range(N):
        c=full^I
        v=np.zeros(N,dtype=complex);v[I]=1
        w=np.zeros(N,dtype=complex);w[c]=1
        s=wedge(v,w)[full]  # +-1
        star[c,I]=s  # *eps_I = s * eps_{I^c}   (since I ^ (s*c) = s*s... need I^*I=vol)
    # fix: eps_I ^ (s' eps_c) = s' * s0 vol, want vol -> s'=s0
    Lmat=np.zeros((N,N),dtype=complex)
    for I in range(N):
        v=np.zeros(N,dtype=complex);v[I]=1
        Lmat[:,I]=wedge(omega,v)
    Lam=Lmat.conj().T
    def mono(Iidx,Jidx):
        v=one.copy()
        for i in Iidx: v=wedge(v,e[i])
        for j in Jidx: v=wedge(v,f[j])
        return v
    def power(M,k): 
        R=np.eye(N,dtype=complex)
        for _ in range(k): R=M@R
        return R
    ok=True
    for k in range(0,n+1):
        for p in range(k+1):
            q=k-p
            if p>n or q>n: continue
            basis=[mono(I,J) for I in itertools.combinations(range(n),p) for J in itertools.combinations(range(n),q)]
            B=np.array(basis).T  # N x d
            # primitive: Lam alpha =0, alpha = B c
            A=Lam@B
            u,s,vh=np.linalg.svd(A)
            rank=(s>1e-9).sum()
            ker=vh[rank:].conj().T
            if ker.shape[1]==0: continue
            c=ker@(rng.normal(size=ker.shape[1])+1j*rng.normal(size=ker.shape[1]))
            al=B@c
            lhs=star@al
            rhs=(-1)**(k*(k+1)//2)*(1j)**(p-q)*(power(Lmat,n-k)@al)/math.factorial(n-k)
            weil=np.allclose(lhs,rhs)
            # HR: i^{p-q}(-1)^{k(k-1)/2} \int omega^{n-k} al ^ conj(al) >0
            alb=al.conj()  # conj of form: conj coefficients in eps,eta basis (real basis) 
            w=wedge(power(Lmat,n-k)@al,alb)
            val=w[full]  # coefficient on vol (omega^n/n! = vol)
            hr=((1j)**(p-q)*(-1)**(k*(k-1)//2)*val)
            print(f"n={n} k={k} (p,q)=({p},{q}) dimker={ker.shape[1]} Weil ok={weil}  HR value={hr:.4f}")
run(2); run(3)
