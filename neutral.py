# -*- coding: utf-8 -*-

import os
import pickle
import numpy as np
import pandas as pd
import statsmodels.api as sm

industry = pd.read_pickle(r'C:/Users/wuwangchuxin/Desktop/yinhua_\
    min/data/industry.pkl').drop_duplicates()

def Neutral_process(alpha_data):
    num_mint = alpha_data.shape[1]
    num_inds = industry.shape[1]
    data = pd.merge(alpha_data, industry, on=['code']).dropna()
    X = data.iloc[:, [1:num_mint+1]
    y = data.iloc[:, [num_mint+1:num_mint+num_inds+1]]
    X.apply(lambda x: sm.OLS(X, y).fit.resid, inplace=True)
    X['code'] = alpha_data['code']
    output = open(r'G:/short_period_mf/netual_process/netual_%s'%saf[-16:],'wb')
    pickle.dump(X,output)
    output.close()
    return 0
