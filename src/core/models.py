from django.db import models


class Business(models.Model):
    business_type = models.CharField(max_length=100)

    def __str__(self):
        return self.business_type 
    class Meta:
        verbose_name = "Тип бизнеса"
        verbose_name_plural = "Типы бизнеса"


class Direction(models.Model):
    direction = models.CharField(max_length=100)
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='Directions')

    def __str__(self):
        return self.direction
    class Meta:
        verbose_name = "Направление бизнеса"
        verbose_name_plural = "Направления бизнеса"


class Region(models.Model):
    region = models.CharField(max_length=100)

    def __str__(self):
        return self.region
    class Meta:
        verbose_name = "Регион бизнеса"
        verbose_name_plural = "Регионы бизнеса"


class City(models.Model):
    city = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        verbose_name = "Город бизнеса"
        verbose_name_plural = "Города бизнеса"
    def __str__(self):
        return self.city


class User(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField()
    previous_platform = models.CharField(max_length=100, blank=True, null=True)

    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='Users')
    business_direction = models.ForeignKey(Direction, on_delete=models.CASCADE, related_name='Users')

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='Users')
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='Users')

    answers_to_questions = models.TextField(blank=True, null=True)


    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"
    def __str__(self):
        return self.text


class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    questions = models.ManyToManyField(Question)

    class Meta:
            verbose_name = "Страница вопросов"
            verbose_name_plural = "Страницы вопросов"
    def __str__(self):
        return self.title
    

class QuestionForSurvey(models.Model):
    text = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Вопрос для опроса"
        verbose_name_plural = "Вопросы для опросов"
    def __str__(self):
        return self.text