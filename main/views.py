from django.shortcuts import render,redirect
from .models import *
def Index(request):
    context = {
        'main':MainMenu.objects.last(),
        'mainabout': MainAbout.objects.last(),
        'aboutservice':AboutusServices.objects.all()[:3],
        'otherabout': OtherAbouts.objects.last(),
        'CardServices': ServicesCards.objects.all()[:6],
        'cardchoose':CardChoose.objects.all()[:6],
        'chooseabout':ChooseAbout.objects.all()[:4],
        'portfoliotype':PortfoliosType.objects.all(),
        'portfolios':Portfolios.objects.all(),
        'testimonial': TestimonialsComment.objects.all(),
        'members': TeamMembers.objects.all(),
        'client': MainClients.objects.last(),
        'contact': ContactUs.objects.last(),
        'companyname':CompanyName.objects.last(),
        'news':NewsLetter.objects.last(),
        'official':OfficialLink.objects.last(),
        'logo':LogoImg.objects.last()
    }
    return render(request,'index.html',context)

def PortfoliosSingle(request, pk):
    context = {
        'main': MainMenu.objects.last(),
        'mainabout': MainAbout.objects.last(),
        'aboutservice': AboutusServices.objects.all()[:3],
        'otherabout': OtherAbouts.objects.last(),
        'CardServices': ServicesCards.objects.all()[:6],
        'cardchoose': CardChoose.objects.all()[:6],
        'chooseabout': ChooseAbout.objects.all()[:4],
        'portfoliotype': PortfoliosType.objects.all(),
        'portfolios': Portfolios.objects.get(id=pk),
        'portfoliosget': Portfolios.objects.filter(type_id=pk),
        'testimonial': TestimonialsComment.objects.all(),
        'members': TeamMembers.objects.all(),
        'client': MainClients.objects.last(),
        'contact': ContactUs.objects.last(),
        'companyname': CompanyName.objects.last(),
        'news': NewsLetter.objects.last(),
        'official': OfficialLink.objects.last(),
        'logo': LogoImg.objects.last()
    }
    return render(request,'portfolios.html',context)

def Form(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        FormContact.objects.create(fullname=fullname,email=email,subject=subject,message=message)
        return redirect('index')


def FooterForm(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        FormFooter.objects.create(name=text)
        return redirect('index')

