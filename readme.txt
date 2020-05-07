Guideline
1. The code is design based on Python 2.7.15 and Scikit-learn 0.20.4 with the dependence of Biopython 1.72,Numpy 1.16.5,Pandas 0.24.2.
2. The input sequence should be the full sequences of spike protein (S) of coronavirus as fasta format. The raw data should not be aligned as input!
3. "CovPred_FL.py" is the main file to run.
4. The folder "feature" contains the GGAP features with parameter 3.
5. The folder "model" contains the trained model based on random forest algorism and the dataset in the paper.
6. "predicting_results.csv" is the result file for the prediction of interspecies transmission.
7. The predicted label for 'H' means the transmission phenotype of interspeices, while label for 'N' means not.
8. The cutoff value should be smaller when you want strict result. 0.5 is always OK!

Reference
1. Qiang, X., Xu, P., Fang, G. et al. Using the spike protein feature to predict infection risk and monitor the evolutionary dynamic of coronavirus. Infect Dis Poverty 9, 33 (2020). https://doi.org/10.1186/s40249-020-00649-8
https://idpjournal.biomedcentral.com/articles/10.1186/s40249-020-00649-8
