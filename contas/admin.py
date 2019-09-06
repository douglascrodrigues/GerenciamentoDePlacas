from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Administrador,Requisitor, Supervisor,Tester


class UsuarioCriacaoForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ('username',)

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password('123@mudar')
        if commit:
            user.save()
        return user


class UsuarioAlteracaoForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'data_expiracao')


'''
ADMINISTRADOR
'''
class AdministradorInline(admin.StackedInline):
    model = Administrador
    max_num = 1

class AdministradorAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (AdministradorInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'A'
        super(AdministradorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(AdministradorAdmin, self).get_queryset(request)
        return resultado.filter(tipo='A')

class AdministradorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'administrador'
        verbose_name_plural = 'administradores'




'''
REQUISITOR
'''
class RequisitorInline(admin.StackedInline):
    model = Requisitor
    max_num = 1

class RequisitorAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (RequisitorInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'R'
        super(RequisitorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(RequisitorAdmin, self).get_queryset(request)
        return resultado.filter(tipo='R')

class RequisitorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'requisitor'
        verbose_name_plural = 'requisitores'



'''
SUPERVISOR
'''
class SupervisorInline(admin.StackedInline):
    model = Supervisor
    max_num = 1

class SupervisorAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (SupervisorInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'S'
        super(SupervisorAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(SupervisorAdmin, self).get_queryset(request)
        return resultado.filter(tipo='S')

class SupervisorUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'supervisor'
        verbose_name_plural = 'supervisores'



'''
TESTER
'''
class TesterInline(admin.StackedInline):
    model = Tester
    max_num = 1

class TesterAdmin(UserAdmin):
    form = UsuarioAlteracaoForm
    add_form = UsuarioCriacaoForm
    inlines = (TesterInline,)
    list_filter = ()
    list_display = ('username', 'tipo')
    fieldsets = (
        (None, {'fields': ('username', 'data_expiracao')}),
    )
    add_fieldsets = (
        (None, { 'fields': ('username',) } ),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    def save_model(self, request, obj, form, change):
        obj.tipo = 'T'
        super(TesterAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        resultado = super(TesterAdmin, self).get_queryset(request)
        return resultado.filter(tipo='T')

class TesterUsuario(Usuario):
    class Meta:
        proxy = True
        verbose_name = 'tester'
        verbose_name_plural = 'testers'
admin.site.register(AdministradorUsuario, AdministradorAdmin)
admin.site.register(RequisitorUsuario, RequisitorAdmin)
admin.site.register(SupervisorUsuario, SupervisorAdmin)
admin.site.register(TesterUsuario, TesterAdmin)