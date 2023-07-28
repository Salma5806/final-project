from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bilan

class BilanModelTestCase(TestCase):
    def setUp(self):
        # Create a user for the test
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a Bilan instance for testing
        self.bilan = Bilan.objects.create(
            actif_immobilisé=1000,
            stock=500,
            créances=300,
            trésorerie_actif=200,
            capitaux_propre=800,
            dette_de_financement=400,
            dette_à_court_terme=300,
            type='Test Type',
            owner=self.user,
        )

    def test_calculate_passif(self):
        # Test the calculate_passif() method
        self.assertEqual(self.bilan.calculate_passif(), 1500)
    
    def test_calculate_actif(self):
        # Test the calculate_actif() method
        self.assertEqual(self.bilan.calculate_actif(), 2000)

    def test_calculate_fond_de_roulement(self):
        # Test the calculate_fond_de_roulement() method
        self.assertEqual(self.bilan.calculate_fond_de_roulement(), 100)
    
    def test_calculate_besoin_de_fond_roulement(self):
        # Test the calculate_besoin_de_fond_roulement() method
        self.assertEqual(self.bilan.calculate_besoin_de_fond_roulement(), 500)

    def test_calculate_tresorie_net(self):
        # Test the calculate_tresorie_net() method
        self.assertEqual(self.bilan.calculate_tresorie_net(), -400)
    
    def test_calculate_financement_permanent(self):
        # Test the calculate_financement_permanent() method
        self.assertEqual(self.bilan.calculate_financement_permanent(), 1.2)

    def test_calculate_autonomie_financiere(self):
        # Test the calculate_autonomie_financiere() method
        self.assertEqual(self.bilan.calculate_autonomie_financiere(), 0.4444)

    def test_calculate_solvabilite_general(self):
        # Test the calculate_solvabilite_general() method
        self.assertEqual(self.bilan.calculate_solvabilite_general(), 1.4286)
    
    def test_calculate_capacite_de_remboursement(self):
        # Test the calculate_capacite_de_remboursement() method
        self.assertEqual(self.bilan.calculate_capacite_de_remboursement(), 2.0)

    def test_commentaire_financement_permanent(self):
        # Test the commentaire_financement_permanent() method
        self.assertEqual(self.bilan.commentaire_financement_permanent(), "Financement permanent > 0: l'actif immobilisé est financé par les capitaux propres et l'entreprise possède des capitaux permanents supplémentaires pour financer des besoins d'exploitation.")
    
    def test_commentaire_autonomie_financiére(self):
        # Test the commentaire_autonomie_financiére() method
        self.assertEqual(self.bilan.commentaire_autonomie_financiére(), "l'entreprise est en manque de capitaux.")
    
    # Add more tests for other comment methods if needed

    def test_save_method(self):
        # Test the overridden save() method to ensure calculated fields are updated on save
        self.bilan.actif_immobilisé = 2000
        self.bilan.save()
        self.assertEqual(self.bilan.passif, 2500)
        self.assertEqual(self.bilan.actif, 2800)
        # Add more assertions for other calculated fields if needed

    def test_model_str_method(self):
        # Test the __str__ method of the Bilan model
        expected_str = f"Bilan ({self.bilan.type})"
        self.assertEqual(str(self.bilan), expected_str)
