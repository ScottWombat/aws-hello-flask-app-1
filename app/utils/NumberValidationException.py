
class NumberValidationException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message = kwargs.get('message')
    
    def __str__(self):
        return self.message
