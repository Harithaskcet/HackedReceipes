from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Receipe(models.Model):
    name = models.CharField(max_length = 255)
    image = models.URLField(max_length = 200)
    category = models.CharField(max_length = 255)
    label = models.CharField(max_length = 255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    top = models.IntegerField()
    favourite = models.BooleanField()
    ingredients = ArrayField(models.CharField(max_length=200), blank=True)
    preparation = models.TextField()

    def summary(self):
        if len(self.description) > 100 :
            return self.description[:150]
        else:
            return self.description

    def getDesc(self):
        return "Soak rava and dal in water for about 1 hour." + "Drain dal and grind to a fine paste using little water. Add this paste to to rice rava and mix well."+"Cover and keep the batter to ferment for 6-8 hours or overnight in a warm place."+"Add salt and bring the batter to pouring consistency, if very thick."+"Heat a non stick tawa and drizzle some oil over it. Wipe off the oil and pour a ladleful of batter over it."+"Spread the batter to form a thick circle and lower the heat."+"When the top becomes a bit dry, spread pizza sauce over it."+"Sprinkle pizza seasoning and chilli flakes."+"Cover it and let it cook on low heat till the cheese melts."+"Uttapam pizza is ready to be devoured. Enjoy it."