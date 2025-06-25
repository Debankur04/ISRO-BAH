def read_satellite_bands(): return 'rasterio'
def clip_raster_to_boundary(): pass
def write_processed_raster(): pass
def extract_pixel_values(): pass
def reproject_resample_raster(): pass


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
