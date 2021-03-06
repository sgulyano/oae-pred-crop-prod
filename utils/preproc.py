import pandas as pd

def read_yield(yield_file, area=None):
    df = pd.read_excel(yield_file)
    df = df.sort_values(by='date')
    
    df_group = df.groupby(['area']).sum().sort_values(by='value', ascending=False)[['value']]
    
    if area:
        df_area = df[df.area == area].reset_index()
        df_area = df_area[['date', 'value']]
        df_area.columns = ['ds', 'y']
        
        df_area_norm = pd.DataFrame({'ds':pd.date_range(start=df_area['ds'].min(), end=df_area['ds'].max(), freq='MS'), 'y':0})
        for index, row in df_area.iterrows():
            idx = df_area_norm['ds']==row['ds']
            if sum(idx) != 1:
                raise ValueError('Month/Year is not unique. This is not a monthly data.')
            df_area_norm.loc[idx, 'y'] = row['y']
        
        df_area_norm = df_area_norm.sort_values(by='ds', ascending=False).reset_index(drop=True)
        return df, df_group, df_area_norm
    else:
        return df, df_group

def get_yeild_area(df, area):
    df_area = df[df.area == area].reset_index()
    df_area = df_area[['date', 'value']]
    df_area.columns = ['ds', 'y']
    
    df_area_norm = pd.DataFrame({'ds':pd.date_range(start=df_area['ds'].min(), end=df_area['ds'].max(), freq='MS'), 'y':0})
    for index, row in df_area.iterrows():
        idx = df_area_norm['ds']==row['ds']
        if sum(idx) != 1:
            raise ValueError('Month/Year is not unique. This is not a monthly data.')
        df_area_norm.loc[idx, 'y'] = row['y']
        
    df_area_norm = df_area_norm.sort_values(by='ds', ascending=False).reset_index(drop=True)
    return df_area_norm


def read_annually_data(file):
    df = pd.read_excel(file)
    
    if len(df['date'].dt.year.unique()) != len(df):
        raise ValueError('Year is not unique. This is not an annual data.')
    
#     df_norm = pd.DataFrame({'ds':pd.date_range(start=df['date'].min(), end=df['date'].max(), freq='YS'), 'y':0})
#     for index, row in df_cost.iterrows():
#         idx = df_cost_norm['ds'].dt.year==row['date'].year
#         if sum(idx) != 12:
#             raise ValueError('Year is not unique. This is not an annual data.')
#         df_cost_norm.loc[idx, 'y'] = row['value']
    
    st = pd.Timestamp(df['date'].min().year, 1, 1)
    en = pd.Timestamp(df['date'].max().year, 12, 1)            
    df_norm = pd.DataFrame({'ds':pd.date_range(start=st, end=en, freq='MS'), 'y':0})
    
    for index, row in df.iterrows():
        idx = df_norm['ds'].dt.year==row['date'].year
        if sum(idx) != 12:
            raise ValueError('Doesn\'t match the whole year')
        df_norm.loc[idx, 'y'] = row['value']
    
    df_norm = df_norm.set_index('ds')
    df_norm = df_norm.resample('MS').asfreq().fillna(method='ffill')
    return df_norm.sort_index(ascending=False)


def read_month_data(file, area=None):
    df = pd.read_excel(file)
    df = df.sort_values(by='date', ascending=False)
    if area:
        df_area = df[df.area == area].reset_index()
    else:
        df_area = df.reset_index()
    df_area = df_area[['date', 'value']]
    df_area.columns = ['ds', 'y']
    return df_area.set_index('ds').sort_index(ascending=False)


def read_month_data_area(df, area):
    df = df.sort_values(by='date', ascending=False)
    df_area = df[df.area == area].reset_index()
    df_area = df_area[['date', 'value']]
    df_area.columns = ['ds', 'y']
    return df_area.set_index('ds').sort_index(ascending=False)


def is_harvest_season(row, st=10, en=12):
    if en < st:
        row['harvest_season'] = row['ds'].month >= st or row['ds'].month <= en
    else:
        row['harvest_season'] = row['ds'].month >= st and row['ds'].month <= en
    return row

def rice_inseason_harvest_season(row):
    return is_harvest_season(row, 10, 12)

def rice_offseason_harvest_season(row):
    return is_harvest_season(row, 2, 6)

def corn_harvest_season(row):
    return is_harvest_season(row, 10, 12)

def cassava_harvest_season(row):
    return is_harvest_season(row, 11, 3)

def rubber_harvest_season(row):
    return is_harvest_season(row, 6, 1)


def add_regressor(dfs_new, cols_name):
    def add_regressor_decorator(func):
        def func_wrapper(df):
            df_res = func(df)
            for df_new, col_name in zip(dfs_new, cols_name):
                assert(len(df_new.columns)==1)
                df_res = df_res.join(df_new.rename(columns={'y':col_name}), on='ds')
            return df_res.fillna(method='ffill')
        return func_wrapper
    return add_regressor_decorator

# def add_regressor(df_new, col_name):
#     def add_regressor_decorator(func):
#         def func_wrapper(df):
#             assert(len(df_new.columns)==1)
#             return func(df).join(df_new.rename(columns={'y':col_name}), on='ds')
#         return func_wrapper
#     return add_regressor_decorator