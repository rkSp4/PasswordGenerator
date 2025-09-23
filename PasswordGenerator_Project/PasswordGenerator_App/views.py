from django.shortcuts import render, redirect
from .models import GenerationLog
import secrets
import string
import random

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    if length < 1:
        raise ValueError("length must be >= 1")
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    symbols = '!@#$%^&*()-_=+[]{};:,.<>?/' if use_symbols else ''
    alphabet = lower + upper + digits + symbols
    if not alphabet:
        raise ValueError("No character sets selected")

    password_chars = []
    # Guarantee variety if those sets are chosen
    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        password_chars.append(secrets.choice(symbols))

    while len(password_chars) < length:
        password_chars.append(secrets.choice(alphabet))

    # Shuffle using SystemRandom for secure shuffle
    rand = random.SystemRandom()
    rand.shuffle(password_chars)
    return ''.join(password_chars[:length])

def home(request):
    password = ''
    error = ''
    form = {
        'length': 12,
        'use_upper': True,
        'use_digits': True,
        'use_symbols': True
    }

    if request.method == 'POST':
        try:
            length = int(request.POST.get('length', 12))
        except ValueError:
            length = 12
        use_upper = request.POST.get('use_upper') == 'on'
        use_digits = request.POST.get('use_digits') == 'on'
        use_symbols = request.POST.get('use_symbols') == 'on'

        form.update({
            'length': length,
            'use_upper': use_upper,
            'use_digits': use_digits,
            'use_symbols': use_symbols
        })

        try:
            password = generate_password(length=length,
                                         use_upper=use_upper,
                                         use_digits=use_digits,
                                         use_symbols=use_symbols)
            # optionally log metadata only (safe)
            try:
                GenerationLog.objects.create(
                    length=length,
                    use_upper=use_upper,
                    use_digits=use_digits,
                    use_symbols=use_symbols
                )
            except Exception:
                # logging shouldn't break UX; ignore DB errors silently
                pass

        except ValueError as e:
            error = str(e)

    return render(request, 'home.html', {'password': password, 'error': error, 'form': form})
