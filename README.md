
# mRMR

mRMR: "Feature Selection Based on Mutual Information: Criteria of Max-Dependency, Max-Relevance, and Min-Redundancy" IEEE PAMI, 2005

Current state:
- (1) formulas of Max-Relevanve and Min-Redundancy.
- (1.0) Shannon entropy testing: I[X,Y] less/equal min(H[X], H[Y]) (unfinished).
- (1.1) Symmetric testing: I[Xi, Xj] = I[Xj, Xi].
- (2) stage1: incremental algorithm optimization (local optimal).
- (3) stage2: wrapper (unfinished).

Files:
- [ ARR.py ] : arrhythmia dataset parser, generate arrhythmia.bin (I[Xi, Y], I[Xi, Xj])
- [ moduleinfo.py ] : mutual information calculation ]
- [ mRMR v1.py ] : feature selection scheme

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
