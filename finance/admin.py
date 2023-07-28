from django.contrib import admin
from .models import Bilan, Type

# Customizing the admin interface for the Bilan model
class BilanAdminSite(admin.ModelAdmin):
    model = Bilan

    # Specifying the fields to be displayed in the admin interface
    fields = ['actif_immobilisé', 'stock', 'créances', 'trésorerie_actif', 'capitaux_propre', 'dette_de_financement',
              'dette_à_court_terme', 'passif', 'actif', 'fond_de_roulement', 'besoin_de_fond_roulement', 'tresorerie_net',
              'financement_permanent', 'autonomie_financiere', 'solvabilite_general', 'capacite_de_remboursement',
              'financement_permanent_text', 'solvabilite_general_text', 'capacite_de_remboursement_text', 'autonomie_financiere_text']

    # Specifying the fields to be displayed in the list view of the admin interface
    list_display = ('actif_immobilisé', 'stock', 'créances', 'trésorerie_actif', 'capitaux_propre', 'dette_de_financement',
                    'dette_à_court_terme', 'passif', 'actif', 'fond_de_roulement', 'besoin_de_fond_roulement',
                    'tresorerie_net', 'financement_permanent', 'autonomie_financiere', 'solvabilite_general',
                    'capacite_de_remboursement', 'financement_permanent_text', 'solvabilite_general_text',
                    'capacite_de_remboursement_text', 'autonomie_financiere_text')


# Registering the Bilan model with the customized admin interface
admin.site.register(Bilan, BilanAdminSite)

# Registering the Type model with the default admin interface
admin.site.register(Type)
