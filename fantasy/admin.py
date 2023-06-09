from django.contrib import admin
from .models import Trainer, Pokemon
# Register your models here.
class PokemonInline(admin.TabularInline):
    model = Pokemon
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [
            PokemonInline,
    ]
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Pokemon)
