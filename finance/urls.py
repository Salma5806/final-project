from django.urls import path
from . import views

# Define URL patterns for the finance app

urlpatterns = [
    # URL for the index view - displays the main finance page
    path('', views.index, name="finance"),
    
    # URL for the add_bilan view - allows users to add a new bilan
    path('add-bilan', views.add_bilan, name="add-bilan"), 
    
    # URL for the bilan_edit view - allows users to edit an existing bilan by providing the bilan id in the URL
    path('edit-bilan/<int:id>', views.bilan_edit, name="edit-bilan"),
    
    # URL for the delete_bilan view - allows users to delete an existing bilan by providing the bilan id in the URL
    path('bilan-delete/<int:id>', views.delete_bilan, name="bilan-delete"),
    
    # URL for the bilan_summary view - displays a summary of all bilans
    path('bilan_summary', views.bilan_summary, name="bilan_summary"),
    
    # URL for the stats_view view - displays statistics for the finance app
    path('stats', views.stats_view, name="stats"),
    
    # URL for the export_csv view - allows users to export data in CSV format
    path('export-csv', views.export_csv, name="export-csv"),
    
    # URL for the export_excel view - allows users to export data in Excel format
    path('export-excel', views.export_excel, name="export-excel"),
    
    # URL for the export_pdf view - allows users to export data in PDF format
    path('export-pdf', views.export_pdf, name="export-pdf"),
]
