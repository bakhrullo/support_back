from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan sana")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="O'zgargan sana")

    class Meta:
        abstract = True


class Agent(Base):
    name = models.CharField(max_length=100, verbose_name="Ism")
    surname = models.CharField(max_length=100, verbose_name="Familya")
    phone = models.CharField(max_length=15, verbose_name="Raqam")
    tg_id = models.IntegerField(unique=True, verbose_name="Telegram id", primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Agentlar"
        verbose_name_plural = "Agentlar"


class Project(Base):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name="Agent")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Proektlar"
        verbose_name_plural = "Proektlar"


class Agency(Base):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name="Agent")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Agentliklar"
        verbose_name_plural = "Agentliklar"


class Contract(Base):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proekt")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, verbose_name="Agentlik")
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name="Agent")
    inn = models.CharField(max_length=50, verbose_name="INN")
    code = models.CharField(max_length=50, verbose_name="Raqam")
    status = models.BooleanField(default=False, verbose_name="Ahvoli")

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Kontraklar"
        verbose_name_plural = "Kontraklar"


class Certificate(Base):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Proekt")
    file = models.FileField(verbose_name="Fayl", upload_to="files")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sertifikatlar"
        verbose_name_plural = "Sertifikatlar"
