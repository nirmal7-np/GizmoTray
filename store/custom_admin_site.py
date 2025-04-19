from django.contrib.admin import AdminSite

class CustomAdminSite(AdminSite):
    site_header = "GizmoTray Admin"
    site_title = "GizmoTray Admin Portal"
    index_title = "Welcome to GizmoTray Admin"

custom_admin_site = CustomAdminSite(name='custom_admin')
