from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False,
                                  verbose_name="Имя")
    second_name = models.CharField(max_length=255, null=True, blank=True,
                                   verbose_name="Отчество")
    last_name = models.CharField(max_length=255, null=False, blank=False,
                                 verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(null=True, blank=True,
                              verbose_name="Фото профиля")

    # documents = models.ForeignKey() подумать как можно сделать проверку препода

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"


class Course(models.Model):
    course_name = models.CharField(max_length=255,
                                   verbose_name="Название курса")
    teacher = models.ForeignKey(
        to=Teacher,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Преподаватель"
    )

    def __str__(self):
        return f"{self.course_name}"

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class CourseStudent(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False,
                                  verbose_name="Имя")
    second_name = models.CharField(max_length=255, null=True, blank=True,
                                   verbose_name="Отчество")
    last_name = models.CharField(max_length=255, null=False, blank=False,
                                 verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(null=True, blank=True,
                              verbose_name="Фото профиля")
    email = models.EmailField(verbose_name="Почта")
    course = models.ForeignKey(
        to=Course,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        verbose_name="Курс"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"


class VideoMaterial(models.Model):
    video_name = models.CharField(max_length=255,
                                  verbose_name="Название видео")
    video_file = models.FileField(verbose_name="Видеоматериал к уроку")
    video_description = models.TextField(max_length=1000,
                                         verbose_name="Описание видео")

    def __str__(self):
        return f"{self.video_name}"

    class Meta:
        verbose_name = "Видеоматериал"
        verbose_name_plural = "Видеоматериалы"


class TextMaterial(models.Model):
    text_name = models.CharField(max_length=255,
                                 verbose_name="Название текста")
    text_file = models.TextField(max_length=10000,
                                 verbose_name="Текстовый материал к уроку")
    text_description = models.TextField(max_length=1000,
                                        verbose_name="Описание к тексту")

    def __str__(self):
        return f"{self.text_name}"

    class Meta:
        verbose_name = "Текстовый материал к уроку"
        verbose_name_plural = "Текстовые материалы к уроку"


class Lesson(models.Model):
    course = models.ForeignKey(
        to=Course,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        verbose_name="Учебная группа"
    )
    number_of_lesson = models.PositiveIntegerField(
        verbose_name="Номер урока в курсе")
    lesson_name = models.CharField(max_length=255, null=False, blank=False,
                                   verbose_name="Название урока")
    video_file = models.ForeignKey(
        to=VideoMaterial,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name="Видеоматериал к уроку")
    text_file = models.ForeignKey(
        to=TextMaterial,
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        verbose_name="Текстовый материал к уроку")

    # text_file - подумать, как сделать написание урока - типо встроить ворд в сайт??
    # test_file - подумать, вставить типо гугл форму?

    def __str__(self):
        return f"{self.number_of_lesson}. {self.lesson_name}"

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"



