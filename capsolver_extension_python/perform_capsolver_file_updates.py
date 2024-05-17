

def perform_capsolver_file_updates(ext, api_key, app_id):

    def update_js_contents(content):
        to_replace = "return e.defaultConfig"
        app_id_str = f", appId: '{app_id}'" if app_id else ""
        replacement = (
            f"return {{ ...e.defaultConfig, apiKey: '{api_key}'{app_id_str} }}"
        )
        return content.replace(to_replace, replacement)
    
    for file in ext.get_js_files():
        file.update_contents(update_js_contents)
    
    def update_config_contents(content):
        key_replaced = content.replace("apiKey: '',", f"apiKey: '{api_key}',")
        # When you use the Capsolver Extension, we integrate our own app ID into the extension if you haven't provided one. This allows us to earn a small commission from each captcha you solve, at no extra cost to you. 
        # This supports us in our efforts to develop awesome open-source projects to make your life easy.
        if not app_id:
            default_app_id = "DC601421-43D5-45E4-9FDB-B3BAF7A2C3FD"
            app_id = default_app_id

        if app_id:
            key_replaced = key_replaced.replace("appId: '',", f"appId: '{app_id}',")
        return key_replaced
    
    ext.get_file("/assets/config.js").update_contents(update_config_contents)