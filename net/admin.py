from django.urls import reverse
from django.utils.html import format_html
from django.contrib import admin
from .models import Product, Network


@admin.action(description='Set debt to 0')
def update_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'debt', 'parent_link')
    actions = [update_debt]
    list_filter = ('city',)

    def parent_link(self, obj):
        link = reverse("admin:net_network_change", args=[obj.parent_id])
        return format_html('<a href="{}">Supplier {}</a>', link, "link")

    parent_link.short_description = 'supplier link'


admin.site.register(Network, NetworkAdmin)
admin.site.register(Product)

