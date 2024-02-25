# from nep_3D import nep_regression_3D
from get_points import get_data3D
import plotly.graph_objs as go
# get_data3D(name_file)[0] - X
# get_data3D(name_file)[1] - Y
# get_data3D(name_file)[2] - Z

proc = 0
name_file = f'dataXYZ_{proc}.txt'
x = get_data3D(name_file)[0]
y = get_data3D(name_file)[1]
z = get_data3D(name_file)[2]
# nep_regression_3D(x, y, z)

fig = go.Figure()
fig.add_trace(go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(color='blue', size=2), name='Исходные данные'))
# fig.add_trace(
#     go.Surface(x=X_grid, y=Y_grid, z=Z_grid, colorscale='blackbody', opacity=0.3, name='Регрессия Надарая-Ватсон'))
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  legend=dict(x=0, y=1, traceorder='normal'))
fig.show()