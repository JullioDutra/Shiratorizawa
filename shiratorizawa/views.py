from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from .models import Match, Player, Highlight, GalleryImage
from .forms import NewsletterForm
from django.contrib import messages

def index(request):
    matches = Match.objects.order_by('date')[:3]
    players = Player.objects.all()[:3]
    highlights = Highlight.objects.filter(year=2022)
    gallery = GalleryImage.objects.all()[:8]
    
    return render(request, 'index.html', {
        'matches': matches,
        'players': players,
        'highlights': highlights,
        'gallery': gallery
    })


@require_POST
def confirmar_presenca(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    match.confirmed_fans += 1
    match.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))


def newsletter_subscribe(request):
    form = NewsletterForm()
    success_message = None

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Inscrição realizada com sucesso!"

    return render(request, 'sua_template.html', {
        'form': form,
        'success_message': success_message
    })
    
    
def confirmar_contribuicao(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        if nome:
            # Aqui você pode salvar no banco se quiser
            messages.success(request, f"Obrigado, {nome}, por sua contribuição!")
        return redirect("index")  