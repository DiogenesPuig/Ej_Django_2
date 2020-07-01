from django.contrib import admin
from Super.models import *
# Register your models here.
class ProductoInline(admin.TabularInline):
    model = Producto

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('Calle','Numero','Ciudad')
    list_display_links = ('Calle','Numero','Ciudad')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','Nombre','WEB','Direccion')
    list_display_links = ('id','Nombre','WEB','Direccion')
    list_filter = ('Nombre','Provedor_Id')
    search_fields = ['Nombre','Provedor_Id']
    inlines = [ProductoInline,]

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Descripcion')
    list_display_links = ('Nombre','Descripcion')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Precio','Stock',)
    list_display_links = ('Nombre',)
    fieldsets = (
    ('Descripcion',{
        'fields': ('Nombre','Categoria','Proveedor')
    }),
    ('Variables',{
        'fields': ('Precio','Stock')
    })
    )

class DetalleAdmin(admin.ModelAdmin):
    list_display = ('Cantidad','nombre_prod')
    list_display_links = ('Cantidad','nombre_prod')

class VentaAdmin(admin.ModelAdmin):
    list_display = ('Detalle','Fecha','Monto_Final','Descuento',)
    list_display_links = ('Detalle','Fecha','Monto_Final','Descuento')
    actions = ['valDesc',]

    def valDesc(self,request,queryset):
        return queryset.update(Descuento = True)
    valDesc.short_description = "Validar Descuento"

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','Nombre','Telefono')
    list_display_links = ('id','Nombre','Telefono')
    search_fields = ['Nombre',]


admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Detalle,DetalleAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(Cliente,ClienteAdmin)
