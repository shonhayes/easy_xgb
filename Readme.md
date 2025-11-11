### Project Purpose

This package is designed to simplify protyping xgboost models on relatively simple datasets easier.

##### Project modules

* transform
    * Transforms categorical data either using dummy encoding or orders them using linear   regression
* optimize
    * Optimizes hyperparameters of xgboost model over transformed data.

##### Project use cases

* Designed to spin up a baseline, high-quality model for datasets with relatively high      number of observations per column. Not designed for sparse or wide datasets.
