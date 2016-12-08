
import pandas as pd
import os
import matplotlib.pylab as plt
%matplotlib inline

user_info_train = pd.read_csv('./Credit/train/user_info_train.txt',names=['ID','gender','career','education','marriage','hukou'],header=None)
bank_detail_train = pd.read_csv('./Credit/train/bank_detail_train.txt',names=['ID','timestamp_bank','type','money','salary'],header=None)
browse_history_train = pd.read_csv('./Credit/train/browse_history_train.txt',names=['ID','timestamp_browse','browse_data','browser_code'],header=None)
bill_detail_train = pd.read_csv('./Credit/train/bill_detail_train.txt',names=['ID','timestamp_bill','bank_id','last_bill','last_repayment','credit_line','current_balance','minimum_payments','amount_transactions','current_money','adjust_money','cycle_interest','available_money','cash_advance','repayment_status'],header=None)
loan_time_train = pd.read_csv('./Credit/train/loan_time_train.txt',names=['ID','timestamp_money'],header=None)
overdue_train = pd.read_csv('./Credit/train/overdue_train.txt',names=['ID','Label'],header=None)


user_info_test = pd.read_csv('./Credit/test/user_info_test.txt',names=['ID','gender','career','education','marriage','hukou'],header=None)
bank_detail_test = pd.read_csv('./Credit/test/bank_detail_test.txt',names=['ID','timestamp_bank','type','money','salary'],header=None)
browse_history_test = pd.read_csv('./Credit/test/browse_history_test.txt',names=['ID','timestamp_browse','browse_data','browser_code'],header=None)
bill_detail_test = pd.read_csv('./Credit/test/bill_detail_test.txt',names=['ID','timestamp_bill','bank_id','last_bill','last_repayment','credit_line','current_balance','minimum_payments','amount_transactions','current_money','adjust_money','cycle_interest','available_money','cash_advance','repayment_status'],header=None)
loan_time_test = pd.read_csv('./Credit/test/loan_time_test.txt',names=['ID','timestamp_money'],header=None)
usersID_test= pd.read_csv('./Credit/test/usersID_test.txt',names=['ID','Label'],header=None)

data_user_train = pd.merge(user_info_train,pd.merge(loan_time_train,overdue_train,on='ID',how='inner'),on='ID',how='inner')

data_user_test = pd.merge(user_info_test,pd.merge(loan_time_test,usersID_test,on='ID',how='inner'),on='ID',how='inner')

data_user_test.head()


data_user_train = data_user_train.apply(lambda x:x.astype(str))
data_user_test = data_user_test.apply(lambda x:x.astype(str))

def rep(dataframe):
    print('Replicate data:',sum(dataframe.duplicated()))
rep(data_user_train)
rep(data_user_test)
