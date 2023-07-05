from django.contrib import admin
from app.models import Author, Location, JobPost, Skill


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "__str__")
    list_filter = ('date', 'salary')
    # Apartado de busqueda
    search_fields = ['title']
    search_help_text = "Busqueda por título"

    # Personalizar los formularios de la app en admin
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description', 'date')}),
        ('Mas informacion', {
            'classes': ('collapse',),  # Mantiene oculto la sección "mas info
            'fields': ('salary', 'expiry', 'slug')}),
        ('Ubicación', {
            'classes': ('collapse',),  # Mantiene oculto la sección "mas info
            'fields': ('location', )}),
        ('Autor', {
            'classes': ('collapse',),  # Mantiene oculto la sección "mas info
            'fields': ('author',)}),
        ('Habilidades requeridas', {
            'classes': ('collapse',),  # Mantiene oculto la sección "mas info
            'fields': ('skill',)}),
    )

# registro de modelos
admin.site.register(JobPost, JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)
