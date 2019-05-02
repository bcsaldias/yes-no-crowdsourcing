# A Full Probabilistic Model for Yes/No Type Crowdsourcing in Multi-Class Classification

The resources in this repository are part of the proposed model and experiments described in "A Full Probabilistic Model for Yes/No Type Crowdsourcing in Multi-Class Classification" (https://arxiv.org/abs/1901.00397).


## Data

As describe in the paper, we set up two experiments: 1) labeling irregular time-series of the Catalina Surveys; 2) labeling animals.

In each folder, *catalina* and *animals* (respectively to experiments 1) and 2)), you can find four files:
- `objects.csv`: contains each object presented to the labelers, along with some features that we used to inform the users (not all of them where shown, but we make all data available). In addition, the last four variables: `Var_Type`, `_training`, `_validation`, `_abc`, indicate the ground truth, whether the objects are part of the prior credibilities training process, used for test or validations, plus a variable that indicates whether the object was also used to ask ABCD questions to the labelers, respectively.
    
- `users.csv`: indicates how many questions were randomly assigned to each user when they enrolled the labeling task - note that not all users annotated all objects; hence, we worked with the ones that completed at least 70\% of the task.
    
- `votes_abcd.cs`
    
- `votes_yn.cs`
    

## Implementation details and usage


#### 00. PYMC | BBVI - Bayesian YN question type
A documented implementation of the proposed model and some tests/results in its two versions: using PYMC3 and BBVI. All implemented equations are referenced to the paper (and supplementary material) equations numbers. The supplementary material provides the derivation of the needed gradients to solve the model, which can be easily extended to any model with similar variable types, and you can find these derivations implemented in this notebook.

#### 01. PYMC - Bayesian ABCD question type
A documented implementation and some tests/results of the baseline model.


## Acknowledgements

Our work was supported in part by the CSS survey, which is funded by the National Aeronautics and Space Administration under Grant No. NNG05GF22G issued through the Science Mission Directorate Near-Earth Objects Observations Program. We would also like to thank the anonymous reviewers whose comments greatly improved this manuscript. 
