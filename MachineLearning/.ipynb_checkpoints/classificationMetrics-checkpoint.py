#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Classification Metrics

                  Positive           Negative
*** Positive   *True Positive     False Negative
*** Negative   False Positive     *True Negaitve

Accuracy = (TP + TN) / m
Precision = TP / (TP + FP)
Recall = TP / (TP + FN)

increasing precision = reducing false positives
increasing recall = reducing false negatives

F(beta) score is harmonic mean of precision and recall and beta ** 2 is weight assigned to recall.

beta is more = more importance to recall = more importance to reduce false negatives
beta is less = more importance to precision = more importance to reduce false positives

F1 Score    = 1 / 0.5 * (1/Precision + 1/Recall) = 2 * Precision * Recall / (Precision + Recall)
F2 Score    = 1 / (1/ (1+2^2) * Precision + 2^2 / (1+2^2) * Recall)
            = (1 +   2^2) * Precision * Recall / (  2^2 * Precision + Recall)
F0.5 Score  = (1 + 0.5^2) * Precision * Recall / (0.5^2 * Precision + Recall)

sensitivity, recall, hit_rate, true_positive_rate = TP / (TP + FN) = TP / Total Positives

specificity, selectivity, true_negative_rate = TN / (TN + FP) = TN / Total Negatives

precision, positive_predictive_value = TP / (TP + FP) = TP / Total Predicted Positives

negative_predictive_value = TN / (TN + FN) = TN / Total Predicted Negatives

miss_rate, false_negative_rate = FN / (FN + TP) = FN / Total Positives

fall_out, false_positive_rate = FP / (FP + TN) = FP / Total Negatives

false_discovery_rate = FP / (TP + FP) = FP / Total Predicted Positives

false_omission_rate = FN / (TN + FN) = FN / Total Predicted Negatives

threat_score = TP / (TP + FN + FP)

balanced_accuracy = (TPR + TNR) / 2

AUC (receiver_operating_characteristicks) = TPR vs FPR

cross_entropy(p, q): -sum(p*log2(q)) for multiclass classification
"""
import numpy as np

data = np.loadtxt('./y_fashion_mnist_cnn.csv')
y_true = data[0]
y_pred = data[1]

from sklearn.metrics import precision_score, recall_score, fbeta_score, f1_score

print(precision_score(y_true, y_pred, average=None))
print(recall_score(y_true, y_pred, average=None))
print(f1_score(y_true, y_pred, average='macro'))
print(fbeta_score(y_true, y_pred, beta=2, average='macro'))
