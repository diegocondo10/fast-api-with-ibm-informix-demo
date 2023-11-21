from app.db.client import select_return_list, sp_return_list
from app.services.demo.models import ObtenerMedicosResponse


class DemoService:
    @staticmethod
    def obtener_medicos() -> ObtenerMedicosResponse:
        sql = "SELECT * FROM medicos ORDER BY idmedico DESC"
        return select_return_list(sql)

    @staticmethod
    def obtene_medicos_filtro(i_nombre_medico: str) -> list:
        sql = "EXECUTE PROCEDURE fn_obtiene_medicos(:i_nombre_medico);"

        parameters = {
            "i_nombre_medico": i_nombre_medico
        }

        index_column_names = [
            "idmedico",
            "nombre",
            "apellidos",
            "ruc",
            "direccion",
            "correo",
            "telefono",
            "id_ciudad"
        ]
        return sp_return_list(sql, parameters, index_column_names)
