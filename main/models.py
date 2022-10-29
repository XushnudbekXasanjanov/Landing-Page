from django.db import models

class MainMenu(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='mainmenu/')
    icon_first = models.CharField(max_length=255)
    icon_second = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class LogoImg(models.Model):
    img = models.ImageField(upload_to='logos/')


class OtherAbouts(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='secondabout/')

    def __str__(self):
        return self.title

class AboutusServices(models.Model):
    titleservices = models.CharField(max_length=255)
    textservices = models.TextField()

    def __str__(self):
        return self.titleservices

class MainAbout(models.Model):
    text = models.CharField(max_length=255)
    img = models.ImageField(upload_to='aboutdescription/')
    abouts = models.ManyToManyField(OtherAbouts)
    services = models.ManyToManyField(AboutusServices)

    def __str__(self):
        return self.text

class ServicesCards(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title



class CardChoose(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

class ChooseAbout(models.Model):
    name = models.CharField(max_length=255)
    number = models.IntegerField()

    def __str__(self):
        return self.name


class PortfoliosType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Portfolios(models.Model):
    name = models.CharField(max_length=255)
    type = models.ForeignKey(PortfoliosType,on_delete=models.CASCADE,related_name='typelar')
    img = models.ImageField(upload_to='portfolios/')

    def __str__(self):
        return self.name



class TestimonialsComment(models.Model):
    fullname = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    comment = models.TextField()
    img = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.fullname



class TeamMembers(models.Model):
    name = models.CharField(max_length=255)
    img = models.ImageField(upload_to='teammembers/')
    profession = models.CharField(max_length=255)
    instagramlink = models.CharField(max_length=999)
    facebooklink = models.CharField(max_length=999)
    twitterlink = models.CharField(max_length=999)
    telegramlink = models.CharField(max_length=999)

    def __str__(self):
        return self.name

class Clients(models.Model):
    img = models.ImageField(upload_to='clients/')



class MainClients(models.Model):
    client = models.ManyToManyField(Clients)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    adress = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.title

class FormContact(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.fullname

class CompanyName(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.name

class NewsLetter(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

class OfficialLink(models.Model):
    instagramlink = models.CharField(max_length=999)
    facebooklink = models.CharField(max_length=999)
    twitterlink = models.CharField(max_length=999)
    telegramlink = models.CharField(max_length=999)



class FormFooter(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name