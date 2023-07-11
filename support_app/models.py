from django.db import models

from datetime import datetime


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")

    class Meta:
        abstract = True


class Agency(Base):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    uniq = models.CharField(max_length=100, verbose_name="Harf yoki soni", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Agentliklar"
        verbose_name_plural = "Agentliklar"


class Agent(Base):
    name = models.CharField(max_length=100, verbose_name="Ism")
    uniq = models.CharField(max_length=100, verbose_name="Harf yoki soni", unique=True, null=True, blank=True)
    agency = models.ManyToManyField(Agency, verbose_name="Agentlik")
    tg_id = models.BigIntegerField(unique=True, verbose_name="Telegram id", primary_key=True)

    def show_agency(self):
        return ",\n".join([g.name for g in self.agency.all()])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Agentlar"
        verbose_name_plural = "Agentlar"


class Project(Base):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    uniq = models.CharField(max_length=100, verbose_name="Harf yoki soni", unique=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name="Agentlik", related_name="project")
    file = models.FileField(verbose_name="Sertifikat", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Proektlar"
        verbose_name_plural = "Proektlar"


class Contract(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proekt")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name="Agent")
    inn = models.CharField(max_length=50, verbose_name="INN")
    code = models.CharField(max_length=50, verbose_name="Raqam")
    signature = models.TextField(verbose_name="Hujjat turi")
    status = models.BooleanField(default=True, verbose_name="Imzo")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Kontraklar"
        verbose_name_plural = "Kontraklar"


class Counter(Base):
    count = models.PositiveBigIntegerField(default=1)
    day = models.PositiveIntegerField(default=int(datetime.now().strftime("%d")))
