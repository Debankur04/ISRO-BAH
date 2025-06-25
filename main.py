from executor import execute_workflow

workflow = [
    {"action": "read_satellite_bands", "output": "vector_meta"},
    {"action": "convert_crs_geodata", "input": "vector_meta", "output": "converted_data"},
    {"action": "read_satellite_bands", "output": "raster_data"},
    {"action": "classify_ndvi", "input": "raster_data", "output": "ndvi_result"}
]

env, results = execute_workflow(workflow)

print("Final Environment:")
print(env)
print("\nResults_Log:")
for r in results:
    print(r)
