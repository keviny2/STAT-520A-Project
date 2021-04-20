# STAT-520A-Project

## Proposal

A Markov chain is a model that tells us something about the probabilities of sequences of random variables and states, each of which can take on values from some set (Jurafsky and Martin, 2020). A Hidden Markov Model, or HMM, is a generalization of a Markov chain and allows for analysis on both observed and hidden states (Fonzo et al, 2007). Currently, HMMs have become standard in statistics and are widely used in bioinformatics, econometrics and statistical signal processing (Ryden, 2008). In a 1970 paper, Baum et al. introduced an EM algorithm - commonly known as the "Baum-Welch algorithm", to learn the model parameters of an HMM given an observation set. In recent years, we have seen an interest in approaching these learning problems using a Bayesian approach. Some examples include: Bayesian Structural Inference, which relies on a set of candidate unifiliar HMM topologies for inference of process structure from a data series (Strelioff and Crutchfield, 2013); and Bayesian Baum-Welch, a model primarily applied in Bioinformatics, that integrates chromosomal spatial information to perform inference (Seifert et al., 2011). Motivated by these examples and their exceptional performance, we propose to implement a Gibbs sampler introduced by Tobias Ryden to tackle the learning problem (Ryden, 2008). Subsequently, we will contrast the Baum-Welch algorithm with Ryden's Gibbs sampler and discuss each one's limitations and strengths. 

### Works Cited

*Jurafsky, and James Martin. Speech and Language Processing. , 30 Dec. 2020.

*Eddy, Sean R. Multiple Alignment Using Hidden Markov Models. , 1995.

*Zahn, Hans, et al. “Scalable Whole-Genome Single-Cell Library Preparation without           Preamplification.” Nature Methods, vol. 14, no. 2, 1 Feb. 2017, pp. 167–173,              pubmed.ncbi.nlm.nih.gov/28068316/, 10.1038/nmeth.4140. Accessed 11 Feb. 2021.
