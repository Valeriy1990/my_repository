from scipy import stats

t = float(input('t for both tails:'))  # Значнние коэффициента Стьюдента t 
df = int(input('Degrees of freedom:'))  # Значение степеней свободы df = N -1
p_value = 2*(1-stats.t.cdf(t, df))  # 2* если двухсторонее, убрать 2 для одностороннего
print('P(X <',-t,'or X >', t,') = %6.4f'  %(p_value))