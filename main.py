import geopandas as gpd
import shapely
import numpy as np
import matplotlib.pyplot as plt


# wczytanie pliku
gdf = gpd.read_file('PD_STAT_GRID_CELL_2011.shp')
gdf = gdf.to_crs("EPSG:4326")
gdf['centroid'] = gdf.centroid


# utworzenie siatki
xmin, ymin, xmax, ymax = [13, 48, 25, 56]

n_cells = 30
cell_size = (xmax - xmin)/n_cells

grid_cells = []
for x0 in np.arange(xmin, xmax+cell_size, cell_size):
    for y0 in np.arange(ymin, ymax+cell_size, cell_size):
        x1 = x0 - cell_size
        y1 = y0 + cell_size
        grid_cells.append(shapely.geometry.box(x0, y0, x1, y1))
cell = gpd.GeoDataFrame(grid_cells, columns=['geometry'])


# spatial join i agregacja
merged = gpd.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")


#a
cell.loc[dissolve.index, 'TOT_0_14'] = dissolve.TOT_0_14.values

ax = cell.plot(column='TOT_0_14', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności w siatce dla przedziału wiekowego 0-14')


#b
cell.loc[dissolve.index, 'TOT_15_64'] = dissolve.TOT_15_64.values

ax = cell.plot(column='TOT_15_64', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności w siatce dla przedziału wiekowego 15-64')


#c
cell.loc[dissolve.index, 'TOT_65__'] = dissolve.TOT_65__.values

ax = cell.plot(column='TOT_65__', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności w siatce dla przedziału wiekowego >65')


#d
cell.loc[dissolve.index, 'MALE_0_14'] = dissolve.MALE_0_14.values

ax = cell.plot(column='MALE_0_14', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności męskiej w siatce dla przedziału wiekowego 0-14')

cell.loc[dissolve.index, 'MALE_15_64'] = dissolve.MALE_15_64.values

ax = cell.plot(column='MALE_15_64', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności męskiej w siatce dla przedziału wiekowego 15-64')

cell.loc[dissolve.index, 'MALE_65__'] = dissolve.MALE_65__.values

ax = cell.plot(column='MALE_65__', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności męskiej w siatce dla przedziału wiekowego >65')


#e
cell.loc[dissolve.index, 'FEM_0_14'] = dissolve.FEM_0_14.values

ax = cell.plot(column='FEM_0_14', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności żeńskiej w siatce dla przedziału wiekowego 0-14')

cell.loc[dissolve.index, 'FEM_15_64'] = dissolve.FEM_15_64.values

ax = cell.plot(column='FEM_15_64', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności żeńskiej w siatce dla przedziału wiekowego 15-64')

cell.loc[dissolve.index, 'FEM_65__'] = dissolve.FEM_65__.values

ax = cell.plot(column='FEM_65__', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('liczba ludności żeńskiej w siatce dla przedziału wiekowego >65')


#f
woj = gpd.read_file('Województwa.shp')
woj = woj.to_crs("EPSG:4326")
woj['centroid'] = woj.centroid

merged = gpd.sjoin(gdf, woj, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="mean")

woj.loc[dissolve.index, 'FEM_RATIO'] = dissolve.FEM_RATIO.values

ax = woj.plot(column='FEM_RATIO', figsize=(12,8), cmap='viridis', edgecolor="grey", legend=True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal')
plt.title('Ratio liczby ludności do powierzchni dla danego województwa')
