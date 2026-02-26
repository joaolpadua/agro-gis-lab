import geopandas as gpd

# Caminho do shapefile
shp_path = r"data\SP_Municipios_2024.shp"

# Lendo o shapefile
gdf = gpd.read_file(shp_path)

print("Total de municípios:", len(gdf))
print("CRS atual:", gdf.crs)

print("\nColunas disponíveis:")
print(gdf.columns)

print("\nPrimeiras linhas:")
print(gdf.head())