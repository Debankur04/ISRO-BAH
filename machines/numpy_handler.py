def classify_ndvi_raster(): return 'numpy'
def run_dem_filter_window(): pass
def aggregate_pixel_statistics(): pass
def mask_raster_array(): pass
def compute_multi_band_index(): pass


# Template for all handler files
def some_action(): return "something"
def another_action(): return 42

def run(action, step, env):
    func = globals().get(action)
    if callable(func):
        return func()
    raise AttributeError(f"No function named '{action}' found.")
