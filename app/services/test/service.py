from app.services.test.models import MedicoIn


class TestService():

    @staticmethod
    def guardar_medico(medico: MedicoIn):
        print('GUARDADO EN BASE DE DATOS: ', medico)
        # execute_store_procedure_return_list
        return medico
