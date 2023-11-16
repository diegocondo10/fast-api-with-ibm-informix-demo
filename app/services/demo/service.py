from app.db.client import execute_sql_operation_return_list, execute_store_procedure_return_list
from app.services.demo.models import ObtenerMedicosResponse


class DemoService:
    @staticmethod
    def obtener_medicos() -> ObtenerMedicosResponse:
        sql = "SELECT * FROM medicos"
        return execute_sql_operation_return_list(sql)

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
        return execute_store_procedure_return_list(sql, parameters, index_column_names)
