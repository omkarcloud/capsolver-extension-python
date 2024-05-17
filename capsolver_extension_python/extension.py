from chrome_extension_python import Extension
from .perform_capsolver_file_updates import perform_capsolver_file_updates

class Capsolver(Extension):
    def __init__(self, api_key, app_id=None):
        if api_key == "CAP-MY_KEY":
            raise ValueError("You need to replace CAP-MY_KEY with your actual Capsolver API key.")
        
        super().__init__(
            extension_id="pgojnojmmhpofjgdmaebadhbocahppod",
            extension_name="capsolver",
            api_key=api_key,
            app_id=app_id,
        )

    def update_files(self, api_key, app_id):
        perform_capsolver_file_updates(self, api_key, app_id)