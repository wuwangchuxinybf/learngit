# -*- coding: utf-8 -*-

import os
import pickle
import numpy as np
import pandas as pd
import statsmodels.api as sm

industry = pd.read_pickle('C:/Users/wuwangchuxin/Desktop/yinhua_\
    min/data/industry.pkl').drop_duplicates()

return_data = pd.read_pickle('G:short_period_mf/dailyreturn.pick\
    le').rename(columns={'symbol':'code'})

def Neutral_process(alpha_data, saf):
    num_mint = alpha_data.shape[1]
    num_inds = industry.shape[1]
    data = pd.merge(alpha_data, industry, on=['code']).dropna()
    X = data.iloc[:, [1:num_mint+1]]
    y = data.iloc[:, [num_mint+1:num_mint+num_inds+1]]
    X.apply(lambda x: sm.OLS(X, y).fit.resid, inplace=True)
    X['code'] = alpha_data['code']
    output = open(r'G:/short_period_mf/netual_process/netual_%s'%saf[-16:],'wb')
    pickle.dump(X,output)
    output.close()
    retutn 0

def IC_computing(alpha_data, saf):
    data = pd.merge(alpha_data,return_data,on = ['code'])
    dailyReturn = data.daily_return
    factors = Netual_process(alpha_data)
    IC = dailyReturn.corr(factors, method='spearman')
    output = open(r'G:/short_period_mf/ic_value/ic_%s'%saf[-16:],'wb')
    pickle.dump(IC,output)
    output.close()    
    return 0


################
standard_alpha = os.listdir(r'G:/short_period_mf/alpha_min_stand')
for saf in standard_alpha:
    alpha_d = pd.read_pickle(r'G:/short_period_mf/alpha_min_stand/%s'%saf)
    IC_computing(alpha_d, saf)


for saf in standard_alpha:
    alpha_d = pd.read_pickle(r'G:/short_period_mf/alpha_min_stand/%s'%saf)
    Neutral_process(alpha_d,saf)
