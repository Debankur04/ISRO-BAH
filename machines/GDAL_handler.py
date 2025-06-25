def reproject_large_raster(): pass
def crop_merge_satellite_images(): pass
def convert_geotiff_to_png(): pass
def extract_raster_metadata(): pass
def align_rasters_with_warp(): pass


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
