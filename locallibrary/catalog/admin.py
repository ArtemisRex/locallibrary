from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Language, Book, BookInstance

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

# Define the admin class
# Can now be extended to define model-specific admin behavior
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

# Allows display of book instances on the book record
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# Define the admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Define the admin class
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
   
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
# Register the admin class with the associated model
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book, BookAdmin)
#admin.site.register(BookInstance, BookInstanceAdmin)
