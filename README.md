
# mRMR

mRMR: "Feature Selection Based on Mutual Information: Criteria of Max-Dependency, Max-Relevance, and Min-Redundancy" IEEE PAMI, 2005

Current state:
- (1) Formulas of Max-Relevanve and Min-Redundancy.
- (1.0) Shannon entropy testing: I[X,Y] less/equal min(H[X], H[Y]) (unfinished).
- (1.1) Symmetric testing: I[Xi, Xj] = I[Xj, Xi].
- (1.2) Mutual information estimation of continuous data.
- (2) Stage1: incremental algorithm optimization (local optimal).
- (3) Stage2: wrapper (unfinished).

Files:
- [ ARR.py ] : Arrhythmia dataset parser, generate arrhythmia.bin (I[Xi, Y], I[Xi, Xj]).
- [ moduleinfo.py ] : Mutual information calculation ].
- [ mRMR v1.py ] : Feature selection scheme.
- [ test condensity.py ] : Mutual information estimation of continuous data.

Results:
- [v1]: (http://felisj-blog.logdown.com/posts/318832-mrmr)

# Citation

	@article{Peng2005pami, 
	  author={Peng, H. and Fulmi Long and Ding, C.}, 
	  journal={Pattern Analysis and Machine Intelligence, IEEE Transactions on}, 
	  title={Feature selection based on mutual information criteria of max-dependency, max-relevance, and min-redundancy}, 
	  year={2005}, 
	  volume={27}, 
	  number={8}, 
	  pages={1226-1238}
	}
