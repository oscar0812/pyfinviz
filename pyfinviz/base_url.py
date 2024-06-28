def get_url(path, api_key=None):
    if path is None:
        raise ValueError("path must be provided")
    
    if api_key is not None:
        return f'https://elite.finviz.com/{path}.ashx?auth={api_key}&'
    return f'https://finviz.com/{path}.ashx?'