# 査読ノート 査読者2（§4〜§6：partB.tex、solB.tex）

ビルド：rv2_build/（`./build.sh`）。修正後：エラー 0、Overfull 0、未定義参照 0、142 頁、問題 88・解答 88、キー一致。
（残る警告は日本語斜体フォントの `Font shape ... it undefined` のみ。既存で内容に影響しない。）
独立検算：scratchpad/rv2/chk2.py（numpy / fractions のみ）。

## 修正した箇所

| 箇所 | 旧 | 新 | 理由 |
|---|---|---|---|
| partB §4.2 テンソル場の定義（「テンソル場とテンソル性の補題」冒頭） | $T_pM$ 上の $r$ 重双対・$s$ 重の共変テンソル | $r$ 重反変・$s$ 重共変のテンソル | 「双対」は共変側の語で、$(T_pM)^{\otimes r}$ を指す語として誤解を招く。用語の誤り。 |
| partB 系 5.x（Poincaré の補題）の証明 | 「$F(x,t)=tx:U\times\R\to U$」 | $U\times[0,1]\to U$ のホモトピーとし、星状 $U$ では $\{(x,t)\mid tx\in U\}$ 上で定義されること、$K$ と命題（ホモトピー公式）の証明は $t\in[0,1]$ の値しか使わないことを注記 | 星状開集合 $U$ では $tx$ は $t\notin[0,1]$ で $U$ を出るので、$U\times\R\to U$ は誤り（$U=\R^n$ なら正しい）。公式の適用条件の欠落。 |
| partB 定理（正則値による写像度）の証明 | 互いに交わらない開近傍 $U_i\ni x_i$ | 「連結な」開近傍 | $\int_{U_i}f^*\omega=\varepsilon(x_i)\int_{W_i}\omega$ で符号が $U_i$ 上で一定であることに連結性が要る（証明の欠落）。 |
| partB 定理（トーラス上の Hodge の定理）の主張 | 「一意に $\omega=h+\dd\alpha+\delta\beta$ と書け」 | 「と書け（$h,\dd\alpha,\delta\beta$ は一意）」 | $\alpha,\beta$ 自体は定数分だけ不定で、「一意」の対象が曖昧だった。 |
| 同定理の証明末尾（環構造） | 「$\star$ は定数係数形式を保ち、式 $\dd x^I\wedge\dd x^J=\pm\Bvol$ から環構造は…一致」 | 定数係数形式の外積は定数係数形式で $[\dd x^I][\dd x^J]=[\dd x^I\wedge\dd x^J]$ だから一致 | $\star$ も $\pm\Bvol$ も環構造の議論と無関係で、論理が不自然だった。 |
| 図 27（$S^2$ の球面座標） | 「$\theta=0$」が北極 $N$ から離れた左上に浮いていた | $N$ のラベルを「$N$（$\theta=0$）」に統合 | 図の可読性。ビルド後に再確認、重なり・はみ出しなし。 |

解答（solB.tex）は修正なし（B 担当 32 問（§4：11、§5：12、§6：9）をすべて手計算で追い、誤りなし）。

## 確認した項目（誤りなし）

### §4
- 外積の規約（行列式規約）、$\dd$ の公理的特徴づけ（存在・一意性・座標独立性・(D4)(D5)）、不変公式、$\iota_X$ の反微分性の符号。
- Cartan の公式の証明（導分の符号計算を手で再確認）、$[\Lie_X,\iota_Y]=\iota_{[X,Y]}$、$[\Lie_X,\Lie_Y]=\Lie_{[X,Y]}$。
- 例：極座標、$z^2$、$S^1$ の $\dd\theta$、$\omega=\dd\theta$ の閉性、回転の Lie 微分（定義と Cartan の両方で一致）、div、Euler 場（図は $t=\ln2$ で整合）。
- $\R^3$ の grad/curl/div の表、勾配場の例。
- Stokes の証明 Step 1 の符号（$\partial\mathbb H^n$ の誘導向きが標準の $(-1)^{n-1}$ 倍。$n=1$ も整合）。Green・Gauss・古典 Stokes。図 21 の向き。
- 標準 1 形式、$\omega=\dd\lambda$、Hamilton 方程式の符号（$\iota_{X_H}\omega=-\dd H$ から $\dot x=H_\xi,\dot\xi=-H_x$）、$\omega^n=n!\,\cdots$。
- 規約が §1（partA）の外積・$\iota$・$\dd$ の規約と一致（partA の規約表と照合）。

### §5
- ホモトピー公式と Poincaré の補題の公式 $P$ を、有理係数多項式の形式（$\R^3$、$k=1,2,3$、ランダム係数）で $\dd P+P\dd=\id$ と検算（chk2.py）。問 B_primitive の値（$\gamma=yz\,\dd x-xz\,\dd y$ など）も手計算で一致。
- Mayer–Vietoris の $\delta$ の式 $-\dd(\rho_V\tau)$ / $\dd(\rho_U\tau)$ と全射性、蛇の補題の完全性 3 か所、$S^1$ での $\int\eta=\tau_2-\tau_1$（問 B_S1MV の解答も一致）。
- $S^n$ の帰納法、Euler 標数の加法性、連結和の公式 $\chi(M\#N)=\chi(M)+\chi(N)-2+\chi(S^{n-1})$、$\chi(\Sigma_g)=2-2g$。
- 写像度：対蹠写像 $(-1)^{n+1}$、毛玉定理、$z^m$、$z+1/z$ の次数 2（正則値 0 の逆像 $\pm i$、$f'(\pm i)=2$）。
- Poincaré 双対の系 (i)〜(iv)（歪対称・対称、$b_m$ 偶数、$\chi$ 偶数）。
- 問 B_brouwer (b) の $\lambda$ の式と、判別式が正であることの議論。問 B_Hc の符号（$-2\pi$）。

### §6
- Hodge 星の符号を一般 $n=2,\dots,5$、全 $k$ で計算機検算（$\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\Bvol$、$\star\star=(-1)^{k(n-k)}$）。$\R^4$ の表は 18 項すべて一致。
- $\delta=(-1)^{n(k+1)+1}\star\dd\star$ が各 Fourier モード上で $-i\,\iota_m$（式 (15) の $-\sum\iota_{\pa_j}\pa_j$）に一致することを $n=2,\dots,5$、全 $k$ で検算。補題の $\theta_m\wedge\iota_m+\iota_m\theta_m\wedge=|m|^2$ も検算。
- 証明中の符号計算（$\star^{-1}=(-1)^{j(n-j)}\star$、指数の mod 2 計算）、共形変換 $\tilde\star=e^{(n-2k)u}\star$、関数の Laplacian の公式、$S^2$ の固有関数（$\Delta\cos\theta=2\cos\theta$、$\Delta(\sin\theta e^{i\varphi})=2\sin\theta e^{i\varphi}$）。
- トーラス上の Hodge 定理の公式 $\alpha,\beta$ の係数（$-i\cdot i=1$ など）、例 $T^2$ の分解（$h=2\dd x+3\dd y$、周期 $4\pi,6\pi$、$\beta=\delta(-\cos y\,\dd x\wedge\dd y)$）。
- $\Lambda^\pm$ の基底、式 (sd)、問 B_star4 の数値（$|\alpha^+|^2-|\alpha^-|^2=4=\alpha\wedge\alpha/\Bvol$）、問 B_torus の $\|\omega\|^2=54\pi^2$、$\|h\|^2=52\pi^2$。
- 問 B_adj (c)（$\Delta=\mathrm{curl\,curl}-\mathrm{grad\,div}$）の成分計算、問 B_conf (b)（$\tilde\delta=e^{-2u}\delta$）。

### 規約・巻番号
- 後の巻への言及（第3・5・6・11・12・15 巻など）は back.tex / integ.md の巻構成と一致。
- 出典の章番号：Lee 第6・14・16・17・18章（back.tex の目次確認と一致）、Warner 第6章（Hodge）、Bott--Tu 第I章 §1〜§5・第II章、McDuff--Salamon 第3章（Darboux）は記憶と整合。

## 確認できなかった項目
- Bott--Tu の節番号（§1〜§5）、Warner 第2・5・6章、Spivak 第5章、McDuff--Salamon 第3章、Petersen の章：ネットワーク不可のため原書で照合していない。本文の【要確認】（de Rham の定理の節番号）はそのまま残した。
- 図 23（$S^2$ の被覆）と図 27 は模式図で、低解像度の目視のみ（重なり・はみ出しなし）。

## 残る懸念（担当範囲の内容。直していない）
1. 滑らかなホモトピーに限った不変性で、連続ホモトピーへの拡張は Whitney 近似の引用に頼る（【文献】）。教科書としては許容範囲。
2. 向きと積分の定義 (2) の well-definedness、座標独立性の証明は簡潔。座標変換と 1 の分割で十分に書かれているが、細部は省略気味。
3. Poincaré 双対・Künneth・$H^n(N)\cong\R$ は主張のみ（本巻の方針どおり）。写像度の定義が $H^n(N)\cong\R$ に依存するので、この依存は本文に明記されている。
4. 連結和の命題の証明で、$M\setminus\{p\}$ のコホモロジーの有限性は「命題の証明の議論」と一言で済ませている。MV 列から従うので誤りではないが、一行補うとより親切。
5. 図 24（写像度の図）の「$y+$整数」は、縦軸の周期（図では約 3）の整数倍の意味。軸の単位を明示するとより正確。

## 担当範囲外の気づき
- 特になし。partA の外積規約表・partC の §5.4 参照（毛玉定理、定理番号は自動）とも整合している。
