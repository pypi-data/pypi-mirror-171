# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:39:06 2019

@author: Jinyi Zhang
"""

import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from qstock.data.money import stock_money

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#计算数据在系列时间周期内的收益率
#运用在同花顺板块概念选股
def date_ret(data,w_list=[1,5,20,60,120]):
    df=pd.DataFrame()
    for w in w_list:
        df[str(w)+'日收益率%']=(((data/data.shift(w)-1)*100)
                            .round(2)
                            .iloc[w:]
                            .fillna(0)
                            .T
                            .iloc[:,-1])
    return df

#计算某期间动量排名
def stock_rets_rank(data,w_list=[1,5,20,60,120],c=4):
    #c为w_list里第几个
    rets=date_ret(data,w_list)
    col=rets.columns[c]
    rank_ret=rets.sort_values(col,ascending=False)
    return rank_ret

#同花顺概念动量排名
def ths_top(ths_rets,n=10):
    ths_top=pd.DataFrame()
    for c in ths_rets.columns:
        ths_top[c]=ths_rets.sort_values(c,ascending=False)[:n].index
    return ths_top

#获取同花顺概念指数动量排名名称列表
def ths_top_list(ths_top):
    alist=ths_top.values.tolist()
    words=' '.join([' '.join(s) for s in alist])
    word_list=words.split(' ')
    w_set=set(word_list)
    w_data=[]
    for w in w_set:
       w_data.append([w,word_list.count(w)/len(word_list)])
    return w_data

#rps选股
class RPS(object):
    pass
    print('策略代码仅供知识星球会员使用')
        
#量价选股（参考欧奈尔的带柄茶杯形态）
#筛选价格和成交量突破N日阈值的个股
def find_price_vol_stock(data,n=120,rr=0.5):
    pass
    print('策略代码仅供知识星球会员使用')

#MM趋势选股（Mark Minervini’s Trend Template）
#参考文章https://zhuanlan.zhihu.com/p/165379657
#股票价格高于150天均线和200天均线
#1、150日均线高于200日均线
#2、200日均线上升至少1个月
#3、50日均线高于150日均线和200日均线
#4、股票价格高于50日均线
#5、股票价格比52周低点高30%
#6、股票价格在52周高点的25%以内
#7、相对强弱指数(RS)大于等于70，这里的相对强弱指的是股票与大盘对比，RS = 股票1年收益率 / 基准指数1年收益率
#这里将第七条RS改为欧奈尔的相对强弱指标，与RPS选股结合选择大于90值的股票

def MM_trend(close,sma=50,mma=150,lma=200):
    """close: 股票收盘价
    """
    pass
    print('策略代码仅供知识星球会员使用')

def tscode(code):
    return code+'.SH'if code.startswith('6') else code+'.SZ'

#资金流选股
def moneyflow_stock(codes,w_list=[3,5,10,20,60]):
    code_list=[]
    for s in tqdm(codes):
        s=s[:6]
        try:
            if all(stock_money(s,w_list).iloc[-1]>0):
               code_list.append(s)
        except:
            continue
    
    code_list=[tscode(c) for c in code_list]
    return code_list


#计算营收和利润增长得分
def cal_yoy(y,a):
    '''y是总资产报酬率时a=5
    y是营业收入增长率时a=10
    y是净资产收益率是a=15
    y是营业利润增长率a=20
    '''
    try:
        return 5+ min(round(y-a),5) if y>=a else 5+ max(round(y-a),-5)
    except:
        return 0
    
def cal_exp(y,a):
    '''y是毛利率或期间费用率a=0.5
     y是存货周转率a=2
     y是每股经营性现金流a=4
    '''
    try:
       return 5+min(round(y)/a,5) if y>0 else max(round(y)/a,-5)+5
    except:
       return 0
        
def cal_roa(y):
    #总资产报酬率打分
    try:
        return min(round((y-5)/0.5),10) if y>=5 else max(round(y-5),0)
    except:
        return 0
    
def cal_pepb(y,a,b):
    '''y是市净率时，a=3,b=0.4
      y是动态市盈率相对盈利增长率时，a=1,b=0.1
    '''
    try:
        return 5-max(round((y-a)/b),-5) if y<=a else 5-min(round((y-a)/b),5)
    except:
        return 0

#财务指标打分系统
##获取个股财务指标（指定某几个指标）+pe市盈率+pb市净率
fields='ts_code,ann_date,end_date,tr_yoy,op_yoy,\
         grossprofit_margin,expense_of_sales,inv_turn,eps,\
         ocfps,roe_yearly,roa2_yearly,netprofit_yoy,update_flag'
#update_flag财务数据是否更新过
def indicator_score(tudata,code,pepb=True,fields=fields):
    pass
    print('策略代码仅供知识星球会员使用')

#计算所有股票财务指标总分
def all_indicator_score(tudata,name_code_dict):
    df=pd.DataFrame()
    for name,code in tqdm(name_code_dict.items()):
        try:
            d1=indicator_score(tudata,code)['总分']
            d1=pd.DataFrame(d1).rename(columns={'总分':name})
            df=pd.concat([df,d1],axis=1)
            
        except:
            continue
    return df

