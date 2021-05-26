#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:04:59 2021

@author: mahan
"""

#%% Chapter 1

"""
Definitions:  
    General:
        Machine learning as science of programming computers to learn from 
        data.
    
    Arthur Samuel:
        A field of study which allows computers to learn without being 
        explicitly programmed.
    
    Tom Mitchell:
        A computer is said to have learn from experience (E) if its 
        performance (P) to perform some task (T) increases with experience (E).

When to use machine learning:
    When a program requires a lot of hand tuning or long list of rules.
    
    When a program needs to adapt to changing environment.
    
    When a problem is too complex to program.
    
    When there is a need to identify unsuspected correlations to better 
    understand the problem or to discover patterns in the data - data mining
    
Types of machine learning:
    What is the outcome:
        supervised:
            classification, regression
        
        un-supervised: 
            clusstering, dimensionality reduction, association learning, or
            anamoly detection
        
        semi-supervised:
            combination of supervised and un-supervised learning
        
        reinforcement learning:
            agent learn a policy to choose an action in a given situation
    
    How is data coming:
        online (incremental) learning
        batch learning
    
    Underlying basis:
        instance-based learning
        model-based learning

Process of ML development:
    Analyse the problem (formulate problem)
    Collect the data (data collection)
    Study the data (data visualisation)
    Prepare the data (data pre-processing)
    Select a model
    Train and fine-tune the model
    Test the model
    Launch, monitor, and maintain
    
Challenges:
    Insufficient quantity of data
    
    Non-representative training data:
        small dataset: sampling noise
        large dataset: sampling bias
    
    Poor quality data:
        errors, outliers, and noise
        remove feature, remove instance, or fill missing values
    
    Irrelevant features:
        Feature engineering:
            Feature selection
            Feature extraction
            Collect new features
    
    Overfitting:
        How to identify:
            low training error; high validation or test errors
        
        What is the reason:
            when the model is too complex relative to amount and noise of the 
            data model starts learning the noise of the training dataset
        
        Solutions:
            simplify model, reduce features, constrain model (regularisation), 
            more data, or reduce noise
        
    Underfitting:
        How to identify:
            high training, validation, and test errors
        
        What is the reason:
            when the model is too simple to learn the underlying structure of 
            the data
        
        Solutions:
            more powerful model, more features, deconstrain model

Testing and validation:
    cross-validation to avoid wasting traning data for validation
    generalisation error or out-of-sample error
"""