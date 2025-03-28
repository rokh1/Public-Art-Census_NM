import geopandas as gpd
import fiona
import os

gdb_path = r"C:\Users\ureka\OneDrive\Documents\ArcGIS\Projects\ABQ\ABQ.gdb"
output_folder = r"C:\Users\ureka\OneDrive\Documents\ArcGIS\Projects\ABQ\converted_geojson"

os.makedirs(output_folder, exist_ok=True)
layers = fiona.listlayers(gdb_path)

for layer in layers:
    try:
        print(f"Reading {layer}...")
        gdf = gpd.read_file(gdb_path, layer=layer, engine="fiona")
        out_path = os.path.join(output_folder, f"{layer}.geojson")
        gdf.to_file(out_path, driver='GeoJSON')
        print(f"✅ Exported {layer} to {out_path}")
    except Exception as e:
        print(f"❌ Skipped {layer} due to error: {e}")
