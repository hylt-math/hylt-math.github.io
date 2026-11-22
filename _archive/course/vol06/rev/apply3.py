src=open('rev/apply.py').read().split("# ---- part0")[0]
exec(src)
rep(P2,r"$u=f(x)$ で変数変換し逆関数を $x=g(u)=u+\cdots$ とする。$\mathrm{Res}_{x=0}f(x)^{-n-1}dx=\mathrm{Res}_{u=0}u^{-n-1}g'(u)\,du=[u^n]g'(u)$。これがすべての $n$ で $1$ なので $g'(u)=\sum_nu^n=\frac1{1-u}$、$g(u)=-\log(1-u)$。",
 r"$u=f(x)$ で変数変換し（補題 \ref{lem:residue}）逆関数を $x=\psi(u)=u+\cdots$ とする。$\mathrm{Res}_{x=0}f(x)^{-n-1}dx=\mathrm{Res}_{u=0}u^{-n-1}\psi'(u)\,du=[u^n]\psi'(u)$。これがすべての $n$ で $1$ なので $\psi'(u)=\sum_nu^n=\frac1{1-u}$、$\psi(u)=-\log(1-u)$。")
