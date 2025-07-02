
from django.shortcuts import render, redirect
import random

def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 25)
        request.session['attempts'] = 0
    return render(request, 'game/index.html')



def guess(request):
    if request.method == 'POST':
        guess = int(request.POST['guess'])
        number = request.session.get('number')
        attempts = request.session.get('attempts', 0) + 1
        request.session['attempts'] = attempts

        if guess < number:
            message = "Too low!"
        elif guess > number:
            message = "Too high!"
        else:
            message = f"🎉 Correct! You guessed it in {attempts} attempts."
            request.session.flush()  # reset game after success

        return render(request, 'game/index.html', {
            'message': message,
            'guess': guess,
            'attempts': attempts
        })
    return redirect('index')

def restart(request):
    request.session.flush()  # Clears all session data
    return redirect('index')




