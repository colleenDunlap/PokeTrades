from django.contrib import admin
from .models import Trainer, Pokemon, Trade
# Register your models here.
class PokemonInline(admin.TabularInline):
    model = Pokemon
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    inlines = [
            PokemonInline,
    ]
class TrainerInline(admin.TabularInline):
    model = Trainer
class TradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'trainer_1','pokemon_1', 'trainer_2','pokemon_2', 'status')
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Pokemon)
admin.site.register(Trade, TradeAdmin)
