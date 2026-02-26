import geopandas as gpd

shp_path = r"data\SP_Municipios_2024.shp"

gdf = gpd.read_file(shp_path)

print("CRS original:", gdf.crs)

# Reprojetando para UTM zona 23S
gdf_utm = gdf.to_crs(epsg=31983)

# Calculando área em m²
gdf_utm["area_m2"] = gdf_utm.geometry.area

# Convertendo para km²
gdf_utm["area_calc_km2"] = gdf_utm["area_m2"] / 1_000_000

print(gdf_utm[["NM_MUN", "area_calc_km2"]].head())

gdf_utm[["NM_MUN", "area_calc_km2"]].to_csv("areas_calculadas.csv", index=False)