from django.db import models

# Create your models here.

class herohome(models.Model):
    name=models.CharField(max_length=120,blank=False)
    title=models.CharField(max_length=120,blank=False,verbose_name="Put a Header Title")
    image=models.ImageField(upload_to='portfolio_pics',verbose_name="Image")

    def __str__(self):
        return self.name

class about(models.Model):

    heading=models.CharField(max_length=120,blank=True)
    title=models.CharField(max_length=120,blank=True)
    description=models.TextField(max_length=220,blank=True)
    about_image=models.ImageField(upload_to='portfolio_pics',verbose_name="about picture",blank=True)


    def __str__(self):
        return self.heading

class skillname(models.Model):
    skill_name=models.CharField(max_length=120,blank=True)
    percentage=models.CharField(max_length=120,blank=True)

    def __str__(self):
        return self.skill_name

class service(models.Model):
    title=models.CharField(max_length=120,null=True)
    service_text=models.CharField(max_length=120,blank=True)
    sv_description=models.TextField(max_length=220,blank=True)

    def __str__(self):
        return self.title

class experience(models.Model):
    date=models.DateTimeField(blank=True)
    work_title=models.CharField(max_length=120,null=True,blank=False)
    wdescription=models.TextField(max_length=220,null=True)

    def __str__(self):
        return self.work_title

class banner(models.Model):
    title=models.CharField(max_length=220,blank=False)
    heading=models.CharField(max_length=220,null=True)
    description=models.TextField(max_length=220,null=True)

    def __str__(self):
        return self.heading

class portfolio(models.Model):
    heading=models.CharField(max_length=120,null=True)
    title=models.CharField(max_length=120,null=True)
    filter=models.CharField(max_length=120,null=True)
    service_image=models.ImageField(upload_to='site_pics',verbose_name="Image")
    servie_text=models.CharField(max_length=120,null=True)
    def __str__(self):
        return self.heading + " " + self.title



class discount(models.Model):
    title=models.CharField(max_length=120,null=True)
    cupon=models.CharField(max_length=120,null=True,verbose_name="put Discount!")
    details=models.TextField(max_length=220,null=True)

    def __str__(self):
        return self.title


class plan(models.Model):
    package_name=models.CharField(max_length=120,null=True)
    subscription=models.CharField(max_length=120,null=True)
    price_description=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.package_name

class client(models.Model):
    image=models.ImageField(upload_to='portfolio_pics',verbose_name="Image")
    name=models.CharField(max_length=220,verbose_name="Put Clinet Name!!")
    description=models.TextField(max_length=220,verbose_name="client Thougths!!")
    prof_name=models.CharField(max_length=120,null=True)

    def __str__(self):
        return self.name + " " +self.prof_name
