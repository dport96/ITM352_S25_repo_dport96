packages = {
    'scipy': 'scipy',
    'statsmodels': 'statsmodels',
    'matplotlib': 'matplotlib'
}

for name, module_name in packages.items():
    try:
        __import__(module_name)
        print(f"{name} is installed.")
    except ImportError:
        print(f"{name} is NOT installed.")
