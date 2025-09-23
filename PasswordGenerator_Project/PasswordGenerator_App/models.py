from django.db import models

class GenerationLog(models.Model):
    length = models.PositiveIntegerField()
    use_upper = models.BooleanField(default=True)
    use_digits = models.BooleanField(default=True)
    use_symbols = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"len={self.length} upper={self.use_upper} digits={self.use_digits} symbols={self.use_symbols} @ {self.created_at:%Y-%m-%d %H:%M}"
